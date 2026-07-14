import { NextResponse } from 'next/server';
import { db } from '@/db';
import { users, withdrawalRequests } from '@/db/schema';
import { eq } from 'drizzle-orm';

export async function POST(request: Request) {
  try {
    const body = await request.json();
    const { userId, currency, amount, walletAddress, network } = body;

    if (!userId || !currency || !amount || !walletAddress || !network) {
      return NextResponse.json({ error: 'Missing parameters' }, { status: 400 });
    }

    const user = await db.query.users.findFirst({ where: eq(users.telegramId, userId) });
    if (!user) {
      return NextResponse.json({ error: 'User not found' }, { status: 404 });
    }

    let hasBalance = false;
    if (currency === 'usdt' && (user.balanceUsdt ?? 0) >= amount && amount >= 2) hasBalance = true;
    if (currency === 'ton' && (user.balanceTon ?? 0) >= amount && amount >= 5) hasBalance = true;
    if (currency === 'usdc' && (user.balanceUsdc ?? 0) >= amount && amount >= 5) hasBalance = true;

    if (!hasBalance) {
      return NextResponse.json({ error: 'Insufficient balance or below minimum' }, { status: 400 });
    }

    await db.insert(withdrawalRequests).values({
      userId,
      currency,
      amount,
      walletAddress,
      network,
      status: 'pending'
    });

    // In a real app, send message to Admin Bot 1 here

    return NextResponse.json({ success: true });
  } catch (error: any) {
    return NextResponse.json({ error: error.message }, { status: 500 });
  }
                                }
