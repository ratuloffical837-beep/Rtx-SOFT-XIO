# ═══════════════════════════════════════
# /start Command Handler
# ═══════════════════════════════════════

import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

log = logging.getLogger(__name__)


def _main_keyboard():
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("📦 Products", callback_data="products"),
            InlineKeyboardButton("💰 Price List", callback_data="price_list"),
        ],
        [
            InlineKeyboardButton("🎁 Promo Code", callback_data="promo"),
            InlineKeyboardButton("🎬 Demo", callback_data="demo"),
        ],
        [
            InlineKeyboardButton("❓ FAQ", callback_data="faq"),
            InlineKeyboardButton("👨‍💼 Support", callback_data="support"),
        ],
        [
            InlineKeyboardButton("📢 Channel", url="https://t.me/ratulhossain4241"),
            InlineKeyboardButton("👥 Group", url="https://t.me/ratulhossain424"),
        ],
        [
            InlineKeyboardButton("🎯 Sales Bot", url="https://t.me/rtxearn2_bot"),
        ],
    ])


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """User /start দিলে"""

    user = update.effective_user
    first_name = user.first_name or "ভাই"

    text = (
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"🌟 আসসালামু আলাইকুম {first_name} ভাই!\n"
        f"━━━━━━━━━━━━━━━━━━━━\n\n"
        f"স্বাগতম RTX Trading Family তে! 🎉\n\n"
        f"Bangladesh এর সবচেয়ে Powerful\n"
        f"Trading Signal Provider!\n\n"
        f"✅ Real Market Data (Binance + Forex)\n"
        f"✅ AI Powered Signal\n"
        f"✅ ৫ মিনিটে Access\n"
        f"✅ ২৪/২৪ Support\n"
        f"✅ Free Signal Available\n\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"👇 কী করতে চান?\n"
        f"━━━━━━━━━━━━━━━━━━━━"
    )

    try:
        await update.message.reply_text(
            text=text,
            reply_markup=_main_keyboard(),
        )
    except Exception as e:
        log.error(f"Start command error: {e}")
