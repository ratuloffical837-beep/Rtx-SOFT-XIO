import os

# ═══════════════════════════════════════
# RTX Bot - Master Configuration
# ═══════════════════════════════════════

# ─── API Keys ───
BOT_TOKEN       = os.environ.get("BOT_TOKEN", "")
GEMINI_API_KEY  = os.environ.get("GEMINI_API_KEY", "")

# ─── Telegram IDs ───
CHANNEL_ID      = int(os.environ.get("CHANNEL_ID", "-1003214037943"))
GROUP_ID        = int(os.environ.get("GROUP_ID", "-1003680966726"))

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

# ─── Twelvedata API Info ───
TWELVEDATA_SITE       = "twelvedata.com"
TWELVEDATA_TRIAL_KEY  = "abcbdaea55ce4796bb139c1a05e6a344"

# ─── Keep Alive ───
RENDER_URL      = os.environ.get("RENDER_URL", "")
PING_INTERVAL   = 120

# ═══════════════════════════════════════
# Group Reply Settings (Mode B)
# ═══════════════════════════════════════
GROUP_COOLDOWN   = 30
PRIVATE_COOLDOWN = 5

# ═══════════════════════════════════════
# Channel Post Schedule
# সকাল ৮টা - রাত ১১টা
# প্রতি ১৫ মিনিটে ১টা = ৬০ post/day
# ═══════════════════════════════════════
ACTIVE_HOURS  = list(range(8, 23))   # 8, 9, 10 ... 22 (23 না, কারণ 22:45 last)
POST_MINUTES  = [0, 15, 30, 45]
ONLY_CHANNEL  = True   # গ্রুপে কোনো auto post যাবে না
