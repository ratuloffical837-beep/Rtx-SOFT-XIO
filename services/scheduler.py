# ═══════════════════════════════════════
# Auto Post Scheduler
# ═══════════════════════════════════════

import asyncio
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from apscheduler.triggers.interval import IntervalTrigger
from datetime import datetime
from config import CHANNEL_ID, GROUP_ID, POST_SCHEDULE
from services.ai_content import (
    generate_promotion_post,
    generate_educational_post,
    generate_success_story,
    generate_offer_post,
    generate_motivational_post,
    generate_signal_tips_post,
)

scheduler = BackgroundScheduler(timezone="Asia/Dhaka")


def post_to_channel_and_group(bot, post_type):
    """Channel + Group এ post করে"""
    
    generators = {
        "promotion": generate_promotion_post,
        "educational": generate_educational_post,
        "success_story": generate_success_story,
        "offer": generate_offer_post,
        "motivational": generate_motivational_post,
        "signal_tips": generate_signal_tips_post,
    }
    
    content = generators.get(post_type, generate_promotion_post)()
    
    async def send_posts():
        # Channel এ post
        try:
            await bot.send_message(
                chat_id=CHANNEL_ID,
                text=content,
                disable_web_page_preview=True,
            )
            print(f"✅ [{datetime.now().strftime('%H:%M')}] Channel post: {post_type}")
        except Exception as e:
            print(f"❌ Channel post failed ({post_type}): {e}")
        
        # Group এ post
        try:
            await bot.send_message(
                chat_id=GROUP_ID,
                text=content,
                disable_web_page_preview=True,
            )
            print(f"✅ [{datetime.now().strftime('%H:%M')}] Group post: {post_type}")
        except Exception as e:
            print(f"❌ Group post failed ({post_type}): {e}")
    
    try:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(send_posts())
        loop.close()
    except Exception as e:
        print(f"❌ Scheduler error: {e}")


def setup_scheduler(bot):
    """Scheduler setup"""
    
    # ═══════════════════════════════════════
    # প্রতি ঘন্টায় নির্দিষ্ট post
    # ═══════════════════════════════════════
    for schedule in POST_SCHEDULE:
        scheduler.add_job(
            post_to_channel_and_group,
            CronTrigger(
                hour=schedule["hour"],
                minute=schedule["minute"],
                timezone="Asia/Dhaka",
            ),
            args=[bot, schedule["type"]],
            id=f"post_{schedule['type']}_{schedule['hour']}_{schedule['minute']}",
            replace_existing=True,
        )
        print(
            f"📅 Scheduled: {schedule['type']} at "
            f"{schedule['hour']:02d}:{schedule['minute']:02d}"
        )
    
    scheduler.start()
    print("✅ Scheduler started!")
    
    # ═══════════════════════════════════════
    # Deploy এর সাথে সাথে একটা post পাঠাও
    # (Test এর জন্য)
    # ═══════════════════════════════════════
    print("🚀 Sending instant startup post...")
    try:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        
        async def startup_post():
            try:
                msg = (
                    "━━━━━━━━━━━━━━━━━━━━\n"
                    "🚀 RTX Bot Active! 🚀\n"
                    "━━━━━━━━━━━━━━━━━━━━\n\n"
                    "✅ 24/7 Trading Signal\n"
                    "✅ Real-time Market Data\n"
                    "✅ Auto Post প্রতি ঘন্টায়\n\n"
                    "💎 Products:\n"
                    "🥉 Qutex Signal - 1000tk\n"
                    "🥈 Qutex Premium - 2000tk\n"
                    "🥇 RTX PRO MAX AI - 5000tk\n\n"
                    "🎁 Promo: RTX4241\n\n"
                    "🎯 @rtxearn2_bot"
                )
                await bot.send_message(CHANNEL_ID, msg)
                await bot.send_message(GROUP_ID, msg)
                print("✅ Startup post sent!")
            except Exception as e:
                print(f"❌ Startup post failed: {e}")
        
        loop.run_until_complete(startup_post())
        loop.close()
    except Exception as e:
        print(f"❌ Startup post error: {e}")
