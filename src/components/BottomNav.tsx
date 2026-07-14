"use client";

import { useAppStore } from '@/store/useAppStore';
import { Home, Pickaxe, CheckSquare, ArrowRightLeft, Trophy } from 'lucide-react';
import clsx from 'clsx';

export default function BottomNav({ activeTab, setActiveTab }: { activeTab: string, setActiveTab: (t: string) => void }) {
  const { t } = useAppStore();

  const tabs = [
    { id: 'home', icon: Home, label: t('home_tab') },
    { id: 'mining', icon: Pickaxe, label: t('mining_tab') },
    { id: 'tasks', icon: CheckSquare, label: t('tasks_tab') },
    { id: 'p2p', icon: ArrowRightLeft, label: t('p2p_tab') },
    { id: 'earn', icon: Trophy, label: t('earn_tab') },
  ];

  return (
    <nav className="fixed bottom-0 w-full h-16 bg-[#1C2127] border-t border-gray-800 flex justify-around items-center px-2 pb-safe z-50">
      {tabs.map(tab => (
        <button
          key={tab.id}
          onClick={() => setActiveTab(tab.id)}
          className={clsx(
            "flex flex-col items-center justify-center w-full h-full space-y-1 transition-colors",
            activeTab === tab.id ? "text-[#F3A63B]" : "text-gray-500 hover:text-gray-300"
          )}
        >
          <tab.icon className="w-5 h-5" />
          <span className="text-[10px] font-medium tracking-wide">{tab.label}</span>
        </button>
      ))}
    </nav>
  );
     }
