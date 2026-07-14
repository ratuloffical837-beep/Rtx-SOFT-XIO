"use client";

import { useAppStore } from '@/store/useAppStore';
import { Share2, CheckCircle2, Link as LinkIcon, DollarSign } from 'lucide-react';
import { useState, useEffect } from 'react';

export default function TasksTab({ userData }: { userData: any }) {
  const { t, telegramUser } = useAppStore();
  const [copied, setCopied] = useState(false);
  const [cpaOffers, setCpaOffers] = useState<any[]>([]);
  const [verifying, setVerifying] = useState<string | null>(null);

  const referralLink = `t.me/YourBotName?start=ref_${telegramUser?.id || 'dev'}`;

  const copyRef = () => {
    navigator.clipboard.writeText(referralLink);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  const socialTasks = [
    { id: 'join_channel', title: 'Join Main Telegram Channel', reward: 5 },
    { id: 'join_group', title: 'Join Main Telegram Group', reward: 5 },
    { id: 'start_bot1', title: 'Start Sponsor Bot 1', reward: 5 },
    { id: 'start_bot2', title: 'Start Sponsor Bot 2', reward: 5 },
    { id: 'start_bot3', title: 'Start Sponsor Bot 3', reward: 5 },
  ];

  const handleVerify = (taskId: string) => {
    setVerifying(taskId);
    setTimeout(() => {
      alert("Simulated verification. Backend will verify and award via /api/sync");
      setVerifying(null);
    }, 1500);
  };

  useEffect(() => {
    // Mock CPA Lead fetch
    setCpaOffers([
      { id: 1, title: 'Install App & Register', description: 'Download and open', amount: 1.5, link: '#' },
      { id: 2, title: 'Complete Survey', description: '5 min survey', amount: 0.8, link: '#' },
    ]);
  }, []);

  return (
    <div className="p-4 space-y-6">
      <div className="bg-[#1C2127] rounded-xl p-4 border border-gray-800">
        <div className="flex items-center gap-2 mb-4">
          <Share2 className="w-5 h-5 text-[#F3A63B]" />
          <h3 className="font-bold">{t('referral_title')}</h3>
        </div>
        
        <div className="bg-[#0B0E11] rounded-lg p-3 flex items-center justify-between mb-4 border border-gray-800">
          <span className="text-sm text-gray-400 truncate max-w-[70%]">{referralLink}</span>
          <button 
            onClick={copyRef}
            className="text-[#F3A63B] p-2 bg-[#F3A63B]/10 rounded hover:bg-[#F3A63B]/20 transition"
          >
            {copied ? <CheckCircle2 className="w-4 h-4" /> : <LinkIcon className="w-4 h-4" />}
          </button>
        </div>

        <div className="flex justify-between text-sm">
          <span className="text-gray-400">{t('total_referrals', { count: userData?.referralCount || 0 })}</span>
          <span className="text-[#F3A63B] font-bold">Bonus: {(userData?.referralCount || 0) * 10} RTX</span>
        </div>
      </div>

      <div className="bg-[#1C2127] rounded-xl p-4 border border-gray-800">
        <h3 className="font-bold mb-4 flex items-center gap-2">
          <DollarSign className="w-5 h-5 text-green-500" />
          {t('cpalead_offers')}
        </h3>
        <div className="space-y-3">
          {cpaOffers.map((offer) => (
            <div key={offer.id} className="bg-gray-800/40 rounded-lg p-3 border border-gray-700/50 flex justify-between items-center">
              <div>
                <h4 className="font-bold text-sm">{offer.title}</h4>
                <p className="text-xs text-gray-400">{offer.description}</p>
                <span className="inline-block mt-1 text-xs font-bold text-green-400">{(offer.amount * 0.5).toFixed(2)} USDT Reward</span>
              </div>
              <a 
                href={offer.link}
                target="_blank"
                rel="noreferrer"
                className="bg-green-600 hover:bg-green-700 text-white px-3 py-1.5 rounded text-xs font-bold"
              >
                {t('start_offer')}
              </a>
            </div>
          ))}
        </div>
      </div>

      <div className="bg-[#1C2127] rounded-xl p-4 border border-gray-800">
        <h3 className="font-bold mb-4 flex items-center gap-2">
          <CheckSquare className="w-5 h-5 text-blue-500" />
          {t('tasks_social')}
        </h3>
        <div className="space-y-3">
          {socialTasks.map((task) => {
            const isCompleted = userData?.completedTasks?.includes(task.id);
            return (
              <div key={task.id} className="bg-gray-800/40 rounded-lg p-3 border border-gray-700/50">
                <div className="flex justify-between items-start mb-2">
                  <h4 className="font-bold text-sm">{task.title}</h4>
                  <span className="text-[#F3A63B] text-xs font-bold">+{task.reward} RTX</span>
                </div>
                {isCompleted ? (
                  <div className="flex items-center gap-1 text-green-500 text-xs font-bold">
                    <CheckCircle2 className="w-4 h-4" /> Completed
                  </div>
                ) : (
                  <div className="flex gap-2">
                    <button className="flex-1 bg-gray-700 hover:bg-gray-600 text-white py-1.5 rounded text-xs font-bold transition">
                      {t('join')}
                    </button>
                    <button 
                      onClick={() => handleVerify(task.id)}
                      disabled={verifying === task.id}
                      className="flex-1 bg-blue-600 hover:bg-blue-700 text-white py-1.5 rounded text-xs font-bold transition disabled:opacity-50"
                    >
                      {verifying === task.id ? '...' : t('verify')}
                    </button>
                  </div>
                )}
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
}

// Needed icon imported below
import { CheckSquare } from 'lucide-react';
