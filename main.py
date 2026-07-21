# ═══════════════════════════════════════
# RTX Marketing Bot — Main Entry Point
# Professional | No Database | No Bugs
# ═══════════════════════════════════════

import sys
import logging
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
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


def _validate_config():
    """Startup এ critical config check করে"""
    errors = []
    if not BOT_TOKEN:
        errors.append("BOT_TOKEN missing")
    if not GEMINI_API_KEY:
        errors.append("GEMINI_API_KEY missing")
    if not CHANNEL_ID:
        errors.append("CHANNEL_ID missing")
    if not GROUP_ID:
        errors.append("GROUP_ID missing")
    if errors:
        for e in errors:
            log.critical(f"❌ Config Error: {e}")
        sys.exit(1)
    log.info("✅ Config validation passed")


async def post_init(application):
    """Bot ready হওয়ার পর চলে"""
    from services.scheduler import setup_scheduler
    setup_scheduler(application)
    log.info("✅ Scheduler initialized")
    log.info("═" * 40)
    log.info("  ✅ RTX Bot is LIVE! 🎉")
    log.info("═" * 40)


async def error_handler(update: object, context):
    """Global error handler"""
    log.error(f"Update error: {context.error}", exc_info=context.error)


def main():
    log.info("═" * 40)
    log.info("  🚀 RTX Marketing Bot Starting...")
    log.info("═" * 40)

    # ─── Config validate ───
    _validate_config()

    # ─── Keep Alive ───
    from keep_alive import keep_alive, start_ping
    keep_alive()
    start_ping()
    log.info("✅ Keep-alive system active")

    # ─── Import handlers ───
    from handlers.start import start_command
    from handlers.welcome import welcome_new_member
    from handlers.message_handler import handle_text_message
    from handlers.products import (
        show_all_products, show_product_detail,
        show_price_list, show_promo,
    )
    from handlers.callbacks import (
        buy_product, show_demo, show_faq,
        handle_faq_answer, show_support,
        help_payment, help_details, back_to_start,
    )

    # ─── Build Application ───
    app = (
        ApplicationBuilder()
        .token(BOT_TOKEN)
        .post_init(post_init)
        .build()
    )

    # ─── Global Error Handler ───
    app.add_error_handler(error_handler)

    # ═══════════════════════════════════════
    # Command Handlers
    # ═══════════════════════════════════════
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("menu", start_command))

    # ═══════════════════════════════════════
    # Callback Handlers
    # ═══════════════════════════════════════

    # Products
    app.add_handler(CallbackQueryHandler(show_all_products,   pattern="^products$"))
    app.add_handler(CallbackQueryHandler(show_product_detail, pattern="^detail_"))
    app.add_handler(CallbackQueryHandler(show_price_list,     pattern="^price_list$"))
    app.add_handler(CallbackQueryHandler(show_promo,          pattern="^promo$"))

    # Buy
    app.add_handler(CallbackQueryHandler(buy_product, pattern="^buy_"))

    # Demo
    app.add_handler(CallbackQueryHandler(show_demo, pattern="^demo$"))

    # FAQ
    app.add_handler(CallbackQueryHandler(show_faq,          pattern="^faq$"))
    app.add_handler(CallbackQueryHandler(show_faq,          pattern="^ask_question$"))
    app.add_handler(CallbackQueryHandler(handle_faq_answer, pattern="^faq_"))

    # Support
    app.add_handler(CallbackQueryHandler(show_support, pattern="^support$"))

    # Help Payment
    app.add_handler(CallbackQueryHandler(help_payment, pattern="^help_payment$"))
    app.add_handler(CallbackQueryHandler(help_details, pattern="^help_"))

    # Back
    app.add_handler(CallbackQueryHandler(back_to_start, pattern="^back_start$"))

    # ═══════════════════════════════════════
    # Message Handlers
    # ═══════════════════════════════════════

    # New member welcome
    app.add_handler(MessageHandler(
        filters.StatusUpdate.NEW_CHAT_MEMBERS,
        welcome_new_member,
    ))

    # Text message AI reply
    app.add_handler(MessageHandler(
        filters.TEXT & ~filters.COMMAND,
        handle_text_message,
    ))

    # ─── Run ───
    log.info("🚀 Starting polling...")
    app.run_polling(
        allowed_updates=["message", "callback_query", "chat_member"],
        drop_pending_updates=True,
    )


if __name__ == "__main__":
    main()
