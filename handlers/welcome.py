# ═══════════════════════════════════════
# New Member Welcome
# ═══════════════════════════════════════

import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

log = logging.getLogger(__name__)


async def welcome_new_member(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Group এ নতুন member join করলে welcome"""

    if not update.message or not update.message.new_chat_members:
        return

    for member in update.message.new_chat_members:
        if member.is_bot:
            continue

        first_name = member.first_name or "ভাই"

        text = (
            f"━━━━━━━━━━━━━━━━━━━━\n"
            f"🌸 আসসালামু আলাইকুম {first_name} ভাই!\n"
            f"━━━━━━━━━━━━━━━━━━━━\n\n"
            f"বিসমিল্লাহির রহমানির রহিম 🤲\n\n"
            f"মাশাআল্লাহ! RTX Trading Family তে\n"
            f"আপনাকে পেয়ে আমরা অনেক খুশি! 🎉\n\n"
            f"📌 এখানে পাবেন:\n"
            f"  ✅ Powerful AI Trading Signal\n"
            f"  ✅ Free Signal (Daily)\n"
            f"  ✅ ২৪/২৪ Community Support\n"
            f"  ✅ Trading Tips & Guide\n\n"
            f"━━━━━━━━━━━━━━━━━━━━\n"
            f"💎 আমাদের ৪টি Signal Bot:\n\n"
            f"📈 Binary — @qutex4241pro_bot\n"
            f"   1,000tk (Promo: RTX4241)\n\n"
            f"💎 Binary Premium — @qutexperiyam_bot\n"
            f"   2,000tk (Promo: RTX4241)\n\n"
            f"💹 Forex — @rtxexness_bot\n"
            f"   8,000tk (Fixed)\n\n"
            f"🪙 Crypto — @rtxpromaxai4241_bot\n"
            f"   5,000tk (Fixed)\n\n"
            f"━━━━━━━━━━━━━━━━━━━━\n"
            f"🎁 Promo: RTX4241\n"
            f"💳 bKash/Nagad: 01725218874\n\n"
            f"ইনশাআল্লাহ সফলতা আসবে! 🚀\n"
            f"━━━━━━━━━━━━━━━━━━━━"
        )

        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("📈 Binary Trading", url="https://t.me/qutex4241pro_bot/signalapp")],
            [InlineKeyboardButton("💎 Binary Premium", url="https://t.me/qutexperiyam_bot/qutexsignalbot")],
            [InlineKeyboardButton("💹 Forex Trading", url="http://t.me/rtxexness_bot/rtxexsignalbot")],
            [InlineKeyboardButton("🪙 Crypto Trading", url="https://t.me/rtxpromaxai4241_bot/binancesignalbot")],
            [
                InlineKeyboardButton("🎯 Sales Bot", url="https://t.me/rtxearn2_bot"),
                InlineKeyboardButton("👨‍💼 Support", url="https://t.me/ratulhossain56"),
            ],
        ])

        try:
            await update.message.reply_text(text=text, reply_markup=keyboard)
        except Exception as e:
            log.error(f"Welcome error: {e}")
