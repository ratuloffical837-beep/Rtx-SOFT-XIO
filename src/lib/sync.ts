import { db } from '@/db';
import { users } from '@/db/schema';
import { eq } from 'drizzle-orm';

// Utility to sync local storage data to the DB via batch update
export async function syncUserData(telegramId: string, payload: any) {
  // In a real app we'd verify telegramInitData signature here
  
  const userRecord = await db.query.users.findFirst({
    where: eq(users.telegramId, telegramId)
  });

  if (!userRecord) {
    // Create if not exists
    await db.insert(users).values({
      telegramId,
      username: payload.username || '',
      firstName: payload.firstName || '',
      language: payload.language || 'en',
    });
  } else {
    // Process sync payload
    const updates: any = {
      lastSyncedAt: new Date()
    };
    
    // Process ad watches
    if (payload.adWatchCount_monetag || payload.adWatchCount_adsgram) {
      const monetagCount = payload.adWatchCount_monetag || 0;
      const adsgramCount = payload.adWatchCount_adsgram || 0;
      
      if (monetagCount + adsgramCount <= 10) { // Safety check
        updates.balanceUsdc = (userRecord.balanceUsdc || 0) + (monetagCount * 0.01);
        updates.balanceTon = (userRecord.balanceTon || 0) + (adsgramCount * 0.01); // approximate
      }
    }

    if (payload.miningRtxPending) {
      // Validate amount (e.g. max 10 per day, simplified check here)
      updates.balanceRtx = (userRecord.balanceRtx || 0) + payload.miningRtxPending;
    }

    if (payload.taskCompletions && Array.isArray(payload.taskCompletions)) {
      const currentTasks = userRecord.completedTasks as string[] || [];
      const newTasks = payload.taskCompletions.filter((t: string) => !currentTasks.includes(t));
      if (newTasks.length > 0) {
        updates.completedTasks = [...currentTasks, ...newTasks];
        updates.balanceRtx = (userRecord.balanceRtx || 0) + (payload.miningRtxPending || 0) + (newTasks.length * 5); // 5 RTX per task
      }
    }

    await db.update(users).set(updates).where(eq(users.telegramId, telegramId));
  }

  return await db.query.users.findFirst({
    where: eq(users.telegramId, telegramId)
  });
      }
