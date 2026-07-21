# ═══════════════════════════════════════
# 15-Minute Rotation Scheduler
# সকাল ৫টা - রাত ১টা
# 00, 15, 30, 45 min এ ভিন্ন post
# ═══════════════════════════════════════

import logging
import asyncio
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from datetime import datetime
from config import CHANNEL_ID, GROUP_ID, ONLY_CHANNEL, POST_ROTATION, ACTIVE_HOURS
from services.ai_content import (
    generate_motivational_post,
    generate_bot_promo_post,
    generate_educational_post,
    generate_poll,
    get_startup_post,
)

log = logging.getLogger(__name__)

_scheduler: AsyncIOScheduler = None

# Track post rotation state
_rotation_index = 0

# Minute → post type mapping
MINUTE_TO_TYPE = {
    0:  "motivational",   # 00 min → motivational/sigma
    15: "poll",           # 15 min → interactive poll
    30: "bot_promo",      # 30 min → bot promotion
    45: "educational",    # 45 min → educational
}


async def _send_post(application, minute: int):
    """Post pathay based on minute"""
    now = datetime.now()
    hour = now.hour
    
    # Active hours check
    if hour not in ACTIVE_HOURS:
        log.info(f"⏸️ [{now.strftime('%H:%M')}] Inactive hour, skipping")
        return
    
    post_type = MINUTE_TO_TYPE.get(minute, "motivational")
    time_str = now.strftime("%H:%M")
    bot = application.bot

    try:
        # ═══ POLL ═══
        if post_type == "poll":
            poll_data = generate_poll()
            
            # Channel poll
            try:
                await bot.send_poll(
                    chat_id=CHANNEL_ID,
                    question=poll_data["question"],
                    options=poll_data["options"],
                    is_anonymous=True,
                )
                log.info(f"✅ [{time_str}] Channel ← poll")
            except Exception as e:
                log.error(f"❌ [{time_str}] Channel poll failed: {e}")
            
            # Group poll (if separate)
            if not ONLY_CHANNEL:
                try:
                    await bot.send_poll(
                        chat_id=GROUP_ID,
                        question=poll_data["question"],
                        options=poll_data["options"],
                        is_anonymous=True,
                    )
                    log.info(f"✅ [{time_str}] Group ← poll")
                except Exception as e:
                    log.error(f"❌ [{time_str}] Group poll failed: {e}")
            return
        
        # ═══ TEXT POSTS ═══
        generators = {
            "motivational": generate_motivational_post,
            "bot_promo":    generate_bot_promo_post,
            "educational":  generate_educational_post,
        }
        
        generator = generators.get(post_type, generate_motivational_post)
        content = generator()
        
        # Channel
        try:
            await bot.send_message(
                chat_id=CHANNEL_ID,
                text=content,
                disable_web_page_preview=True,
            )
            log.info(f"✅ [{time_str}] Channel ← {post_type}")
        except Exception as e:
            log.error(f"❌ [{time_str}] Channel post failed ({post_type}): {e}")
        
        # Group (only if no auto-forward)
        if not ONLY_CHANNEL:
            try:
                await bot.send_message(
                    chat_id=GROUP_ID,
                    text=content,
                    disable_web_page_preview=True,
                )
                log.info(f"✅ [{time_str}] Group ← {post_type}")
            except Exception as e:
                log.error(f"❌ [{time_str}] Group post failed ({post_type}): {e}")
                
    except Exception as e:
        log.error(f"❌ Post send error ({post_type}): {e}")


async def _startup_post(application):
    """Deploy হওয়ার পর startup post"""
    await asyncio.sleep(3)
    try:
        content = get_startup_post()
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
    """15-minute rotation scheduler setup"""
    global _scheduler
    
    _scheduler = AsyncIOScheduler(timezone="Asia/Dhaka")
    
    # Schedule for each 15-minute mark
    for minute in [0, 15, 30, 45]:
        _scheduler.add_job(
            _send_post,
            trigger=CronTrigger(
                minute=minute,
                timezone="Asia/Dhaka",
            ),
            args=[application, minute],
            id=f"post_min_{minute:02d}",
            replace_existing=True,
            misfire_grace_time=60,
        )
    
    _scheduler.start()
    log.info("═" * 40)
    log.info("✅ 15-Min Rotation Scheduler Started!")
    log.info("📅 সকাল ৫টা - রাত ১টা")
    log.info("⏱️  00 min → Motivational/Sigma")
    log.info("⏱️  15 min → Interactive Poll")
    log.info("⏱️  30 min → Bot Promotion")
    log.info("⏱️  45 min → Educational/Tips")
    log.info("═" * 40)
    
    # Send startup post
    asyncio.ensure_future(_startup_post(application))
