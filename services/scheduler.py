# ═══════════════════════════════════════
# Auto Post Scheduler
# নির্দিষ্ট সময়ে Channel + Group এ post
# ═══════════════════════════════════════

import asyncio
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from config import CHANNEL_ID, GROUP_ID, POST_SCHEDULE
from services.ai_content import (
    generate_promotion_post,
    generate_educational_post,
    generate_success_story,
    generate_offer_post,
    generate_motivational_post,
)

scheduler = BackgroundScheduler(timezone="Asia/Dhaka")


def post_to_channel_and_group(bot, post_type):
    """Channel + Group দুই জায়গায় post করে (sync wrapper)"""
    
    # AI দিয়ে content generate
    generators = {
        "promotion": generate_promotion_post,
        "educational": generate_educational_post,
        "success_story": generate_success_story,
        "offer": generate_offer_post,
        "motivational": generate_motivational_post,
    }
    
    content = generators.get(post_type, generate_promotion_post)()
    
    # Async function কে sync context এ চালানোর জন্য
    async def send_posts():
        # Channel এ post
        try:
            await bot.send_message(
                chat_id=CHANNEL_ID,
                text=content,
                disable_web_page_preview=True,
            )
            print(f"✅ Channel post done: {post_type}")
        except Exception as e:
            print(f"❌ Channel post failed: {e}")
        
        # Group এ post
        try:
            await bot.send_message(
                chat_id=GROUP_ID,
                text=content,
                disable_web_page_preview=True,
            )
            print(f"✅ Group post done: {post_type}")
        except Exception as e:
            print(f"❌ Group post failed: {e}")
    
    # New event loop create করে run
    try:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(send_posts())
        loop.close()
    except Exception as e:
        print(f"❌ Scheduler error: {e}")


def setup_scheduler(bot):
    """Scheduler setup করে — scheduled time এ auto post"""
    
    for schedule in POST_SCHEDULE:
        scheduler.add_job(
            post_to_channel_and_group,
            CronTrigger(
                hour=schedule["hour"],
                minute=schedule["minute"],
                timezone="Asia/Dhaka",
            ),
            args=[bot, schedule["type"]],
            id=f"post_{schedule['type']}_{schedule['hour']}",
            replace_existing=True,
        )
        print(
            f"📅 Scheduled: {schedule['type']} at "
            f"{schedule['hour']}:{schedule['minute']:02d}"
        )
    
    scheduler.start()
    print("✅ Scheduler started!")
