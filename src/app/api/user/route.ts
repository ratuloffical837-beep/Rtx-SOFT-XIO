import { NextResponse } from 'next/server';
import { db } from '@/db';
import { users } from '@/db/schema';
import { eq } from 'drizzle-orm';

export async function GET(request: Request) {
  const { searchParams } = new URL(request.url);
  const telegramId = searchParams.get('id');

  if (!telegramId) {
    return NextResponse.json({ error: 'Missing id' }, { status: 400 });
  }

  const user = await db.query.users.findFirst({
    where: eq(users.telegramId, telegramId)
  });

  if (!user) {
    return NextResponse.json({ error: 'User not found' }, { status: 404 });
  }

  return NextResponse.json({ user });
}
