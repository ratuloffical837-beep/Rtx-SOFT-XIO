"use client";

import { useState } from 'react';
import { useAppStore } from '@/store/useAppStore';
import { Settings, HelpCircle, X } from 'lucide-react';

export default function Header({ userData }: { userData: any }) {
  const { t, language, setLanguage, telegramUser } = useAppStore();
  const [menuOpen, setMenuOpen] = useState(false);
  const [withdrawModalOpen, setWithdrawModalOpen] = useState(false);

  return (
    <>
      <header className="fixed top-0 w-full h-16 bg-[#0B0E11] border-b border-gray-800 flex items-center justify-between px-4 z-50">
        <div className="flex items-center gap-2">
          <div className="w-8 h-8 rounded-full bg-[#F3A63B] flex items-center justify-center font-bold text-black">
            R
          </div>
          <span className="font-bold text-lg text-white">RTX EARN</span>
        </div>

        <div className="flex items-center gap-3 relative">
          <div 
            className="flex items-center gap-2 cursor-pointer bg-gray-800/50 px-3 py-1.5 rounded-full"
            onClick={() => setMenuOpen(!menuOpen)}
          >
            <span className="text-sm font-medium">{telegramUser?.first_name || 'User'}</span>
            <div className="w-6 h-6 rounded-full bg-gray-700 flex items-center justify-center text-xs">
              {telegramUser?.first_name?.charAt(0) || 'U'}
            </div>
          </div>

          {menuOpen && (
            <div className="absolute top-12 right-0 w-64 bg-[#1C2127] border border-gray-800 rounded-xl shadow-xl overflow-hidden">
              <div className="p-3 border-b border-gray-800 flex justify-between items-center bg-[#252b33]">
                <div className="flex gap-2">
                  <button 
                    onClick={() => setLanguage('en')}
                    className={`px-2 py-1 text-xs rounded ${language === 'en' ? 'bg-[#F3A63B] text-black font-bold' : 'text-gray-400'}`}
                  >
                    EN
                  </button>
                  <button 
                    onClick={() => setLanguage('bn')}
                    className={`px-2 py-1 text-xs rounded ${language === 'bn' ? 'bg-[#F3A63B] text-black font-bold' : 'text-gray-400'}`}
                  >
                    বাংলা
                  </button>
                </div>
              </div>

              <div className="p-4">
                <div className="flex items-center justify-between mb-3">
                  <h4 className="text-sm font-semibold text-gray-300">{t('wallet_title')}</h4>
                  <HelpCircle className="w-4 h-4 text-gray-500 cursor-pointer" onClick={() => alert(t('help_wallet'))}/>
                </div>
                
                <div className="space-y-3">
                  <div className="flex justify-between items-center text-sm">
                    <span className="text-gray-400">USDT (BEP20)</span>
                    <span className="font-mono text-white">{(userData?.balanceUsdt || 0).toFixed(2)}</span>
                  </div>
                  <div className="flex justify-between items-center text-sm">
                    <span className="text-gray-400">TON (TON)</span>
                    <span className="font-mono text-white">{(userData?.balanceTon || 0).toFixed(2)}</span>
                  </div>
                  <div className="flex justify-between items-center text-sm">
                    <span className="text-gray-400">USDC (BEP20)</span>
                    <span className="font-mono text-white">{(userData?.balanceUsdc || 0).toFixed(2)}</span>
                  </div>
                  <div className="flex justify-between items-center text-sm">
                    <span className="text-gray-400 text-[#F3A63B]">RTX</span>
                    <span className="font-mono text-[#F3A63B]">{(userData?.balanceRtx || 0).toFixed(2)}</span>
                  </div>
                </div>

                <button 
                  onClick={() => setWithdrawModalOpen(true)}
                  className="w-full mt-4 bg-gray-800 text-white py-2 rounded-lg text-sm hover:bg-gray-700 transition"
                >
                  {t('withdraw')}
                </button>
              </div>
            </div>
          )}
        </div>
      </header>

      {withdrawModalOpen && (
        <div className="fixed inset-0 bg-black/80 flex items-center justify-center p-4 z-[100]">
          <div className="bg-[#1C2127] rounded-xl w-full max-w-sm p-6 relative">
            <button onClick={() => setWithdrawModalOpen(false)} className="absolute top-4 right-4 text-gray-400 hover:text-white">
              <X className="w-5 h-5" />
            </button>
            <h3 className="text-xl font-bold mb-4">{t('withdraw')}</h3>
            <form className="space-y-4" onSubmit={async (e) => {
              e.preventDefault();
              const fd = new FormData(e.currentTarget);
              const currency = fd.get('currency') as string;
              const amount = Number(fd.get('amount'));
              const address = fd.get('address') as string;
              
              let network = 'BEP20';
              if (currency === 'ton') network = 'TON Network';

              const res = await fetch('/api/withdraw', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({
                  userId: String(telegramUser.id),
                  currency,
                  amount,
                  walletAddress: address,
                  network
                })
              });
              if (res.ok) {
                alert('Withdrawal request submitted.');
                setWithdrawModalOpen(false);
              } else {
                const data = await res.json();
                alert('Error: ' + data.error);
              }
            }}>
              <div>
                <label className="block text-xs text-gray-400 mb-1">Currency</label>
                <select name="currency" className="w-full bg-[#0B0E11] border border-gray-800 rounded p-2 text-white">
                  <option value="usdt">USDT (Min 2)</option>
                  <option value="ton">TON (Min 5)</option>
                  <option value="usdc">USDC (Min 5)</option>
                </select>
              </div>
              <div>
                <label className="block text-xs text-gray-400 mb-1">Amount</label>
                <input type="number" step="0.01" name="amount" required className="w-full bg-[#0B0E11] border border-gray-800 rounded p-2 text-white" />
              </div>
              <div>
                <label className="block text-xs text-gray-400 mb-1">Wallet Address</label>
                <input type="text" name="address" required className="w-full bg-[#0B0E11] border border-gray-800 rounded p-2 text-white" />
              </div>
              <button type="submit" className="w-full bg-[#F3A63B] text-black font-bold py-3 rounded mt-2">
                {t('withdraw')}
              </button>
            </form>
          </div>
        </div>
      )}
    </>
  );
                    }
