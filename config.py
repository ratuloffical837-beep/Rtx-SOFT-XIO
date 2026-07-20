import os

# ═══════════════════════════════════════
# RTX Marketing Bot Configuration
# সব secret keys Render ENV এ থাকবে
# ═══════════════════════════════════════

BOT_TOKEN = os.environ.get("BOT_TOKEN")
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

# ═══════════════════════════════════════
# Telegram Links
# ═══════════════════════════════════════
CHANNEL_ID = "@ratulhossain4241"
GROUP_ID = "@ratulhossain424"
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
# Auto Post Schedule (24-hour format)
# ═══════════════════════════════════════
POST_SCHEDULE = [
    {"hour": 10, "minute": 0, "type": "promotion"},
    {"hour": 14, "minute": 0, "type": "educational"},
    {"hour": 17, "minute": 0, "type": "success_story"},
    {"hour": 20, "minute": 0, "type": "offer"},
    {"hour": 23, "minute": 0, "type": "motivational"},
]

# ═══════════════════════════════════════
# Keep Alive (ping every 2 minutes)
# ═══════════════════════════════════════
RENDER_URL = os.environ.get("RENDER_URL", "")
PING_INTERVAL = 120  # seconds (2 minutes)
