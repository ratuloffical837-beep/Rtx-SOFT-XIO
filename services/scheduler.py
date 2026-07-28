# ═══════════════════════════════════════
# 60 Post Scheduler - No Repeat System
# সকাল ৮টা - রাত ১১টা
# প্রতি ১৫ মিনিটে ১টা post
# শুধু Channel এ (Group এ না)
# ═══════════════════════════════════════

import logging
import asyncio
import random
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from datetime import datetime
from config import CHANNEL_ID, ACTIVE_HOURS, POST_MINUTES
from data.channel_posts import POSTS, get_post_count

log = logging.getLogger(__name__)

_scheduler: AsyncIOScheduler = None

# ═══════════════════════════════════════
# Post Queue System (No Repeat)
# ═══════════════════════════════════════
# _post_queue = shuffled 60 posts এর index list
# একবার সব post শেষ হলে আবার shuffle হয়
# ═══════════════════════════════════════

_post_queue: list[int] = []
_current_position: int = 0


def _refill_queue():
    """Queue খালি হলে নতুন shuffle করে refill"""
    global _post_queue, _current_position
    
    total = get_post_count()
    _post_queue = list(range(total))
    random.shuffle(_post_queue)
    _current_position = 0
    
    log.info(f"🔄 Post queue refilled & shuffled ({total} posts)")


def _get_next_post_index() -> int:
    """পরের unique post এর index দেয় (no repeat)"""
    global _current_position
    
    # Queue শেষ হলে refill
    if _current_position >= len(_post_queue):
        _refill_queue()
    
    index = _post_queue[_current_position]
    _current_position += 1
    return index


# Initial fill
_refill_queue()


# ═══════════════════════════════════════
# Post Sender
# ═══════════════════════════════════════

async def _send_channel_post(application):
    """Channel এ post পাঠায়"""
    now = datetime.now()
    hour = now.hour
    time_str = now.strftime("%H:%M")
    
    # Active hours check (8 AM - 10:45 PM, last slot 22:45)
    if hour not in ACTIVE_HOURS:
        log.info(f"⏸️ [{time_str}] Inactive hour, skip (hour={hour})")
        return
    
    # Get next unique post
    post_index = _get_next_post_index()
    post_text = POSTS[post_index]
    
    # Send to channel only
    try:
        await application.bot.send_message(
            chat_id=CHANNEL_ID,
            text=post_text,
            disable_web_page_preview=True,
        )
        log.info(
            f"✅ [{time_str}] Post #{post_index + 1}/60 sent "
            f"(Queue: {_current_position}/{len(_post_queue)})"
        )
    except Exception as e:
        log.error(f"❌ [{time_str}] Post send failed: {e}")


# ═══════════════════════════════════════
# Startup Post (Deploy হলে ১বার)
# ═══════════════════════════════════════

async def _startup_post(application):
    """Bot deploy হলে startup notification"""
    await asyncio.sleep(5)
    
    text = (
        "━━━━━━━━━━━━━━━━━━━━\n"
        "🌸 আসসালামু আলাইকুম প্রিয় ভাই!\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"
        "বিসমিল্লাহির রহমানির রহিম 🤲\n\n"
        "🚀 RTX Bot সম্পূর্ণ Active!\n\n"
        "⏰ Schedule:\n"
        "• সকাল ৮টা - রাত ১১টা\n"
        "• প্রতি ১৫ মিনিটে পোস্ট\n"
        "• দৈনিক ৬০টি Unique Post\n\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "💎 ৪টি Signal Bot:\n\n"
        "📈 Binary — @qutex4241pro_bot\n"
        "💎 Premium — @qutexperiyam_bot\n"
        "💹 Forex — @rtxexness_bot\n"
        "🪙 Crypto — @rtxpromaxai4241_bot\n\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "🎁 Promo: RTX4241\n"
        "💳 bKash/Nagad: 01725218874\n\n"
        "🎯 Sales: @rtxearn2_bot\n"
        "👨‍💼 Support: @ratulhossain56\n\n"
        "ইনশাআল্লাহ সফলতা আসবে! 🚀\n"
        "━━━━━━━━━━━━━━━━━━━━"
    )
    
    try:
        await application.bot.send_message(
            chat_id=CHANNEL_ID,
            text=text,
            disable_web_page_preview=True,
        )
        log.info("✅ Startup post sent to channel")
    except Exception as e:
        log.error(f"❌ Startup post failed: {e}")


# ═══════════════════════════════════════
# Scheduler Setup
# ═══════════════════════════════════════

def setup_scheduler(application):
    """15-minute scheduler setup"""
    global _scheduler
    
    _scheduler = AsyncIOScheduler(timezone="Asia/Dhaka")
    
    # প্রতি ১৫ মিনিটে (00, 15, 30, 45)
    for minute in POST_MINUTES:
        _scheduler.add_job(
            _send_channel_post,
            trigger=CronTrigger(
                minute=minute,
                timezone="Asia/Dhaka",
            ),
            args=[application],
            id=f"channel_post_min_{minute:02d}",
            replace_existing=True,
            misfire_grace_time=120,
        )
    
    _scheduler.start()
    
    log.info("═" * 45)
    log.info("✅ RTX Channel Post Scheduler Started!")
    log.info(f"⏰ Active Hours: {ACTIVE_HOURS[0]} AM - {ACTIVE_HOURS[-1]}:45 PM")
    log.info(f"📊 Total Posts/Day: {len(ACTIVE_HOURS) * 4}")
    log.info(f"📚 Unique Posts: {get_post_count()}")
    log.info(f"🔄 No Repeat System: Active")
    log.info(f"📢 Target: Channel Only (No Group)")
    log.info("═" * 45)
    
    # Startup post
    try:
        application.create_task(_startup_post(application))
    except AttributeError:
        # Fallback for older versions
        asyncio.get_event_loop().create_task(_startup_post(application))


def stop_scheduler():
    """Scheduler stop"""
    global _scheduler
    if _scheduler and _scheduler.running:
        _scheduler.shutdown()
        log.info("✅ Scheduler stopped gracefully")
