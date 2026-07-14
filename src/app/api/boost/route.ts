import { NextResponse } from 'next/server';
import { db } from '@/db';
import { boostRequests } from '@/db/schema';

export async function POST(request: Request) {
  try {
    const body = await request.json();
    const { userId, tonAmount, txid } = body;

    if (!userId || !tonAmount || !txid) {
      return NextResponse.json({ error: 'Missing parameters' }, { status: 400 });
    }

    await db.insert(boostRequests).values({
      userId,
      tonAmount,
      txid,
      status: 'pending'
    });

    // In a real app, send message to Admin Bot 2 here

    return NextResponse.json({ success: true });
  } catch (error: any) {
    return NextResponse.json({ error: error.message }, { status: 500 });
  }
  }
