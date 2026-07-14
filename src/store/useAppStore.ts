import { create } from 'zustand';
import { persist } from 'zustand/middleware';
import en from '../i18n/en.json';
import bn from '../i18n/bn.json';

const translations = { en, bn };

type Language = 'en' | 'bn';

interface AppState {
  language: Language;
  setLanguage: (lang: Language) => void;
  t: (key: keyof typeof en, params?: Record<string, string | number>) => string;
  vpnWarningDismissed: boolean;
  dismissVpnWarning: () => void;
  telegramUser: any | null;
  setTelegramUser: (user: any) => void;
  // Local storage for mining & ads
  lastAdTime_monetag: number;
  lastAdTime_adsgram: number;
  todayAdCount: number;
  adCountDate: string;
  setAdWatched: (type: 'monetag' | 'adsgram') => void;
  miningRtxPending: number;
  lastMiningSync: number;
  updateMining: (amount: number) => void;
}

export const useAppStore = create<AppState>()(
  persist(
    (set, get) => ({
      language: 'en',
      setLanguage: (lang) => set({ language: lang }),
      t: (key, params) => {
        const lang = get().language;
        let str = translations[lang][key] || translations['en'][key] || key;
        if (params) {
          Object.keys(params).forEach((p) => {
            str = str.replace(`{${p}}`, String(params[p]));
          });
        }
        return str;
      },
      vpnWarningDismissed: false,
      dismissVpnWarning: () => set({ vpnWarningDismissed: true }),
      telegramUser: null,
      setTelegramUser: (user) => set({ telegramUser: user }),
      
      lastAdTime_monetag: 0,
      lastAdTime_adsgram: 0,
      todayAdCount: 0,
      adCountDate: new Date().toISOString().split('T')[0],
      setAdWatched: (type) => {
        const now = Date.now();
        const today = new Date().toISOString().split('T')[0];
        set((state) => {
          const isNewDay = state.adCountDate !== today;
          return {
            [type === 'monetag' ? 'lastAdTime_monetag' : 'lastAdTime_adsgram']: now,
            todayAdCount: isNewDay ? 1 : state.todayAdCount + 1,
            adCountDate: today,
          };
        });
      },
      miningRtxPending: 0,
      lastMiningSync: Date.now(),
      updateMining: (amount) => set((state) => ({ 
        miningRtxPending: state.miningRtxPending + amount,
        lastMiningSync: Date.now()
      })),
    }),
    {
      name: 'rtx-earn-storage',
      partialize: (state) => ({
        language: state.language,
        vpnWarningDismissed: state.vpnWarningDismissed,
        lastAdTime_monetag: state.lastAdTime_monetag,
        lastAdTime_adsgram: state.lastAdTime_adsgram,
        todayAdCount: state.todayAdCount,
        adCountDate: state.adCountDate,
        miningRtxPending: state.miningRtxPending,
        lastMiningSync: state.lastMiningSync,
      }),
    }
  )
);
