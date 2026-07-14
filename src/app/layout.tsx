import './globals.css';
import TelegramProvider from '@/components/TelegramProvider';

export const metadata = {
  title: 'RTX EARN',
  description: 'Telegram Mini App - RTX EARN',
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <head>
        <script src="https://telegram.org/js/telegram-web-app.js" async></script>
        <script src='//libtl.com/sdk.js' data-zone='11278383' data-sdk='show_11278383' async></script>
      </head>
      <body className="bg-[#0B0E11] text-[#FFFFFF] font-sans antialiased">
        <TelegramProvider>
          {children}
        </TelegramProvider>
      </body>
    </html>
  );
}
