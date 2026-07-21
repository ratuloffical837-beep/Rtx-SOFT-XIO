# ═══════════════════════════════════════
# Auto Post Scheduler
# AsyncIOScheduler - No Double Post
# ═══════════════════════════════════════

import logging
import asyncio
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from datetime import datetime
from config import CHANNEL_ID, GROUP_ID, POST_SCHEDULE, ONLY_CHANNEL
from services.ai_content import (
    generate_promotion_post,
    generate_educational_post,
    generate_success_story,
    generate_offer_post,
    generate_motivational_post,
    generate_signal_tips_post,
    generate_sigma_post,
    generate_emotional_post,
    generate_crypto_update_post,
    generate_market_analysis_post,
    generate_bot_links_post,
)

log = logging.getLogger(__name__)

_scheduler: AsyncIOScheduler = None

# Post type → generator mapping
GENERATORS = {
    "promotion":       generate_promotion_post,
    "educational":     generate_educational_post,
    "success_story":   generate_success_story,
    "offer":           generate_offer_post,
    "motivational":    generate_motivational_post,
    "signal_tips":     generate_signal_tips_post,
    "sigma":           generate_sigma_post,
    "emotional":       generate_emotional_post,
    "crypto_update":   generate_crypto_update_post,
    "market_analysis": generate_market_analysis_post,
    "bot_links":       generate_bot_links_post,
}


async def _send_post(application, post_type: str):
    """
    Channel (এবং প্রয়োজনে Group) এ post পাঠায়।
    ONLY_CHANNEL=True → শুধু channel (group এ auto-forward হবে)
    """
    now = datetime.now().strftime("%H:%M")
    generator = GENERATORS.get(post_type, generate_promotion_post)

    try:
        content = generator()
    except Exception as e:
        log.error(f"Content generation failed ({post_type}): {e}")
        return

    bot = application.bot

    # ─── Channel ───
    try:
        await bot.send_message(
            chat_id=CHANNEL_ID,
            text=content,
            disable_web_page_preview=True,
        )
        log.info(f"✅ [{now}] Channel ← {post_type}")
    except Exception as e:
        log.error(f"❌ [{now}] Channel post failed ({post_type}): {e}")

    # ─── Group (only if auto-forward disabled) ───
    if not ONLY_CHANNEL:
        try:
            await bot.send_message(
                chat_id=GROUP_ID,
                text=content,
                disable_web_page_preview=True,
            )
            log.info(f"✅ [{now}] Group ← {post_type}")
        except Exception as e:
            log.error(f"❌ [{now}] Group post failed ({post_type}): {e}")


async def _startup_post(application):
    """Deploy হওয়ার পর একটা startup post"""
    await asyncio.sleep(3)  # Bot ready হওয়ার জন্য
    content = (
        "━━━━━━━━━━━━━━━━━━━━\n"
        "🚀 RTX Bot Active! 🚀\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"
        "✅ ২৪/২৪ Signal Active\n"
        "✅ AI Auto Post চালু\n"
        "✅ সকাল ৫টা - রাত ১টা পোস্ট\n\n"
        "💎 আমাদের Signal Bot:\n\n"
        "🥉 Qutex Signal — 1,000tk\n"
        "   🤖 @qutex4241pro_bot\n\n"
        "🥈 Qutex Premium — 2,000tk\n"
        "   🤖 @qutexperiyam_bot\n\n"
        "🥇 RTX PRO MAX AI — 5,000tk\n"
        "   🤖 @rtxpromaxai4241_bot\n\n"
        "🎁 Promo Code: RTX4241\n"
        "💳 bKash/Nagad: 01725218874\n\n"
        "📢 @ratulhossain4241\n"
        "🎯 @rtxearn2_bot\n"
        "👨‍💼 @ratulhossain56\n"
        "━━━━━━━━━━━━━━━━━━━━"
    )
    try:
        await application.bot.send_message(
            chat_id=CHANNEL_ID,
            text=content,
            disable_web_page_preview=True,
        )
        if not ONLY_CHANNEL:
            await application.bot.send_message(
                chat_id=GROUP_ID,
                text=content,
                disable_web_page_preview=True,
            )
        log.info("✅ Startup post sent")
    except Exception as e:
        log.error(f"❌ Startup post failed: {e}")


def setup_scheduler(application):
    """
    Scheduler setup করে।
    main.py এর post_init থেকে call হয়।
    """
    global _scheduler

    _scheduler = AsyncIOScheduler(timezone="Asia/Dhaka")

    for schedule in POST_SCHEDULE:
        hour   = schedule["hour"]
        minute = schedule["minute"]
        ptype  = schedule["type"]

        _scheduler.add_job(
            _send_post,
            trigger=CronTrigger(
                hour=hour,
                minute=minute,
                timezone="Asia/Dhaka",
            ),
            args=[application, ptype],
            id=f"job_{ptype}_{hour:02d}_{minute:02d}",
            replace_existing=True,
            misfire_grace_time=60,
        )

    _scheduler.start()
    log.info(f"✅ Scheduler started — {len(POST_SCHEDULE)} jobs scheduled")
    log.info("📅 Post time: সকাল ৫টা — রাত ১টা (প্রতি ২০-৩০ মিনিটে)")

    # Startup post
    asyncio.ensure_future(_startup_post(application))
