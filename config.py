import os

# ═══════════════════════════════════════
# RTX Bot - Master Configuration
# ═══════════════════════════════════════

# ─── API Keys ───
BOT_TOKEN       = os.environ.get("BOT_TOKEN", "")
GEMINI_API_KEY  = os.environ.get("GEMINI_API_KEY", "")

# ─── Telegram IDs ───
CHANNEL_ID      = -1003214037943
GROUP_ID        = -1003680966726

# ─── Usernames & Contacts ───
SALES_BOT           = "@rtxearn2_bot"
SUPPORT_USERNAME    = "@ratulhossain56"
CHANNEL_USERNAME    = "@ratulhossain4241"
GROUP_USERNAME      = "@ratulhossain424"

# ─── Payment ───
BKASH_NUMBER    = "01344594241"
NAGAD_NUMBER    = "01344594241"
WHATSAPP_NUMBER = "01344594241"

# ─── Business ───
BUSINESS_NAME   = "RTX"
PROMO_CODE      = "RTX4241"

# ─── Keep Alive ───
RENDER_URL      = os.environ.get("RENDER_URL", "")
PING_INTERVAL   = 120  # seconds

# ═══════════════════════════════════════
# Group Reply Settings
# ═══════════════════════════════════════

# Group এ reply দেওয়ার keywords
# এই শব্দগুলো থাকলেই শুধু reply দেবে (group এ)
REPLY_KEYWORDS = [
    "price", "প্রাইস", "দাম", "কত",
    "buy", "কিনব", "কিনতে", "কিনি",
    "signal", "সিগনাল",
    "promo", "প্রোমো", "discount", "ছাড়",
    "support", "সাপোর্ট", "সমস্যা", "problem",
    "bot", "বট", "app", "এপ",
    "forex", "crypto", "বিটকয়েন", "bitcoin",
    "payment", "পেমেন্ট", "bkash", "nagad",
    "profit", "income", "আয়",
    "hi", "hello", "হাই", "হ্যালো",
    "ভাই", "bhai", "help", "হেল্প",
    "কেমন", "আছেন", "আছো",
    "free", "ফ্রি", "trial",
    "refund", "রিফান্ড",
    "access", "একসেস",
]

# Group এ একই user কে কতক্ষণ পর reply (seconds)
GROUP_COOLDOWN = 30

# Private এ cooldown (seconds)
PRIVATE_COOLDOWN = 5

# ═══════════════════════════════════════
# Post Schedule
# সকাল ৫টা - রাত ১টা
# ২০-৩০ মিনিট পর পর
# ONLY_CHANNEL = True মানে শুধু channel এ post
# (channel → group auto-forward থাকলে True করো)
# ═══════════════════════════════════════

ONLY_CHANNEL = True  # ✅ Double post fix

POST_SCHEDULE = [
    # ─── সকাল ৫-৭ ───
    {"hour": 5,  "minute": 0,  "type": "motivational"},
    {"hour": 5,  "minute": 30, "type": "market_analysis"},
    {"hour": 6,  "minute": 0,  "type": "crypto_update"},
    {"hour": 6,  "minute": 30, "type": "signal_tips"},
    {"hour": 7,  "minute": 0,  "type": "educational"},
    {"hour": 7,  "minute": 30, "type": "promotion"},

    # ─── সকাল ৮-১০ ───
    {"hour": 8,  "minute": 0,  "type": "sigma"},
    {"hour": 8,  "minute": 30, "type": "offer"},
    {"hour": 9,  "minute": 0,  "type": "educational"},
    {"hour": 9,  "minute": 30, "type": "promotion"},
    {"hour": 10, "minute": 0,  "type": "crypto_update"},
    {"hour": 10, "minute": 30, "type": "bot_links"},

    # ─── দুপুর ১১-১ ───
    {"hour": 11, "minute": 0,  "type": "market_analysis"},
    {"hour": 11, "minute": 30, "type": "emotional"},
    {"hour": 12, "minute": 0,  "type": "promotion"},
    {"hour": 12, "minute": 30, "type": "signal_tips"},
    {"hour": 13, "minute": 0,  "type": "educational"},
    {"hour": 13, "minute": 30, "type": "success_story"},

    # ─── বিকাল ২-৪ ───
    {"hour": 14, "minute": 0,  "type": "offer"},
    {"hour": 14, "minute": 30, "type": "sigma"},
    {"hour": 15, "minute": 0,  "type": "crypto_update"},
    {"hour": 15, "minute": 30, "type": "promotion"},
    {"hour": 16, "minute": 0,  "type": "bot_links"},
    {"hour": 16, "minute": 30, "type": "motivational"},

    # ─── সন্ধ্যা ৫-৭ ───
    {"hour": 17, "minute": 0,  "type": "market_analysis"},
    {"hour": 17, "minute": 30, "type": "educational"},
    {"hour": 18, "minute": 0,  "type": "promotion"},
    {"hour": 18, "minute": 30, "type": "emotional"},
    {"hour": 19, "minute": 0,  "type": "signal_tips"},
    {"hour": 19, "minute": 30, "type": "offer"},

    # ─── রাত ৮-১০ ───
    {"hour": 20, "minute": 0,  "type": "crypto_update"},
    {"hour": 20, "minute": 30, "type": "sigma"},
    {"hour": 21, "minute": 0,  "type": "promotion"},
    {"hour": 21, "minute": 30, "type": "educational"},
    {"hour": 22, "minute": 0,  "type": "bot_links"},
    {"hour": 22, "minute": 30, "type": "market_analysis"},

    # ─── রাত ১১-১ ───
    {"hour": 23, "minute": 0,  "type": "motivational"},
    {"hour": 23, "minute": 30, "type": "signal_tips"},
    {"hour": 0,  "minute": 0,  "type": "emotional"},
    {"hour": 0,  "minute": 30, "type": "promotion"},
    {"hour": 1,  "minute": 0,  "type": "motivational"},
]
