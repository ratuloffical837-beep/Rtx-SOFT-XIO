# ═══════════════════════════════════════
# New Member Welcome Handler
# Group এ নতুন member join করলে welcome
# ═══════════════════════════════════════

from telegram import Update
from telegram.ext import ContextTypes


async def welcome_new_member(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """নতুন member join করলে welcome message"""
    
    for member in update.message.new_chat_members:
        # Bot নিজেকে welcome করবে না
        if member.is_bot:
            continue
        
        first_name = member.first_name or "ভাই"
        
        welcome_text = (
            f"━━━━━━━━━━━━━━━━━━━━\n"
            f"🎉 স্বাগতম {first_name} ভাই!\n"
            f"━━━━━━━━━━━━━━━━━━━━\n\n"
            f"RTX Trading Family তে আপনাকে পেয়ে\n"
            f"আমরা আনন্দিত! 🌟\n\n"
            f"📌 এখানে আপনি পাবেন:\n"
            f"  ✅ Free trading tips\n"
            f"  ✅ Signal updates\n"
            f"  ✅ Community support\n"
            f"  ✅ Live proof & results\n\n"
            f"━━━━━━━━━━━━━━━━━━━━\n\n"
            f"💎 আমাদের Signal Bot গুলো:\n\n"
            f"🥉 Qutex Signal - 1,000tk (Promo)\n"
            f"🥈 Qutex Premium - 2,000tk (Promo)\n"
            f"🥇 RTX PRO MAX AI - 5,000tk\n\n"
            f"🎁 Promo Code: RTX4241\n\n"
            f"━━━━━━━━━━━━━━━━━━━━\n\n"
            f"🎯 বিস্তারিত জানতে:\n"
            f"👉 @rtxearn2_bot\n\n"
            f"📢 Channel: @ratulhossain4241\n\n"
            f"━━━━━━━━━━━━━━━━━━━━"
        )
        
        await update.message.reply_text(text=welcome_text)
