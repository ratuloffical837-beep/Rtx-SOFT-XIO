"use client";

import { useState, useEffect } from 'react';
import { useAppStore } from '@/store/useAppStore';
import { Rocket, Info } from 'lucide-react';
import { motion } from 'framer-motion';

export default function MiningTab({ userData }: { userData: any }) {
  const { t, miningRtxPending, lastMiningSync, updateMining, telegramUser } = useAppStore();
  const [minedSoFar, setMinedSoFar] = useState(0);
  const [isPaused, setIsPaused] = useState(false);
  const [claimTimer, setClaimTimer] = useState(0);
  const [boostModal, setBoostModal] = useState<number | null>(null);

  const multiplier = userData?.miningMultiplier || 1.0;
  // Rate: 10 RTX per 24 hours = 0.416 RTX per hour. Multiplied.
  const ratePerHour = (10 / 24) * multiplier;
  const autoPauseHours = 1;

  useEffect(() => {
    const updateProgress = () => {
      const hoursElapsed = (Date.now() - lastMiningSync) / (1000 * 60 * 60);
      if (hoursElapsed >= autoPauseHours) {
        setMinedSoFar(autoPauseHours * ratePerHour);
        setIsPaused(true);
      } else {
        setMinedSoFar(hoursElapsed * ratePerHour);
        setIsPaused(false);
      }
    };
    
    updateProgress();
    const interval = setInterval(updateProgress, 10000);
    return () => clearInterval(interval);
  }, [lastMiningSync, ratePerHour]);

  useEffect(() => {
    if (claimTimer > 0) {
      const t = setTimeout(() => setClaimTimer(claimTimer - 1), 1000);
      return () => clearTimeout(t);
    } else if (claimTimer === 0 && isPaused) {
      // Simulate claim success
      // In real scenario we'd do the shortlink first, then start 15s timer
    }
  }, [claimTimer, isPaused]);

  const handleClaim = () => {
    // 50/50 Exe.io or ShrinkMe.io logic goes here
    // We simulate returning from shortlink and showing 15s timer
    alert("Simulating shortlink visit...");
    setTimeout(() => {
      setClaimTimer(15);
    }, 1000);
  };

  useEffect(() => {
    if (claimTimer === 1 && isPaused) {
      updateMining(minedSoFar);
      setMinedSoFar(0);
      setIsPaused(false);
      alert("Mining reward claimed!");
    }
  }, [claimTimer, isPaused, updateMining, minedSoFar]);

  const boostPackages = [
    { amount: 1, speed: '1.5x' },
    { amount: 5, speed: '2x' },
    { amount: 10, speed: '3x' },
    { amount: 25, speed: '5x' },
    { amount: 50, speed: '10x' }
  ];

  const handleBoostSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    const fd = new FormData(e.currentTarget);
    const txid = fd.get('txid') as string;
    if (!boostModal) return;

    const res = await fetch('/api/boost', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        userId: String(telegramUser.id),
        tonAmount: boostModal,
        txid
      })
    });
    
    if (res.ok) {
      alert("TXID Submitted for review");
      setBoostModal(null);
    }
  };

  return (
    <div className="p-4 space-y-6">
      <div className="bg-[#1C2127] rounded-xl p-6 border border-gray-800 flex flex-col items-center">
        <h2 className="text-lg font-bold mb-6">{t('mining_title')}</h2>
        
        <motion.div 
          animate={{ rotateY: 360 }}
          transition={{ duration: 3, repeat: Infinity, ease: "linear" }}
          className="w-24 h-24 bg-gradient-to-br from-[#F3A63B] to-yellow-600 rounded-full mb-6 flex items-center justify-center shadow-[0_0_30px_rgba(243,166,59,0.3)]"
          style={{ transformStyle: 'preserve-3d' }}
        >
          <span className="font-bold text-2xl text-black">RTX</span>
        </motion.div>

        <div className="w-full space-y-2 mb-6">
          <div className="flex justify-between text-sm">
            <span className="text-gray-400">Mining Progress</span>
            <span className="font-mono">{minedSoFar.toFixed(4)} / {(autoPauseHours * ratePerHour).toFixed(4)} RTX</span>
          </div>
          <div className="w-full h-3 bg-gray-800 rounded-full overflow-hidden">
            <div 
              className="h-full bg-[#F3A63B] transition-all duration-1000"
              style={{ width: `${Math.min(100, (minedSoFar / (autoPauseHours * ratePerHour)) * 100)}%` }}
            />
          </div>
          <p className="text-xs text-center text-gray-500">Current Speed: {multiplier}x</p>
        </div>

        {isPaused ? (
          <button 
            onClick={handleClaim}
            disabled={claimTimer > 0}
            className={`w-full py-3 rounded-lg font-bold transition ${
              claimTimer > 0 ? 'bg-gray-700 text-gray-400' : 'bg-[#F3A63B] text-black hover:bg-yellow-500'
            }`}
          >
            {claimTimer > 0 ? `Wait ${claimTimer}s...` : t('claim_mining')}
          </button>
        ) : (
          <div className="w-full py-3 rounded-lg font-bold text-center bg-gray-800 text-gray-400">
            Mining in progress...
          </div>
        )}
      </div>

      <div className="bg-[#1C2127] rounded-xl p-4 border border-gray-800">
        <div className="flex items-center gap-2 mb-4">
          <Rocket className="w-5 h-5 text-[#F3A63B]" />
          <h3 className="font-bold">{t('boost_shop')}</h3>
        </div>

        <div className="space-y-3">
          {boostPackages.map((pkg) => (
            <div key={pkg.amount} className="bg-gray-800/50 rounded-lg p-4 border border-gray-700/50 flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4">
              <div>
                <h4 className="font-bold text-lg">{pkg.speed} Speed Boost</h4>
                <p className="text-xs text-gray-400 flex items-center gap-1 mt-1">
                  <Info className="w-3 h-3" /> {t('boost_disclaimer')}
                </p>
              </div>
              <button 
                onClick={() => setBoostModal(pkg.amount)}
                className="shrink-0 bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded font-bold text-sm"
              >
                {t('buy_boost', { amount: pkg.amount })}
              </button>
            </div>
          ))}
        </div>
      </div>

      {boostModal && (
        <div className="fixed inset-0 bg-black/80 flex items-center justify-center p-4 z-[100]">
          <div className="bg-[#1C2127] rounded-xl w-full max-w-md p-6 relative">
            <button onClick={() => setBoostModal(null)} className="absolute top-4 right-4 text-gray-400">X</button>
            <h3 className="text-xl font-bold mb-2">Buy Boost ({boostModal} TON)</h3>
            <p className="text-sm text-gray-400 mb-4">Send exactly {boostModal} TON to the admin wallet below, then submit your TXID.</p>
            
            <div className="bg-gray-800 p-3 rounded mb-4 font-mono text-sm break-all">
              UQAdminWalletAddressHereToReceiveTON123456789
            </div>

            <form onSubmit={handleBoostSubmit} className="space-y-4">
              <div>
                <label className="block text-xs text-gray-400 mb-1">Transaction ID (TXID)</label>
                <input type="text" name="txid" required className="w-full bg-[#0B0E11] border border-gray-800 rounded p-2 text-white" />
              </div>
              <button type="submit" className="w-full bg-[#F3A63B] text-black font-bold py-3 rounded">
                {t('submit_txid')}
              </button>
            </form>
          </div>
        </div>
      )}
    </div>
  );
      }
