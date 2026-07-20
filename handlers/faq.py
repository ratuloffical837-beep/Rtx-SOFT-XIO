# ═══════════════════════════════════════
# AI FAQ Handler
# যেকোনো text message এ AI reply দেয়
# ═══════════════════════════════════════

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from services.ai_content import generate_faq_answer


async def handle_text_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    User যেকোনো text লিখলে AI answer দেয়
    Group + Private দুই জায়গায় কাজ করবে
    """
    
    # Group message হলে check
    if update.effective_chat.type in ["group", "supergroup"]:
        # Group এ শুধু bot কে mention করলে reply দিবে
        # অথবা reply করলে
        if update.message.reply_to_message:
            if not update.message.reply_to_message.from_user.is_bot:
                return
        else:
            # Bot username mention check
            bot_username = context.bot.username
            if f"@{bot_username}" not in (update.message.text or ""):
                return
    
    user_message = update.message.text or ""
    
    # Bot username remove
    bot_username = context.bot.username
    user_message = user_message.replace(f"@{bot_username}", "").strip()
    
    if not user_message:
        return
    
    # "Typing..." action দেখায়
    await context.bot.send_chat_action(
        chat_id=update.effective_chat.id,
        action="typing",
    )
    
    # AI থেকে answer generate
    answer = generate_faq_answer(user_message)
    
    keyboard = [
        [
            InlineKeyboardButton("📦 Products", callback_data="products"),
            InlineKeyboardButton("💰 Price", callback_data="price_list"),
        ],
        [
            InlineKeyboardButton("🛒 কিনতে চাই", callback_data="products"),
            InlineKeyboardButton("👨‍💼 Support", callback_data="support"),
        ],
    ]
    
    await update.message.reply_text(
        text=answer,
        reply_markup=InlineKeyboardMarkup(keyboard),
  )
