"use client";

import { useState, useEffect } from 'react';
import { useAppStore } from '@/store/useAppStore';
import { Tv, MonitorPlay } from 'lucide-react';

export default function HomeTab({ userData }: { userData: any }) {
  const { t, todayAdCount, lastAdTime_monetag, lastAdTime_adsgram, setAdWatched } = useAppStore();
  const [monetagCooldown, setMonetagCooldown] = useState(0);
  const [adsgramCooldown, setAdsgramCooldown] = useState(0);

  useEffect(() => {
    const timer = setInterval(() => {
      const now = Date.now();
      const mDiff = 180000 - (now - lastAdTime_monetag);
      setMonetagCooldown(mDiff > 0 ? Math.ceil(mDiff / 1000) : 0);

      const aDiff = 180000 - (now - lastAdTime_adsgram);
      setAdsgramCooldown(aDiff > 0 ? Math.ceil(aDiff / 1000) : 0);
    }, 1000);
    return () => clearInterval(timer);
  }, [lastAdTime_monetag, lastAdTime_adsgram]);

  const handleMonetag = () => {
    if (todayAdCount >= 10) return alert('Daily ad limit reached!');
    if (monetagCooldown > 0) return;
    
    // @ts-ignore
    if (typeof show_11278383 === 'function') {
      // @ts-ignore
      show_11278383().then(() => {
        setAdWatched('monetag');
      }).catch((e: any) => {
        console.error('Monetag error', e);
        // Fallback for demo
        setAdWatched('monetag');
      });
    } else {
      // Mock for development
      setAdWatched('monetag');
    }
  };

  const handleAdsgram = () => {
    if (todayAdCount >= 10) return alert('Daily ad limit reached!');
    if (adsgramCooldown > 0) return;
    
    // Mock AdsGram SDK callback
    setTimeout(() => {
      setAdWatched('adsgram');
    }, 1000);
  };

  const formatTime = (seconds: number) => {
    const m = Math.floor(seconds / 60);
    const s = seconds % 60;
    return `${m}:${s.toString().padStart(2, '0')}`;
  };

  return (
    <div className="p-4 space-y-6">
      <div className="bg-[#1C2127] rounded-xl p-4 border border-gray-800 text-center">
        <h3 className="text-gray-400 text-sm">{t('ads_watched_today')}</h3>
        <p className="text-3xl font-bold mt-1 text-[#F3A63B]">{todayAdCount}/10</p>
      </div>

      <div className="grid grid-cols-2 gap-4">
        <div className="bg-[#1C2127] rounded-xl p-4 border border-gray-800 flex flex-col items-center text-center">
          <div className="w-12 h-12 bg-blue-500/20 text-blue-500 rounded-full flex items-center justify-center mb-3">
            <Tv className="w-6 h-6" />
          </div>
          <h4 className="font-bold mb-1">Monetag Ads</h4>
          <p className="text-xs text-gray-400 mb-4">+0.01 USDC</p>
          
          <button 
            onClick={handleMonetag}
            disabled={monetagCooldown > 0 || todayAdCount >= 10}
            className={`w-full py-2 rounded font-bold text-sm transition ${
              monetagCooldown > 0 || todayAdCount >= 10 ? 'bg-gray-800 text-gray-500 cursor-not-allowed' : 'bg-blue-600 text-white hover:bg-blue-700'
            }`}
          >
            {monetagCooldown > 0 ? `${t('wait')} ${formatTime(monetagCooldown)}` : t('watch_monetag')}
          </button>
        </div>

        <div className="bg-[#1C2127] rounded-xl p-4 border border-gray-800 flex flex-col items-center text-center">
          <div className="w-12 h-12 bg-purple-500/20 text-purple-500 rounded-full flex items-center justify-center mb-3">
            <MonitorPlay className="w-6 h-6" />
          </div>
          <h4 className="font-bold mb-1">AdsGram Ads</h4>
          <p className="text-xs text-gray-400 mb-4">+0.01 TON eq.</p>
          
          <button 
            onClick={handleAdsgram}
            disabled={adsgramCooldown > 0 || todayAdCount >= 10}
            className={`w-full py-2 rounded font-bold text-sm transition ${
              adsgramCooldown > 0 || todayAdCount >= 10 ? 'bg-gray-800 text-gray-500 cursor-not-allowed' : 'bg-purple-600 text-white hover:bg-purple-700'
            }`}
          >
            {adsgramCooldown > 0 ? `${t('wait')} ${formatTime(adsgramCooldown)}` : t('watch_adsgram')}
          </button>
        </div>
      </div>

      <div className="bg-[#1C2127] rounded-xl p-4 border border-gray-800">
        <h4 className="font-bold mb-3">Wallet Summary</h4>
        <div className="grid grid-cols-2 gap-y-3 text-sm">
          <div><span className="text-gray-400">USDT:</span> {userData?.balanceUsdt?.toFixed(2) || '0.00'}</div>
          <div><span className="text-gray-400">TON:</span> {userData?.balanceTon?.toFixed(2) || '0.00'}</div>
          <div><span className="text-gray-400">USDC:</span> {userData?.balanceUsdc?.toFixed(2) || '0.00'}</div>
          <div><span className="text-gray-400">RTX:</span> <span className="text-[#F3A63B] font-bold">{userData?.balanceRtx?.toFixed(2) || '0.00'}</span></div>
        </div>
      </div>
    </div>
  );
    }
