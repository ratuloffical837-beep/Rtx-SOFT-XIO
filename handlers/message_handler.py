# ═══════════════════════════════════════
# Smart Message Handler
# Private: সব message এ reply
# Group: keyword match হলে reply + cooldown
# Bot কথায় আটকে থাকবে না
# ═══════════════════════════════════════

import time
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from config import REPLY_KEYWORDS, GROUP_COOLDOWN, PRIVATE_COOLDOWN
from services.ai_content import generate_smart_reply

log = logging.getLogger(__name__)

# ─── In-memory cooldown store ───
# {user_id: last_reply_timestamp}
_cooldown_store: dict[int, float] = {}


def _reply_keyboard():
    """প্রতিটা reply এর নিচে এই buttons থাকবে"""
    return InlineKeyboardMarkup([
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


def _is_on_cooldown(user_id: int, cooldown: int) -> bool:
    """User cooldown এ আছে কিনা check করে"""
    now = time.time()
    last = _cooldown_store.get(user_id, 0)
    return (now - last) < cooldown


def _set_cooldown(user_id: int):
    """User এর cooldown set করে"""
    _cooldown_store[user_id] = time.time()

    # Memory leak prevent করতে পুরনো entries সরাও
    if len(_cooldown_store) > 500:
        oldest = sorted(_cooldown_store, key=_cooldown_store.get)[:100]
        for uid in oldest:
            del _cooldown_store[uid]


def _should_reply_in_group(message_text: str) -> bool:
    """Group এ এই message এ reply দেওয়া উচিত কিনা"""
    text_lower = message_text.lower()
    return any(kw.lower() in text_lower for kw in REPLY_KEYWORDS)


async def handle_text_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Main message handler।
    Private: সব message এ AI reply।
    Group: keyword match + cooldown check → AI reply।
    """

    # ─── Basic validation ───
    if not update.message or not update.message.text:
        return

    message = update.message
    user_message = message.text.strip()

    if not user_message or user_message.startswith("/"):
        return

    user_id   = message.from_user.id
    chat_type = update.effective_chat.type  # "private" / "group" / "supergroup"

    # ─── Bot mention remove ───
    bot_username = context.bot.username
    if bot_username:
        user_message = user_message.replace(f"@{bot_username}", "").strip()

    if not user_message:
        return

    # ═══════════════════════════════════════
    # GROUP LOGIC
    # ═══════════════════════════════════════
    if chat_type in ("group", "supergroup"):

        # keyword match না হলে skip (bot ব্যস্ত থাকবে না)
        if not _should_reply_in_group(user_message):
            return

        # cooldown check
        if _is_on_cooldown(user_id, GROUP_COOLDOWN):
            return

    # ═══════════════════════════════════════
    # PRIVATE LOGIC
    # ═══════════════════════════════════════
    else:
        if _is_on_cooldown(user_id, PRIVATE_COOLDOWN):
            return

    # ─── Cooldown set ───
    _set_cooldown(user_id)

    # ─── Typing action ───
    try:
        await context.bot.send_chat_action(
            chat_id=update.effective_chat.id,
            action="typing",
        )
    except Exception:
        pass

    # ─── AI Smart Reply ───
    try:
        answer = generate_smart_reply(user_message)
    except Exception as e:
        log.error(f"Smart reply error: {e}")
        answer = (
            "ভাই, ধন্যবাদ! 🙏\n"
            "বিস্তারিত জানতে @rtxearn2_bot এ মেসেজ দিন!"
        )

    # ─── Reply পাঠাও ───
    try:
        await message.reply_text(
            text=answer,
            reply_markup=_reply_keyboard(),
            reply_to_message_id=message.message_id,
        )
        log.info(f"✅ Reply sent [{chat_type}] to user {user_id}")
    except Exception as e:
        log.error(f"❌ Reply send failed: {e}")
        # Fallback without reply_to
        try:
            await message.reply_text(
                text=answer,
                reply_markup=_reply_keyboard(),
            )
        except Exception as e2:
            log.error(f"❌ Fallback reply also failed: {e2}")
