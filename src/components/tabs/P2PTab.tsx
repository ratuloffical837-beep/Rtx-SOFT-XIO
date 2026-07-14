"use client";

import { useState, useEffect } from 'react';
import { useAppStore } from '@/store/useAppStore';
import { Send, Plus, Search, MessageCircle } from 'lucide-react';
import clsx from 'clsx';

export default function P2PTab({ userData }: { userData: any }) {
  const { t, telegramUser } = useAppStore();
  const [filter, setFilter] = useState<'buy'|'sell'>('buy');
  const [listings, setListings] = useState<any[]>([]);
  const [postModal, setPostModal] = useState(false);
  const [transferModal, setTransferModal] = useState(false);

  const fetchListings = async () => {
    const res = await fetch('/api/p2p');
    if (res.ok) {
      const data = await res.json();
      setListings(data.listings);
    }
  };

  useEffect(() => {
    fetchListings();
  }, []);

  const handlePostSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    const fd = new FormData(e.currentTarget);
    const type = fd.get('type') as string;
    const rtxAmount = Number(fd.get('amount'));
    const pricePerRtx = Number(fd.get('price'));
    const methods = fd.getAll('methods') as string[];

    if (pricePerRtx < 1.0 || pricePerRtx > 3.0) {
      return alert(t('invalid_price'));
    }

    const res = await fetch('/api/p2p', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        ownerId: String(telegramUser.id),
        ownerUsername: telegramUser.username || telegramUser.first_name,
        type,
        rtxAmount,
        pricePerRtx,
        paymentMethods: methods
      })
    });

    if (res.ok) {
      setPostModal(false);
      fetchListings();
    } else {
      alert("Error posting ad");
    }
  };

  const handleTransfer = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    const fd = new FormData(e.currentTarget);
    const identifier = fd.get('identifier') as string;
    const amount = Number(fd.get('amount'));

    const res = await fetch('/api/p2p/transfer', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        senderId: String(telegramUser.id),
        receiverIdentifier: identifier,
        amount
      })
    });

    if (res.ok) {
      alert("Transfer successful!");
      setTransferModal(false);
    } else {
      const data = await res.json();
      alert("Transfer failed: " + data.error);
    }
  };

  const filteredListings = listings.filter(l => l.type === filter);

  return (
    <div className="p-4 space-y-6 relative min-h-screen">
      <div className="bg-[#1C2127] rounded-xl p-3 border border-gray-800 text-center sticky top-0 z-10">
        <span className="font-bold text-[#F3A63B]">{t('p2p_reference')}</span>
      </div>

      <div className="flex gap-2">
        <button 
          onClick={() => setFilter('buy')}
          className={clsx(
            "flex-1 py-2 rounded-lg font-bold transition text-sm",
            filter === 'buy' ? "bg-green-600 text-white" : "bg-gray-800 text-gray-400"
          )}
        >
          {t('buy_ads')}
        </button>
        <button 
          onClick={() => setFilter('sell')}
          className={clsx(
            "flex-1 py-2 rounded-lg font-bold transition text-sm",
            filter === 'sell' ? "bg-red-600 text-white" : "bg-gray-800 text-gray-400"
          )}
        >
          {t('sell_ads')}
        </button>
      </div>

      <div className="space-y-3 pb-24">
        {filteredListings.length === 0 ? (
          <div className="text-center text-gray-500 py-10">No ads found.</div>
        ) : (
          filteredListings.map(l => (
            <div key={l.id} className="bg-[#1C2127] rounded-xl p-4 border border-gray-800">
              <div className="flex justify-between items-start mb-2">
                <div className="font-bold">@{l.ownerUsername}</div>
                <div className={clsx("text-xs font-bold px-2 py-1 rounded", l.type === 'buy' ? 'bg-green-600/20 text-green-500' : 'bg-red-600/20 text-red-500')}>
                  {l.type.toUpperCase()}
                </div>
              </div>
              <div className="flex justify-between items-center mb-4">
                <div>
                  <div className="text-xl font-bold">{l.rtxAmount} RTX</div>
                  <div className="text-xs text-gray-400">{l.pricePerRtx} BDT/RTX</div>
                </div>
                <div className="text-right">
                  <div className="text-sm font-bold">Total: {(l.rtxAmount * l.pricePerRtx).toFixed(2)} BDT</div>
                  <div className="flex gap-1 mt-1 justify-end">
                    {l.paymentMethods.map((m: string) => (
                      <span key={m} className="text-[10px] bg-gray-800 px-1.5 py-0.5 rounded text-gray-300">{m}</span>
                    ))}
                  </div>
                </div>
              </div>
              <a 
                href={`https://t.me/${l.ownerUsername}`} 
                target="_blank" 
                rel="noreferrer"
                className="w-full flex items-center justify-center gap-2 bg-[#F3A63B] text-black py-2 rounded-lg font-bold text-sm"
              >
                <MessageCircle className="w-4 h-4" /> {t('contact')}
              </a>
            </div>
          ))
        )}
      </div>

      <div className="fixed bottom-20 left-0 w-full px-4 flex gap-2 z-20">
        <button 
          onClick={() => setPostModal(true)}
          className="flex-1 bg-blue-600 text-white font-bold py-3 rounded-xl shadow-lg flex justify-center items-center gap-2"
        >
          <Plus className="w-5 h-5" /> {t('post_ad')}
        </button>
        <button 
          onClick={() => setTransferModal(true)}
          className="flex-1 bg-[#F3A63B] text-black font-bold py-3 rounded-xl shadow-lg flex justify-center items-center gap-2"
        >
          <Send className="w-5 h-5" /> {t('transfer_rtx')}
        </button>
      </div>

      {/* Post Modal */}
      {postModal && (
        <div className="fixed inset-0 bg-black/90 flex items-center justify-center p-4 z-[100]">
          <div className="bg-[#1C2127] rounded-xl w-full max-w-md p-6 relative">
            <button onClick={() => setPostModal(false)} className="absolute top-4 right-4 text-gray-400">X</button>
            <h3 className="text-xl font-bold mb-4">{t('post_ad_title')}</h3>
            <form onSubmit={handlePostSubmit} className="space-y-4">
              <div>
                <label className="block text-xs text-gray-400 mb-1">{t('ad_type')}</label>
                <select name="type" className="w-full bg-[#0B0E11] border border-gray-800 rounded p-2 text-white">
                  <option value="buy">BUY</option>
                  <option value="sell">SELL</option>
                </select>
              </div>
              <div>
                <label className="block text-xs text-gray-400 mb-1">{t('amount')} (Min 10 RTX)</label>
                <input type="number" name="amount" min="10" required className="w-full bg-[#0B0E11] border border-gray-800 rounded p-2 text-white" />
              </div>
              <div>
                <label className="block text-xs text-gray-400 mb-1">{t('price_per_rtx')}</label>
                <input type="number" name="price" step="0.01" min="1.0" max="3.0" required className="w-full bg-[#0B0E11] border border-gray-800 rounded p-2 text-white" />
              </div>
              <div>
                <label className="block text-xs text-gray-400 mb-1">{t('payment_methods')}</label>
                <div className="flex gap-4">
                  <label className="flex items-center gap-2"><input type="checkbox" name="methods" value="Bkash" defaultChecked /> Bkash</label>
                  <label className="flex items-center gap-2"><input type="checkbox" name="methods" value="Nagad" /> Nagad</label>
                  <label className="flex items-center gap-2"><input type="checkbox" name="methods" value="Rocket" /> Rocket</label>
                </div>
              </div>
              <button type="submit" className="w-full bg-[#F3A63B] text-black font-bold py-3 rounded mt-4">
                {t('post')}
              </button>
            </form>
          </div>
        </div>
      )}

      {/* Transfer Modal */}
      {transferModal && (
        <div className="fixed inset-0 bg-black/90 flex items-center justify-center p-4 z-[100]">
          <div className="bg-[#1C2127] rounded-xl w-full max-w-md p-6 relative">
            <button onClick={() => setTransferModal(false)} className="absolute top-4 right-4 text-gray-400">X</button>
            <h3 className="text-xl font-bold mb-4">{t('transfer_title')}</h3>
            <form onSubmit={handleTransfer} className="space-y-4">
              <div>
                <label className="block text-xs text-gray-400 mb-1">{t('recipient_username')}</label>
                <input type="text" name="identifier" required className="w-full bg-[#0B0E11] border border-gray-800 rounded p-2 text-white" placeholder="@username or ID" />
              </div>
              <div>
                <label className="block text-xs text-gray-400 mb-1">{t('amount_rtx')}</label>
                <input type="number" name="amount" min="10" required className="w-full bg-[#0B0E11] border border-gray-800 rounded p-2 text-white" />
              </div>
              <button type="submit" className="w-full bg-blue-600 text-white font-bold py-3 rounded mt-4">
                {t('confirm_transfer')}
              </button>
            </form>
          </div>
        </div>
      )}
    </div>
  );
}
