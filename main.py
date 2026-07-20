# ═══════════════════════════════════════
# RTX Marketing & Sales Bot
# Main Entry Point
# ═══════════════════════════════════════

import asyncio
import logging
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    filters,
)
from config import BOT_TOKEN
from keep_alive import keep_alive, start_ping
from services.scheduler import setup_scheduler
from handlers.start import start_command
from handlers.products import (
    show_all_products,
    show_product_detail,
    show_price_list,
    show_promo,
)
from handlers.welcome import welcome_new_member
from handlers.faq import handle_text_message
from handlers.callbacks import (
    buy_product,
    show_demo,
    show_faq,
    handle_faq_answer,
    show_support,
    help_payment,
    help_details,
    back_to_start,
)

# ═══════════════════════════════════════
# Logging Setup
# ═══════════════════════════════════════
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


async def post_init(application):
    """Bot start হওয়ার পর scheduler setup"""
    setup_scheduler(application.bot)
    print("✅ Auto-post scheduler active")
    print("═══════════════════════════════════════")
    print("  ✅ RTX Bot is LIVE! 🎉")
    print("═══════════════════════════════════════")


def main():
    """Bot চালু করে"""
    
    print("═══════════════════════════════════════")
    print("  🚀 RTX Marketing Bot Starting...")
    print("═══════════════════════════════════════")
    
    # ─── Keep Alive (bot ঘুমাবে না) ───
    keep_alive()
    start_ping()
    print("✅ Keep-alive system active")
    
    # ─── Bot Application তৈরি ───
    app = (
        ApplicationBuilder()
        .token(BOT_TOKEN)
        .post_init(post_init)
        .build()
    )
    
    # ═══════════════════════════════════════
    # Command Handlers
    # ═══════════════════════════════════════
    app.add_handler(CommandHandler("start", start_command))
    
    # ═══════════════════════════════════════
    # Callback (Button Click) Handlers
    # ═══════════════════════════════════════
    
    # Products
    app.add_handler(CallbackQueryHandler(show_all_products, pattern="^products$"))
    app.add_handler(CallbackQueryHandler(show_product_detail, pattern="^detail_"))
    app.add_handler(CallbackQueryHandler(show_price_list, pattern="^price_list$"))
    app.add_handler(CallbackQueryHandler(show_promo, pattern="^promo$"))
    
    # Buy
    app.add_handler(CallbackQueryHandler(buy_product, pattern="^buy_"))
    
    # Demo
    app.add_handler(CallbackQueryHandler(show_demo, pattern="^demo$"))
    
    # FAQ
    app.add_handler(CallbackQueryHandler(show_faq, pattern="^faq$"))
    app.add_handler(CallbackQueryHandler(handle_faq_answer, pattern="^faq_"))
    
    # Support
    app.add_handler(CallbackQueryHandler(show_support, pattern="^support$"))
    
    # Help
    app.add_handler(CallbackQueryHandler(help_payment, pattern="^help_payment$"))
    app.add_handler(CallbackQueryHandler(help_details, pattern="^help_"))
    
    # Ask question
    app.add_handler(CallbackQueryHandler(show_faq, pattern="^ask_question$"))
    
    # Back
    app.add_handler(CallbackQueryHandler(back_to_start, pattern="^back_start$"))
    
    # ═══════════════════════════════════════
    # Welcome New Members
    # ═══════════════════════════════════════
    app.add_handler(
        MessageHandler(
            filters.StatusUpdate.NEW_CHAT_MEMBERS,
            welcome_new_member,
        )
    )
    
    # ═══════════════════════════════════════
    # Text Message Handler (AI Reply)
    # ═══════════════════════════════════════
    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            handle_text_message,
        )
    )
    
    # ─── Bot চালু (polling) ───
    app.run_polling(
        allowed_updates=["message", "callback_query", "chat_member"],
        drop_pending_updates=True,
    )


if __name__ == "__main__":
    main()
