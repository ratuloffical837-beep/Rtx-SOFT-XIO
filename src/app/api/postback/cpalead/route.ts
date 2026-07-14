import { NextResponse } from 'next/server';
import { db } from '@/db';
import { users, cpaTransactions, adminStats } from '@/db/schema';
import { eq, sql } from 'drizzle-orm';

export async function GET(request: Request) {
  try {
    const { searchParams } = new URL(request.url);
    const subid = searchParams.get('subid');
    const amountStr = searchParams.get('amount');
    const currency = searchParams.get('currency');
    const transaction_id = searchParams.get('transaction_id');

    if (!subid || !amountStr || !transaction_id) {
      return new NextResponse('Missing required parameters', { status: 400 });
    }

    const existing = await db.query.cpaTransactions.findFirst({
      where: eq(cpaTransactions.transactionId, transaction_id)
    });
    if (existing) {
      return new NextResponse('OK', { status: 200 });
    }

    const userId = subid;
    const totalAmount = parseFloat(amountStr);
    const userAmount = totalAmount * 0.5;
    const adminAmount = totalAmount * 0.5;

    await db.transaction(async (tx) => {
      await tx.insert(cpaTransactions).values({
        transactionId: transaction_id,
        userId,
        amount: totalAmount,
        userAmount,
        adminAmount,
        currency: currency || 'USD',
      });

      const userRecord = await tx.query.users.findFirst({ where: eq(users.telegramId, userId) });
      if (userRecord) {
        await tx.update(users)
          .set({ balanceUsdt: (userRecord.balanceUsdt ?? 0) + userAmount })
          .where(eq(users.telegramId, userId));
      }

      const stats = await tx.query.adminStats.findFirst();
      if (!stats) {
        await tx.insert(adminStats).values({
          totalCPALeadProfit: adminAmount
        });
      } else {
        await tx.update(adminStats).set({
          totalCPALeadProfit: (stats.totalCPALeadProfit ?? 0) + adminAmount
        });
      }
    });

    return new NextResponse('OK', { status: 200 });
  } catch (error) {
    console.error('CPAlead postback error:', error);
    return new NextResponse('Error', { status: 500 });
  }
      }
