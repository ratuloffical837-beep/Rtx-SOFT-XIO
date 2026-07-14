"use client";

import { useEffect, useState } from 'react';
import { useAppStore } from '@/store/useAppStore';

export default function TelegramProvider({ children }: { children: React.ReactNode }) {
  const [mounted, setMounted] = useState(false);
  const { setTelegramUser } = useAppStore();

  useEffect(() => {
    setMounted(true);
    
    // Check if telegram WebApp is available
    if (typeof window !== 'undefined' && (window as any).Telegram?.WebApp) {
      const tg = (window as any).Telegram.WebApp;
      tg.ready();
      tg.expand();

      if (tg.initDataUnsafe?.user) {
        setTelegramUser(tg.initDataUnsafe.user);
      } else {
        // Mock user for local dev/preview
        setTelegramUser({
          id: '123456789',
          first_name: 'Dev User',
          username: 'dev_user'
        });
      }
    } else {
      // Mock user for local dev/preview
      setTelegramUser({
        id: '123456789',
        first_name: 'Preview User',
        username: 'preview_user'
      });
    }
  }, [setTelegramUser]);

  if (!mounted) return null; // Prevent hydration mismatch

  return <>{children}</>;
        }
