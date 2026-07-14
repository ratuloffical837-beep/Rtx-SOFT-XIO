import { NextResponse } from 'next/server';
import { db } from '@/db';
import { p2pListings } from '@/db/schema';
import { desc, eq } from 'drizzle-orm';

export async function GET() {
  const listings = await db.query.p2pListings.findMany({
    orderBy: [desc(p2pListings.createdAt)],
    where: eq(p2pListings.status, 'active')
  });
  return NextResponse.json({ listings });
}

export async function POST(request: Request) {
  try {
    const body = await request.json();
    const { ownerId, ownerUsername, type, rtxAmount, pricePerRtx, paymentMethods } = body;

    if (!ownerId || rtxAmount < 10 || pricePerRtx < 1.0 || pricePerRtx > 3.0) {
      return NextResponse.json({ error: 'Invalid parameters' }, { status: 400 });
    }

    const newListing = await db.insert(p2pListings).values({
      ownerId,
      ownerUsername,
      type,
      rtxAmount,
      pricePerRtx,
      paymentMethods,
      status: 'active'
    }).returning();

    return NextResponse.json({ success: true, listing: newListing[0] });
  } catch (error: any) {
    return NextResponse.json({ error: error.message }, { status: 500 });
  }
}
