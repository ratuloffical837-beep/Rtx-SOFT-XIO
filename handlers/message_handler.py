# ═══════════════════════════════════════
# Smart Islamic Message Handler - Fixed
# ═══════════════════════════════════════

import time
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from config import REPLY_KEYWORDS, GROUP_COOLDOWN, PRIVATE_COOLDOWN
from services.ai_content import generate_smart_reply

log = logging.getLogger(__name__)

_cooldown_store: dict[int, float] = {}


def _reply_keyboard():
    """Reply এর নিচে সব buttons — /start এর মতো"""
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
            InlineKeyboardButton("🥉 Qutex Signal", url="https://t.me/qutex4241pro_bot/signalapp"),
        ],
        [
            InlineKeyboardButton("🥈 Qutex Premium", url="https://t.me/qutexperiyam_bot/qutexsignalbot"),
        ],
        [
            InlineKeyboardButton("🥇 RTX PRO MAX AI", url="https://t.me/rtxpromaxai4241_bot/binancesignalbot"),
        ],
        [
            InlineKeyboardButton("🎯 Sales Bot", url="https://t.me/rtxearn2_bot"),
            InlineKeyboardButton("👨‍💼 Admin", url="https://t.me/ratulhossain56"),
        ],
    ])


def _is_on_cooldown(user_id: int, cooldown: int) -> bool:
    now = time.time()
    last = _cooldown_store.get(user_id, 0)
    return (now - last) < cooldown


def _set_cooldown(user_id: int):
    _cooldown_store[user_id] = time.time()
    if len(_cooldown_store) > 500:
        oldest = sorted(_cooldown_store, key=_cooldown_store.get)[:100]
        for uid in oldest:
            del _cooldown_store[uid]


def _should_reply_in_group(text: str) -> bool:
    text_lower = text.lower()
    return any(kw.lower() in text_lower for kw in REPLY_KEYWORDS)


async def handle_text_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Smart Islamic message handler — সব buttons সহ"""

    if not update.message or not update.message.text:
        return

    message = update.message
    user_message = message.text.strip()

    if not user_message or user_message.startswith("/"):
        return

    user_id = message.from_user.id
    chat_type = update.effective_chat.type

    bot_username = context.bot.username
    if bot_username:
        user_message = user_message.replace(f"@{bot_username}", "").strip()

    if not user_message:
        return

    # Group logic
    if chat_type in ("group", "supergroup"):
        if not _should_reply_in_group(user_message):
            return
        if _is_on_cooldown(user_id, GROUP_COOLDOWN):
            return
    else:
        if _is_on_cooldown(user_id, PRIVATE_COOLDOWN):
            return

    _set_cooldown(user_id)

    try:
        await context.bot.send_chat_action(
            chat_id=update.effective_chat.id,
            action="typing",
        )
    except Exception:
        pass

    try:
        answer = generate_smart_reply(user_message)
    except Exception as e:
        log.error(f"Reply error: {e}")
        answer = (
            "আসসালামু আলাইকুম প্রিয় ভাই! 🌸\n\n"
            "আমাদের ৩টি Powerful Signal Bot আছে:\n"
            "🥉 Qutex Signal — 1,000tk\n"
            "🥈 Qutex Premium — 2,000tk\n"
            "🥇 RTX PRO MAX AI — 5,000tk\n\n"
            "🎁 Promo: RTX4241\n"
            "নিচের বাটন থেকে দেখুন ইনশাআল্লাহ 👇"
        )

    try:
        await message.reply_text(
            text=answer,
            reply_markup=_reply_keyboard(),
            reply_to_message_id=message.message_id,
        )
    except Exception as e:
        log.error(f"❌ Reply failed: {e}")
        try:
            await message.reply_text(text=answer, reply_markup=_reply_keyboard())
        except Exception:
            pass
