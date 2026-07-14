"use client";

import { useState, useEffect } from 'react';
import { useAppStore } from '@/store/useAppStore';
import Header from '@/components/Header';
import BottomNav from '@/components/BottomNav';
import HomeTab from '@/components/tabs/HomeTab';
import MiningTab from '@/components/tabs/MiningTab';
import TasksTab from '@/components/tabs/TasksTab';
import P2PTab from '@/components/tabs/P2PTab';
import EarnTab from '@/components/tabs/EarnTab';
import { AlertCircle, X } from 'lucide-react';

export default function Home() {
  const [activeTab, setActiveTab] = useState('home');
  const { vpnWarningDismissed, dismissVpnWarning, t, telegramUser } = useAppStore();
  const [userData, setUserData] = useState<any>(null);

  useEffect(() => {
    if (telegramUser?.id) {
      // Sync on app open
      fetch('/api/sync', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          telegramId: String(telegramUser.id),
          payload: {
            username: telegramUser.username,
            firstName: telegramUser.first_name
          }
        })
      })
      .then(res => res.json())
      .then(data => {
        if (data.success) {
          setUserData(data.user);
        }
      });
    }
  }, [telegramUser]);

  return (
    <div className="flex flex-col min-h-screen bg-[#0B0E11] pb-20">
      <Header userData={userData} />

      {!vpnWarningDismissed && (
        <div className="bg-[#F6465D]/10 border-b border-[#F6465D]/20 p-4 mt-16">
          <div className="flex items-start gap-3">
            <AlertCircle className="text-[#F6465D] w-5 h-5 shrink-0 mt-0.5" />
            <div className="flex-1 text-sm text-[#F6465D]">
              {t('vpn_warning')}
            </div>
            <button onClick={dismissVpnWarning} className="shrink-0 p-1 bg-[#F6465D] text-white rounded text-xs px-3 py-1">
              {t('got_it')}
            </button>
          </div>
        </div>
      )}

      <main className={`flex-1 overflow-y-auto ${vpnWarningDismissed ? 'mt-16' : ''}`}>
        {activeTab === 'home' && <HomeTab userData={userData} />}
        {activeTab === 'mining' && <MiningTab userData={userData} />}
        {activeTab === 'tasks' && <TasksTab userData={userData} />}
        {activeTab === 'p2p' && <P2PTab userData={userData} />}
        {activeTab === 'earn' && <EarnTab userData={userData} />}
      </main>

      <BottomNav activeTab={activeTab} setActiveTab={setActiveTab} />
    </div>
  );
        }
