# ═══════════════════════════════════════
# New Member Welcome Handler
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
            f"🎉 স্বাগতম {first_name} ভাই!\n"
            f"━━━━━━━━━━━━━━━━━━━━\n\n"
            f"RTX Trading Family তে আপনাকে\n"
            f"পেয়ে আমরা আনন্দিত! 🌟\n\n"
            f"📌 এখানে পাবেন:\n"
            f"  ✅ Free trading tips\n"
            f"  ✅ Signal updates\n"
            f"  ✅ ২৪/২৪ Community support\n\n"
            f"━━━━━━━━━━━━━━━━━━━━\n\n"
            f"💎 আমাদের Signal Bot:\n\n"
            f"🥉 Qutex Signal — 1,000tk\n"
            f"   👉 @qutex4241pro_bot\n"
            f"🥈 Qutex Premium — 2,000tk\n"
            f"   👉 @qutexperiyam_bot\n"
            f"🥇 RTX PRO MAX AI — 5,000tk\n"
            f"   👉 @rtxpromaxai4241_bot\n\n"
            f"🎁 Promo Code: RTX4241\n\n"
            f"━━━━━━━━━━━━━━━━━━━━"
        )

        keyboard = InlineKeyboardMarkup([
            [
                InlineKeyboardButton("📦 Products", callback_data="products"),
                InlineKeyboardButton("💰 Price", callback_data="price_list"),
            ],
            [
                InlineKeyboardButton("🎁 Promo", callback_data="promo"),
                InlineKeyboardButton("❓ FAQ", callback_data="faq"),
            ],
            [
                InlineKeyboardButton("🎯 Sales Bot", url="https://t.me/rtxearn2_bot"),
                InlineKeyboardButton("👨‍💼 Support", url="https://t.me/ratulhossain56"),
            ],
        ])

        try:
            await update.message.reply_text(
                text=text,
                reply_markup=keyboard,
            )
        except Exception as e:
            log.error(f"Welcome message error for {first_name}: {e}")
