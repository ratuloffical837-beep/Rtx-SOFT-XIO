"use client";

import { useAppStore } from '@/store/useAppStore';
import { Flame, Medal, Award } from 'lucide-react';
import clsx from 'clsx';

export default function EarnTab({ userData }: { userData: any }) {
  const { t } = useAppStore();

  const streakRewards = [5, 10, 15, 20, 30, 40, 50];
  const currentStreak = userData?.currentStreak || 0;

  const handleClaimStreak = () => {
    alert("Simulated Daily Streak Claim");
  };

  const leaderboard = [
    { rank: 1, username: 'crypto_king', amount: 5400 },
    { rank: 2, username: 'rtx_miner', amount: 3200 },
    { rank: 3, username: 'ton_master', amount: 2800 },
    { rank: 4, username: 'bd_trader', amount: 1500 },
    { rank: 5, username: 'earn_pro', amount: 900 },
  ];

  return (
    <div className="p-4 space-y-6">
      <div className="bg-[#1C2127] rounded-xl p-4 border border-gray-800">
        <div className="flex items-center gap-2 mb-4">
          <Flame className="w-5 h-5 text-orange-500" />
          <h3 className="font-bold">{t('daily_streak')}</h3>
        </div>
        
        <div className="flex justify-between mb-4">
          {streakRewards.map((reward, i) => (
            <div key={i} className="flex flex-col items-center">
              <div className={clsx(
                "w-8 h-8 rounded-full flex items-center justify-center text-xs font-bold mb-1",
                currentStreak > i ? "bg-orange-500 text-black" : "bg-gray-800 text-gray-500"
              )}>
                {i + 1}
              </div>
              <span className="text-[10px] text-gray-400">{reward}</span>
            </div>
          ))}
        </div>

        <button 
          onClick={handleClaimStreak}
          className="w-full bg-orange-500 hover:bg-orange-600 text-black font-bold py-2 rounded-lg transition"
        >
          {t('claim_streak')}
        </button>
      </div>

      <div className="bg-[#1C2127] rounded-xl p-4 border border-gray-800">
        <div className="flex items-center gap-2 mb-4">
          <Medal className="w-5 h-5 text-yellow-400" />
          <h3 className="font-bold">{t('leaderboard')}</h3>
        </div>
        
        <div className="space-y-2">
          {leaderboard.map((user) => (
            <div key={user.rank} className="flex justify-between items-center bg-[#0B0E11] p-3 rounded-lg border border-gray-800">
              <div className="flex items-center gap-3">
                <span className={clsx(
                  "font-bold w-6 text-center",
                  user.rank === 1 ? "text-yellow-400" : user.rank === 2 ? "text-gray-300" : user.rank === 3 ? "text-amber-600" : "text-gray-500"
                )}>#{user.rank}</span>
                <span className="text-sm">@{user.username}</span>
              </div>
              <span className="text-[#F3A63B] font-bold text-sm">{user.amount} RTX</span>
            </div>
          ))}
        </div>
      </div>

      <div className="bg-[#1C2127] rounded-xl p-4 border border-gray-800">
        <div className="flex items-center gap-2 mb-4">
          <Award className="w-5 h-5 text-blue-400" />
          <h3 className="font-bold">{t('achievements')}</h3>
        </div>

        <div className="grid grid-cols-2 gap-3">
          <div className="bg-[#0B0E11] p-3 rounded-lg border border-gray-800 text-center opacity-50">
            <div className="text-2xl mb-1">🎯</div>
            <div className="text-xs font-bold">First Ad Watched</div>
          </div>
          <div className="bg-[#0B0E11] p-3 rounded-lg border border-gray-800 text-center opacity-50">
            <div className="text-2xl mb-1">👥</div>
            <div className="text-xs font-bold">10 Referrals</div>
          </div>
          <div className="bg-[#0B0E11] p-3 rounded-lg border border-gray-800 text-center opacity-50">
            <div className="text-2xl mb-1">🔥</div>
            <div className="text-xs font-bold">7-Day Streak</div>
          </div>
          <div className="bg-[#0B0E11] p-3 rounded-lg border border-gray-800 text-center opacity-50">
            <div className="text-2xl mb-1">🤝</div>
            <div className="text-xs font-bold">First P2P Ad</div>
          </div>
        </div>
      </div>
    </div>
  );
    }
