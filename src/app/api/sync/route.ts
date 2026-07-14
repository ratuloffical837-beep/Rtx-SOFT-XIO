import { NextResponse } from 'next/server';
import { syncUserData } from '@/lib/sync';

export async function POST(request: Request) {
  try {
    const body = await request.json();
    const { telegramId, payload } = body;
    
    if (!telegramId) {
      return NextResponse.json({ error: 'Missing telegramId' }, { status: 400 });
    }

    const user = await syncUserData(telegramId, payload);
    
    return NextResponse.json({ success: true, user });
  } catch (error: any) {
    console.error('Sync Error:', error);
    return NextResponse.json({ error: error.message }, { status: 500 });
  }
}
