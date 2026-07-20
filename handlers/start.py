# ═══════════════════════════════════════
# /start Command Handler
# ═══════════════════════════════════════

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """User /start দিলে welcome message + buttons"""
    
    user = update.effective_user
    first_name = user.first_name or "ভাই"
    
    welcome_text = (
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"🌟 আসসালামু আলাইকুম {first_name} ভাই!\n"
        f"━━━━━━━━━━━━━━━━━━━━\n\n"
        f"স্বাগতম RTX Trading Family তে! 🎉\n\n"
        f"আমরা Bangladesh এর সবচেয়ে Powerful\n"
        f"Trading Signal Provider!\n\n"
        f"✅ Real Market Data\n"
        f"✅ High Accuracy Signal\n"
        f"✅ Instant Access (5 min)\n"
        f"✅ 24/7 Support\n"
        f"✅ Free Signal Available\n\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"👇 কী করতে চান? নিচে click করুন:\n"
        f"━━━━━━━━━━━━━━━━━━━━"
    )
    
    keyboard = [
        [
            InlineKeyboardButton("📦 Products দেখুন", callback_data="products"),
            InlineKeyboardButton("💰 Price List", callback_data="price_list"),
        ],
        [
            InlineKeyboardButton("🎁 Promo Code", callback_data="promo"),
            InlineKeyboardButton("🎬 Demo দেখুন", callback_data="demo"),
        ],
        [
            InlineKeyboardButton("❓ FAQ", callback_data="faq"),
            InlineKeyboardButton("👨‍💼 Support", callback_data="support"),
        ],
        [
            InlineKeyboardButton("📢 Channel Join", url="https://t.me/ratulhossain4241"),
            InlineKeyboardButton("👥 Group Join", url="https://t.me/ratulhossain424"),
        ],
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        text=welcome_text,
        reply_markup=reply_markup,
    )
