# ═══════════════════════════════════════
# RTX Marketing Bot — Main Entry Point
# ═══════════════════════════════════════

import sys
import logging
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    ContextTypes,
    filters,
)
from config import BOT_TOKEN, GEMINI_API_KEY, CHANNEL_ID, GROUP_ID

# ─── Logging ───
logging.basicConfig(
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    level=logging.INFO,
    handlers=[logging.StreamHandler(sys.stdout)],
)
log = logging.getLogger(__name__)

# ─── Suppress noisy loggers ───
logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("apscheduler").setLevel(logging.WARNING)
logging.getLogger("telegram.ext").setLevel(logging.INFO)


def _validate_config():
    """Config validation"""
    errors = []
    if not BOT_TOKEN:
        errors.append("BOT_TOKEN missing")
    if not CHANNEL_ID:
        errors.append("CHANNEL_ID missing")
    if not GROUP_ID:
        errors.append("GROUP_ID missing")
    
    if not GEMINI_API_KEY:
        log.warning("⚠️ GEMINI_API_KEY missing — AI reply disabled")
    
    if errors:
        for e in errors:
            log.critical(f"❌ Config Error: {e}")
        sys.exit(1)
    log.info("✅ Config validation passed")


async def post_init(application):
    """Bot ready হওয়ার পর"""
    from services.scheduler import setup_scheduler
    setup_scheduler(application)
    log.info("═" * 45)
    log.info("  ✅ RTX Marketing Bot is LIVE! 🎉")
    log.info("═" * 45)


async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE):
    """Global error handler"""
    log.error(f"Update error: {context.error}", exc_info=context.error)


def main():
    log.info("═" * 45)
    log.info("  🚀 RTX Marketing Bot Starting...")
    log.info("═" * 45)

    # Config validate
    _validate_config()

    # Keep Alive
    from keep_alive import keep_alive, start_ping
    keep_alive()
    start_ping()
    log.info("✅ Keep-alive system active")

    # Handlers import
    from handlers.start import start_command
    from handlers.welcome import welcome_new_member
    from handlers.message_handler import handle_text_message
    from handlers.callbacks import (
        show_category,
        buy_product,
        show_faq,
        handle_faq_answer,
        show_support,
        help_payment,
        help_details,
        back_to_start,
    )

    # Build Application
    app = (
        ApplicationBuilder()
        .token(BOT_TOKEN)
        .post_init(post_init)
        .build()
    )

    # Global Error Handler
    app.add_error_handler(error_handler)

    # ═══════════════════════════════════════
    # Command Handlers
    # ═══════════════════════════════════════
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("menu", start_command))
    app.add_handler(CommandHandler("help", show_faq))

    # ═══════════════════════════════════════
    # Callback Query Handlers
    # ═══════════════════════════════════════

    # 4 Category buttons
    app.add_handler(CallbackQueryHandler(show_category, pattern="^cat_"))

    # Buy
    app.add_handler(CallbackQueryHandler(buy_product, pattern="^buy_"))

    # FAQ
    app.add_handler(CallbackQueryHandler(show_faq, pattern="^faq$"))
    app.add_handler(CallbackQueryHandler(handle_faq_answer, pattern="^faq_"))

    # Support
    app.add_handler(CallbackQueryHandler(show_support, pattern="^support$"))

    # Help Payment (specific first!)
    app.add_handler(CallbackQueryHandler(help_payment, pattern="^help_payment$"))
    app.add_handler(CallbackQueryHandler(help_details, pattern="^help_"))

    # Back to start
    app.add_handler(CallbackQueryHandler(back_to_start, pattern="^back_start$"))

    # ═══════════════════════════════════════
    # Message Handlers
    # ═══════════════════════════════════════

    # New member welcome
    app.add_handler(MessageHandler(
        filters.StatusUpdate.NEW_CHAT_MEMBERS,
        welcome_new_member,
    ))

    # Text message reply
    app.add_handler(MessageHandler(
        filters.TEXT & ~filters.COMMAND,
        handle_text_message,
    ))

    # Run
    log.info("🚀 Starting polling...")
    app.run_polling(
        allowed_updates=["message", "callback_query", "chat_member"],
        drop_pending_updates=True,
    )


if __name__ == "__main__":
    main()
