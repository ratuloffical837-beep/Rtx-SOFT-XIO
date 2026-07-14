import { NextResponse } from 'next/server';
import { db } from '@/db';
import { users, transactions } from '@/db/schema';
import { eq, or } from 'drizzle-orm';

export async function POST(request: Request) {
  try {
    const body = await request.json();
    const { senderId, receiverIdentifier, amount } = body;

    if (!senderId || !receiverIdentifier || amount < 10) {
      return NextResponse.json({ error: 'Invalid parameters' }, { status: 400 });
    }

    // Wrap in transaction
    const result = await db.transaction(async (tx) => {
      const sender = await tx.query.users.findFirst({ where: eq(users.telegramId, senderId) });
      if (!sender || (sender.balanceRtx ?? 0) < amount) {
        throw new Error('Insufficient balance');
      }

      const receiver = await tx.query.users.findFirst({
        where: or(
          eq(users.telegramId, receiverIdentifier),
          eq(users.username, receiverIdentifier.replace('@', ''))
        )
      });

      if (!receiver) {
        throw new Error('Receiver not found');
      }

      if (sender.telegramId === receiver.telegramId) {
        throw new Error('Cannot transfer to yourself');
      }

      await tx.update(users)
        .set({ balanceRtx: (sender.balanceRtx ?? 0) - amount })
        .where(eq(users.telegramId, sender.telegramId));

      await tx.update(users)
        .set({ balanceRtx: (receiver.balanceRtx ?? 0) + amount })
        .where(eq(users.telegramId, receiver.telegramId));

      await tx.insert(transactions).values({
        senderId: sender.telegramId,
        receiverId: receiver.telegramId,
        amount,
        type: 'transfer',
        status: 'completed'
      });

      return { success: true };
    });

    return NextResponse.json(result);
  } catch (error: any) {
    return NextResponse.json({ error: error.message }, { status: 400 });
  }
}
