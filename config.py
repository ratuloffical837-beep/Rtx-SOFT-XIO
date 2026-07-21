import os

# ═══════════════════════════════════════
# RTX Bot - Master Configuration
# Islamic Muslim Assistant Version
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
BKASH_NUMBER    = "01725218874"
NAGAD_NUMBER    = "01725218874"
WHATSAPP_NUMBER = "01344594241"

# ─── Business ───
BUSINESS_NAME   = "RTX"
PROMO_CODE      = "RTX4241"

# ─── Keep Alive ───
RENDER_URL      = os.environ.get("RENDER_URL", "")
PING_INTERVAL   = 120

# ═══════════════════════════════════════
# Group Reply Settings
# ═══════════════════════════════════════
REPLY_KEYWORDS = [
    "price", "প্রাইস", "দাম", "কত",
    "buy", "কিনব", "কিনতে", "কিনি",
    "signal", "সিগনাল",
    "promo", "প্রোমো", "discount", "ছাড়",
    "support", "সাপোর্ট", "সমস্যা", "problem",
    "bot", "বট", "app", "এপ",
    "forex", "crypto", "বিটকয়েন", "bitcoin",
    "payment", "পেমেন্ট", "bkash", "nagad", "বিকাশ", "নগদ",
    "profit", "income", "আয়",
    "hi", "hello", "হাই", "হ্যালো",
    "salam", "সালাম", "আসসালামু",
    "ভাই", "bhai", "help", "হেল্প",
    "কেমন", "আছেন", "আছো",
    "free", "ফ্রি", "trial",
    "refund", "রিফান্ড",
    "access", "একসেস",
    "rtx", "qutex",
]

GROUP_COOLDOWN = 30      # seconds
PRIVATE_COOLDOWN = 5     # seconds

# ═══════════════════════════════════════
# 15-Minute Rotation Schedule
# সকাল ৫টা থেকে রাত ১টা
# প্রতি ১৫ মিনিটে ১টা post
# 
# Rotation Pattern:
#   00 min → motivational/sigma
#   15 min → interactive poll
#   30 min → bot promotion (3 apps)
#   45 min → educational/tips
# ═══════════════════════════════════════

ONLY_CHANNEL = True  # ✅ Double post fix

# Post types rotation (15-min cycle)
POST_ROTATION = [
    "motivational",      # 00 min
    "poll",              # 15 min
    "bot_promo",         # 30 min
    "educational",       # 45 min
]

# Active hours: সকাল ৫টা - রাত ১টা
ACTIVE_HOURS = list(range(5, 24)) + [0, 1]  # 5,6,7...23,0,1
