# ═══════════════════════════════════════
# Reply Handler - Group + Private
# Group এ সব text message এ reply দিবে
# ═══════════════════════════════════════

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from services.ai_content import generate_faq_answer


async def handle_text_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """সব text message এ AI reply"""
    
    # Message check
    if not update.message or not update.message.text:
        return
    
    user_message = update.message.text.strip()
    
    if not user_message:
        return
    
    # Command হলে skip
    if user_message.startswith("/"):
        return
    
    chat_type = update.effective_chat.type
    bot_username = context.bot.username
    
    # Bot mention remove
    if f"@{bot_username}" in user_message:
        user_message = user_message.replace(f"@{bot_username}", "").strip()
    
    if not user_message:
        return
    
    # ═══════════════════════════════════════
    # Typing action
    # ═══════════════════════════════════════
    try:
        await context.bot.send_chat_action(
            chat_id=update.effective_chat.id,
            action="typing",
        )
    except:
        pass
    
    # ═══════════════════════════════════════
    # AI answer generate
    # ═══════════════════════════════════════
    try:
        answer = generate_faq_answer(user_message)
    except Exception as e:
        print(f"AI Error: {e}")
        answer = (
            "ভাই, একটু পরে try করুন 🙏\n\n"
            "বিস্তারিত জানতে:\n"
            "👉 @rtxearn2_bot"
        )
    
    keyboard = [
        [
            InlineKeyboardButton("📦 Products", url="https://t.me/rtxearn2_bot"),
            InlineKeyboardButton("💰 Price", url="https://t.me/rtxearn2_bot"),
        ],
        [
            InlineKeyboardButton("🛒 কিনতে চাই", url="https://t.me/rtxearn2_bot"),
            InlineKeyboardButton("👨‍💼 Support", url="https://t.me/ratulhossain56"),
        ],
    ]
    
    # Reply পাঠাও
    try:
        await update.message.reply_text(
            text=answer,
            reply_markup=InlineKeyboardMarkup(keyboard),
            reply_to_message_id=update.message.message_id,
        )
        print(f"✅ Reply sent in {chat_type}")
    except Exception as e:
        print(f"❌ Reply failed: {e}")
        try:
            await update.message.reply_text(text=answer)
        except:
            pass
