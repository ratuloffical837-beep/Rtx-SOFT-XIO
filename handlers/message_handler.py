# ═══════════════════════════════════════
# Smart Group Reply Handler (Mode B)
# শুধু keyword থাকলে reply দেবে
# ═══════════════════════════════════════

import time
import logging
import threading
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from data.keywords import REPLY_KEYWORDS
from config import GROUP_COOLDOWN, PRIVATE_COOLDOWN
from services.ai_content import generate_smart_reply

log = logging.getLogger(__name__)

# Thread-safe cooldown
_cooldown_store: dict[int, float] = {}
_cooldown_lock = threading.Lock()


def _reply_keyboard():
    """Reply keyboard — main menu style"""
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("📈 Binary Trading", callback_data="cat_binary")],
        [InlineKeyboardButton("💎 Binary Premium", callback_data="cat_binary_premium")],
        [InlineKeyboardButton("💹 Forex Trading", callback_data="cat_forex")],
        [InlineKeyboardButton("🪙 Crypto Trading", callback_data="cat_crypto")],
        [
            InlineKeyboardButton("❓ FAQ", callback_data="faq"),
            InlineKeyboardButton("👨‍💼 Support", callback_data="support"),
        ],
        [InlineKeyboardButton("🎯 Sales Bot", url="https://t.me/rtxearn2_bot")],
    ])


def _is_on_cooldown(user_id: int, cooldown: int) -> bool:
    """Cooldown check (thread-safe)"""
    with _cooldown_lock:
        now = time.time()
        last = _cooldown_store.get(user_id, 0)
        return (now - last) < cooldown


def _set_cooldown(user_id: int):
    """Cooldown set (thread-safe)"""
    with _cooldown_lock:
        _cooldown_store[user_id] = time.time()
        # Memory cleanup
        if len(_cooldown_store) > 500:
            oldest = sorted(_cooldown_store, key=_cooldown_store.get)[:100]
            for uid in oldest:
                del _cooldown_store[uid]


def _should_reply_in_group(text: str) -> bool:
    """Group এ keyword থাকলে reply দেবে (Mode B)"""
    text_lower = text.lower()
    return any(kw.lower() in text_lower for kw in REPLY_KEYWORDS)


async def handle_text_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Group + Private message handler"""

    if not update.message or not update.message.text:
        return

    message = update.message
    user_message = message.text.strip()

    if not user_message or user_message.startswith("/"):
        return

    user_id = message.from_user.id
    chat_type = update.effective_chat.type

    # Bot mention remove
    bot_username = context.bot.username
    if bot_username:
        user_message = user_message.replace(f"@{bot_username}", "").strip()

    if not user_message:
        return

    # ═══ Group Logic (Mode B) ═══
    if chat_type in ("group", "supergroup"):
        # Bot কে reply করলেও reply দেবে
        is_reply_to_bot = (
            message.reply_to_message
            and message.reply_to_message.from_user
            and message.reply_to_message.from_user.id == context.bot.id
        )

        # Keyword check OR bot কে reply
        if not (_should_reply_in_group(user_message) or is_reply_to_bot):
            return

        if _is_on_cooldown(user_id, GROUP_COOLDOWN):
            return
    else:
        # Private cooldown
        if _is_on_cooldown(user_id, PRIVATE_COOLDOWN):
            return

    _set_cooldown(user_id)

    # Typing action
    try:
        await context.bot.send_chat_action(
            chat_id=update.effective_chat.id,
            action="typing",
        )
    except Exception:
        pass

    # Generate reply
    try:
        answer = generate_smart_reply(user_message)
    except Exception as e:
        log.error(f"Reply generation error: {e}")
        answer = (
            "আসসালামু আলাইকুম প্রিয় ভাই! 🌸\n\n"
            "আমাদের ৪টি Powerful Trading Bot:\n"
            "📈 Binary Trading — 1,000tk\n"
            "💎 Binary Premium — 2,000tk\n"
            "💹 Forex Trading — 8,000tk\n"
            "🪙 Crypto Trading — 5,000tk\n\n"
            "🎁 Promo: RTX4241\n"
            "নিচের বাটন থেকে দেখুন 👇"
        )

    # Send reply
    try:
        await message.reply_text(
            text=answer,
            reply_markup=_reply_keyboard(),
        )
    except Exception as e:
        log.error(f"Reply failed: {e}")
