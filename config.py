import os

# ═══════════════════════════════════════
# RTX Marketing Bot Configuration
# ═══════════════════════════════════════

BOT_TOKEN = os.environ.get("BOT_TOKEN")
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

# ═══════════════════════════════════════
# Telegram Links & IDs
# ═══════════════════════════════════════
CHANNEL_ID = -1003214037943      # তোমার Channel ID
GROUP_ID = -1003680966726        # তোমার Group ID (change করো!)
SALES_BOT = "@rtxearn2_bot"
SUPPORT_USERNAME = "@ratulhossain56"

# ═══════════════════════════════════════
# Business Info
# ═══════════════════════════════════════
BUSINESS_NAME = "RTX"
BKASH_NUMBER = "01344594241"
NAGAD_NUMBER = "01344594241"
WHATSAPP_NUMBER = "01344594241"
PROMO_CODE = "RTX4241"

# ═══════════════════════════════════════
# Auto Post Schedule
# প্রতি 1 ঘন্টায় post (24 ঘন্টায় 24টা post)
# ═══════════════════════════════════════
POST_SCHEDULE = [
    # সকাল
    {"hour": 6,  "minute": 0,  "type": "motivational"},
    {"hour": 7,  "minute": 0,  "type": "educational"},
    {"hour": 8,  "minute": 0,  "type": "promotion"},
    {"hour": 9,  "minute": 0,  "type": "signal_tips"},
    {"hour": 10, "minute": 0,  "type": "promotion"},
    {"hour": 11, "minute": 0,  "type": "success_story"},
    
    # দুপুর
    {"hour": 12, "minute": 0,  "type": "offer"},
    {"hour": 13, "minute": 0,  "type": "educational"},
    {"hour": 14, "minute": 0,  "type": "promotion"},
    {"hour": 15, "minute": 0,  "type": "signal_tips"},
    
    # বিকাল
    {"hour": 16, "minute": 0,  "type": "success_story"},
    {"hour": 17, "minute": 0,  "type": "promotion"},
    {"hour": 18, "minute": 0,  "type": "offer"},
    
    # সন্ধ্যা
    {"hour": 19, "minute": 0,  "type": "educational"},
    {"hour": 20, "minute": 0,  "type": "promotion"},
    {"hour": 21, "minute": 0,  "type": "success_story"},
    
    # রাত
    {"hour": 22, "minute": 0,  "type": "signal_tips"},
    {"hour": 23, "minute": 0,  "type": "motivational"},
    
    # গভীর রাত (কম post)
    {"hour": 0,  "minute": 0,  "type": "motivational"},
    {"hour": 1,  "minute": 0,  "type": "educational"},
    {"hour": 2,  "minute": 0,  "type": "signal_tips"},
    {"hour": 3,  "minute": 0,  "type": "promotion"},
    {"hour": 4,  "minute": 0,  "type": "educational"},
    {"hour": 5,  "minute": 0,  "type": "motivational"},
]

# ═══════════════════════════════════════
# Keep Alive
# ═══════════════════════════════════════
RENDER_URL = os.environ.get("RENDER_URL", "")
PING_INTERVAL = 120  # 2 minutes
