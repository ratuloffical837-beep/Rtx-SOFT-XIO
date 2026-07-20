# ═══════════════════════════════════════
# AI FAQ Handler
# Group + Private এ সব message এ reply
# ═══════════════════════════════════════

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from services.ai_content import generate_faq_answer


async def handle_text_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    User যেকোনো text লিখলে AI answer দেয়
    """
    
    # Message check
    if not update.message or not update.message.text:
        return
    
    user_message = update.message.text.strip()
    
    if not user_message:
        return
    
    chat_type = update.effective_chat.type
    bot_username = context.bot.username
    
    # ═══════════════════════════════════════
    # Group এ কখন reply দিবে
    # ═══════════════════════════════════════
    if chat_type in ["group", "supergroup"]:
        should_reply = False
        
        # Case 1: Bot কে mention করলে
        if f"@{bot_username}" in user_message:
            should_reply = True
            user_message = user_message.replace(f"@{bot_username}", "").strip()
        
        # Case 2: Bot এর message এ reply দিলে
        elif update.message.reply_to_message:
            if update.message.reply_to_message.from_user:
                if update.message.reply_to_message.from_user.id == context.bot.id:
                    should_reply = True
        
        # Case 3: Trading related keywords থাকলে
        else:
            trading_keywords = [
                "signal", "bot", "trade", "trading", "forex", "crypto",
                "price", "cost", "buy", "kine", "kinbo", "kinbo",
                "সিগনাল", "বট", "দাম", "কিনব", "কিনবো", "কত", 
                "কিভাবে", "কেমন", "কোথায়", "প্রমো", "promo",
                "rtx", "qutex", "premium", "vip"
            ]
            
            message_lower = user_message.lower()
            for keyword in trading_keywords:
                if keyword.lower() in message_lower:
                    should_reply = True
                    break
        
        if not should_reply:
            return
    
    # ═══════════════════════════════════════
    # "Typing..." action দেখায়
    # ═══════════════════════════════════════
    try:
        await context.bot.send_chat_action(
            chat_id=update.effective_chat.id,
            action="typing",
        )
    except:
        pass
    
    # ═══════════════════════════════════════
    # AI থেকে answer generate
    # ═══════════════════════════════════════
    try:
        answer = generate_faq_answer(user_message)
    except Exception as e:
        print(f"AI Error: {e}")
        answer = (
            "ভাই, একটু পরে try করুন 🙏\n\n"
            "অথবা সরাসরি জানতে:\n"
            "👉 @rtxearn2_bot"
        )
    
    keyboard = [
        [
            InlineKeyboardButton("📦 Products", callback_data="products"),
            InlineKeyboardButton("💰 Price", callback_data="price_list"),
        ],
        [
            InlineKeyboardButton("🛒 কিনতে চাই", callback_data="products"),
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
    except Exception as e:
        print(f"Reply error: {e}")
        try:
            await update.message.reply_text(text=answer)
        except:
            pass
