# ═══════════════════════════════════════
# /start Command - New 4 Button Menu
# ═══════════════════════════════════════

import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

log = logging.getLogger(__name__)


def _main_keyboard():
    """Main menu keyboard — ৪টি Trading category"""
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("📈 Binary Trading", callback_data="cat_binary")],
        [InlineKeyboardButton("💎 Binary Premium", callback_data="cat_binary_premium")],
        [InlineKeyboardButton("💹 Forex Trading", callback_data="cat_forex")],
        [InlineKeyboardButton("🪙 Crypto Trading", callback_data="cat_crypto")],
        [
            InlineKeyboardButton("❓ FAQ", callback_data="faq"),
            InlineKeyboardButton("👨‍💼 Support", callback_data="support"),
        ],
        [
            InlineKeyboardButton("📢 Channel", url="https://t.me/ratulhossain4241"),
            InlineKeyboardButton("👥 Group", url="https://t.me/ratulhossain424"),
        ],
        [InlineKeyboardButton("🎯 Sales Bot", url="https://t.me/rtxearn2_bot")],
    ])


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """/start command handler"""
    user = update.effective_user
    first_name = user.first_name or "ভাই"

    text = (
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"🌸 আসসালামু আলাইকুম {first_name} ভাই!\n"
        f"━━━━━━━━━━━━━━━━━━━━\n\n"
        f"বিসমিল্লাহির রহমানির রহিম 🤲\n\n"
        f"মাশাআল্লাহ! RTX Trading Family তে\n"
        f"আপনাকে স্বাগতম! 🎉\n\n"
        f"Bangladesh এর সবচেয়ে Powerful\n"
        f"AI Trading Signal Provider!\n\n"
        f"✅ Real Market Data (Binance + Forex)\n"
        f"✅ Powerful AI Signal\n"
        f"✅ ৫ মিনিটে Access\n"
        f"✅ ২৪/২৪ Support\n"
        f"✅ Free Signal Available\n\n"
        f"ইনশাআল্লাহ সফলতা আসবে! 🚀\n\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"👇 কোন Trading এ interested?\n"
        f"━━━━━━━━━━━━━━━━━━━━"
    )

    keyboard = _main_keyboard()

    try:
        # Callback থেকে এলে edit করবে, command থেকে এলে reply
        if update.callback_query:
            await update.callback_query.edit_message_text(
                text=text, reply_markup=keyboard
            )
        else:
            await update.message.reply_text(text=text, reply_markup=keyboard)
    except Exception as e:
        log.error(f"Start error: {e}")
