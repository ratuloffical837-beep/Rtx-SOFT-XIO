# ═══════════════════════════════════════
# 15-Minute Scheduler — FIXED
# সকাল ৫টা - রাত ১২টা (00:00)
# ═══════════════════════════════════════

import logging
import asyncio
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from datetime import datetime
from config import CHANNEL_ID, GROUP_ID, ONLY_CHANNEL
from services.ai_content import (
    generate_motivational_post,
    generate_bot_promo_post,
    generate_educational_post,
    generate_poll,
    get_startup_post,
)

log = logging.getLogger(__name__)

_scheduler: AsyncIOScheduler = None


async def _send_post(application, minute: int):
    """Post send based on minute"""
    now = datetime.now()
    hour = now.hour
    time_str = now.strftime("%H:%M")
    
    # ═══ STRICT Active Hours: 5AM to 12AM (midnight) ═══
    # 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23
    if hour < 5:
        log.info(f"⏸️ [{time_str}] রাত, skip (hour={hour})")
        return
    
    bot = application.bot

    try:
        # ═══ POLL (15 min mark) ═══
        if minute == 15:
            poll_data = generate_poll()
            try:
                await bot.send_poll(
                    chat_id=CHANNEL_ID,
                    question=poll_data["question"],
                    options=poll_data["options"],
                    is_anonymous=True,
                )
                log.info(f"✅ [{time_str}] Channel ← poll")
            except Exception as e:
                log.error(f"❌ [{time_str}] Poll failed: {e}")
            
            if not ONLY_CHANNEL:
                try:
                    await bot.send_poll(
                        chat_id=GROUP_ID,
                        question=poll_data["question"],
                        options=poll_data["options"],
                        is_anonymous=True,
                    )
                except Exception as e:
                    log.error(f"❌ [{time_str}] Group poll failed: {e}")
            return
        
        # ═══ TEXT POSTS ═══
        if minute == 0:
            content = generate_motivational_post()
            ptype = "motivational"
        elif minute == 30:
            content = generate_bot_promo_post()
            ptype = "bot_promo"
        elif minute == 45:
            content = generate_educational_post()
            ptype = "educational"
        else:
            content = generate_motivational_post()
            ptype = "motivational"
        
        # Channel
        try:
            await bot.send_message(
                chat_id=CHANNEL_ID,
                text=content,
                disable_web_page_preview=True,
            )
            log.info(f"✅ [{time_str}] Channel ← {ptype}")
        except Exception as e:
            log.error(f"❌ [{time_str}] Channel failed ({ptype}): {e}")
        
        # Group (if no auto-forward)
        if not ONLY_CHANNEL:
            try:
                await bot.send_message(
                    chat_id=GROUP_ID,
                    text=content,
                    disable_web_page_preview=True,
                )
                log.info(f"✅ [{time_str}] Group ← {ptype}")
            except Exception as e:
                log.error(f"❌ [{time_str}] Group failed ({ptype}): {e}")
                
    except Exception as e:
        log.error(f"❌ Post error: {e}")


async def _startup_post(application):
    """Deploy startup post"""
    await asyncio.sleep(5)
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
    """15-minute rotation scheduler"""
    global _scheduler
    
    _scheduler = AsyncIOScheduler(timezone="Asia/Dhaka")
    
    # ═══ Schedule: minute 0, 15, 30, 45 ═══
    # Active hours handled inside _send_post
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
            misfire_grace_time=120,
        )
    
    _scheduler.start()
    log.info("═" * 40)
    log.info("✅ Scheduler Started!")
    log.info("⏰ সকাল ৫টা - রাত ১২টা")
    log.info("⏱️  00 min → Motivational/Sigma")
    log.info("⏱️  15 min → Interactive Poll")
    log.info("⏱️  30 min → Bot Promotion")
    log.info("⏱️  45 min → Educational/Tips")
    log.info("═" * 40)
    
    asyncio.ensure_future(_startup_post(application))
