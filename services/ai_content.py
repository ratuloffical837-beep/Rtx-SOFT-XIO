# ═══════════════════════════════════════
# AI Content Generator - COMPLETE FIXED
# Islamic Muslim Assistant Version
# ═══════════════════════════════════════

import google.generativeai as genai
import random
import logging
import hashlib
from collections import deque
from config import GEMINI_API_KEY

log = logging.getLogger(__name__)

genai.configure(api_key=GEMINI_API_KEY)

try:
    model = genai.GenerativeModel("gemini-1.5-flash")
except Exception as e:
    log.error(f"Gemini init failed: {e}")
    model = None

# ═══════════════════════════════════════
# Duplicate Prevention
# ═══════════════════════════════════════
_recent_hashes = deque(maxlen=30)

def _is_duplicate(content: str) -> bool:
    h = hashlib.md5(content.encode()).hexdigest()
    if h in _recent_hashes:
        return True
    _recent_hashes.append(h)
    return False


# ═══════════════════════════════════════
# COMPANY CONTEXT
# ═══════════════════════════════════════
COMPANY_CONTEXT = """
Company: RTX Trading Signal (হালাল বিজনেস সাপোর্ট)

Products (৩টি Mini App):
  🥉 Qutex Signal (@qutex4241pro_bot) — Forex — নোভিসদের জন্য
     Price: 1500tk (Promo RTX4241: 1000tk)
     App: https://t.me/qutex4241pro_bot/signalapp
     
  🥈 Qutex Premium (@qutexperiyam_bot) — Advanced 1m/5m Forex
     Price: 3000tk (Promo RTX4241: 2000tk)
     App: https://t.me/qutexperiyam_bot/qutexsignalbot
     
  🥇 RTX PRO MAX AI (@rtxpromaxai4241_bot) — Crypto/Binance মাস্টার
     Price: 5000tk (No promo)
     App: https://t.me/rtxpromaxai4241_bot/binancesignalbot

Payment: bKash/Nagad 01725218874
Support: @ratulhossain56
Sales Bot: @rtxearn2_bot
Channel: @ratulhossain4241
Group: @ratulhossain424
Service: ২৪/২৪ সচল
"""

AI_RULES = """
🕋 STRICT RULES:

ইসলামিক পার্সোনা:
- সালাম দাও: "আসসালামু আলাইকুম"
- বিসমিল্লাহ ব্যবহার করো
- "ইনশাআল্লাহ" / "আলহামদুলিল্লাহ" / "মাশাআল্লাহ"
- "প্রিয় ভাই" সম্বোধন

পজিটিভ টোন (NO NEGATIVE):
❌ "৯০% লোক লস করে" বলবে না
❌ "ট্রেডিং থেকে দূরে থাকুন" না
❌ "ঝুঁকিপূর্ণ" না
✅ "সঠিক Strategy + AI দিয়ে সহজ ও প্রফিটেবল"
✅ "ইনশাআল্লাহ সফলতা আসবে"

Sales Focus:
- প্রতিটা reply এ product/link mention
- Buy করার জন্য উৎসাহিত
- @rtxearn2_bot mention
- ৫ মিনিট access highlight
"""


# ═══════════════════════════════════════
# SMART AI REPLY
# ═══════════════════════════════════════

def generate_smart_reply(user_message: str) -> str:
    """Islamic + Positive + Smart reply"""
    
    msg_lower = user_message.lower().strip()

    # Salam
    salam_words = ["salam", "সালাম", "আসসালামু", "assalamu", "assalam"]
    if any(g in msg_lower for g in salam_words):
        return random.choice([
            "ওয়ালাইকুম আসসালাম ওয়া রহমাতুল্লাহ প্রিয় ভাই! 🌸\nকীভাবে সাহায্য করতে পারি?\n\nনিচের বাটন থেকে দেখুন 👇",
            "ওয়ালাইকুম আসসালাম প্রিয় ভাই! 🕋\nআলহামদুলিল্লাহ আপনাকে পেয়ে খুশি!\n\nকোনো প্রশ্ন থাকলে বলুন 👇",
        ])

    # Hi / Hello
    greetings = ["hi", "hello", "হাই", "হ্যালো", "hey"]
    if any(g in msg_lower for g in greetings):
        return random.choice([
            "আসসালামু আলাইকুম প্রিয় ভাই! 🌸\nবিসমিল্লাহ, RTX এ স্বাগতম!\n\nনিচের বাটন থেকে যেকোনো কিছু জানুন 👇",
            "আসসালামু আলাইকুম ভাই! 🕋\nমাশাআল্লাহ, কীভাবে সাহায্য করতে পারি? 👇",
        ])

    # How are you
    how_are = ["কেমন আছেন", "কেমন আছো", "কেমন আছ", "how are you"]
    if any(h in msg_lower for h in how_are):
        return random.choice([
            "আলহামদুলিল্লাহ ভালো আছি প্রিয় ভাই! 😊\nআপনি কেমন আছেন?\n\nনিচের বাটন দেখুন 👇",
            "আলহামদুলিল্লাহ, মাশাআল্লাহ ভালো আছি! 🌸\nআপনার জন্য দোয়া রইলো।\n\nনিচের বাটন থেকে সব জানুন 👇",
        ])

    # Name
    name_words = ["নাম কি", "নাম কী", "তোমার নাম", "your name"]
    if any(n in msg_lower for n in name_words):
        return (
            "আসসালামু আলাইকুম! 🌸\n\n"
            "আমি RTX Trading Assistant! 🤖\n"
            "Trading Signal, Bot Info, Payment Help\n"
            "সবকিছুতে সাহায্য করবো ইনশাআল্লাহ! 🚀\n\n"
            "নিচের বাটন থেকে জানুন 👇"
        )

    # Signal quality
    signal_words = ["সিগনাল কেমন", "signal কেমন", "সিগন্যাল", "accuracy", "কতটুকু সঠিক"]
    if any(s in msg_lower for s in signal_words):
        return (
            "মাশাআল্লাহ প্রিয় ভাই! 🌸\n\n"
            "আমাদের ৩টি Bot Real-time Market Data\n"
            "থেকে AI দিয়ে Signal generate করে! 📊\n\n"
            "🥉 Qutex Signal — Forex\n"
            "🥈 Qutex Premium — 1m/5m Forex\n"
            "🥇 RTX PRO MAX AI — Binance Crypto\n\n"
            "সঠিক Strategy + AI দিয়ে\n"
            "ইনশাআল্লাহ ভালো result পাবেন! 🚀\n\n"
            "আগে Free Signal try করুন 👇"
        )

    # Details
    detail_words = ["বিস্তারিত", "details", "জানতে চাই", "বলো", "explain"]
    if any(d in msg_lower for d in detail_words):
        return (
            "বিসমিল্লাহ প্রিয় ভাই! 🌸\n\n"
            "💎 ৩টি Signal Bot:\n\n"
            "🥉 Qutex Signal — 1,000tk\n"
            "   Forex, নতুনদের জন্য\n"
            "   Free: দৈনিক ৩টি Signal\n\n"
            "🥈 Qutex Premium — 2,000tk\n"
            "   1m/5m Advanced Forex\n"
            "   Free: দৈনিক ৩টি Signal\n\n"
            "🥇 RTX PRO MAX AI — 5,000tk\n"
            "   Binance Crypto, ৫টি Strategy\n"
            "   Free: দৈনিক ২টি Signal\n\n"
            "🎁 Promo: RTX4241\n"
            "💳 bKash/Nagad: 01725218874\n\n"
            "নিচের বাটন দেখুন 👇"
        )

    # Price
    price_words = ["price", "প্রাইস", "দাম", "কত টাকা", "খরচ"]
    if any(p in msg_lower for p in price_words):
        return (
            "বিসমিল্লাহ প্রিয় ভাই! 🌸\n\n"
            "💰 Bot Price:\n"
            "🥉 Qutex Signal: 1,000tk (Promo)\n"
            "🥈 Qutex Premium: 2,000tk (Promo)\n"
            "🥇 RTX PRO MAX AI: 5,000tk\n\n"
            "🎁 Promo: RTX4241\n"
            "💳 bKash/Nagad: 01725218874\n\n"
            "নিচের বাটন থেকে কিনুন 👇"
        )

    # Promo
    promo_words = ["promo", "প্রোমো", "discount", "ছাড়", "code", "কোড"]
    if any(p in msg_lower for p in promo_words):
        return (
            "মাশাআল্লাহ প্রিয় ভাই! 🎁\n\n"
            "🔑 Promo: RTX4241\n\n"
            "✅ Qutex Signal: 1500→1000tk\n"
            "✅ Qutex Premium: 3000→2000tk\n"
            "⚠️ RTX PRO MAX AI: 5000tk (fixed)\n\n"
            "এখনই ব্যবহার করুন ইনশাআল্লাহ! 🌸\n\n"
            "নিচের বাটন দেখুন 👇"
        )

    # Payment
    payment_words = ["bkash", "বিকাশ", "nagad", "নগদ", "payment", "পেমেন্ট"]
    if any(p in msg_lower for p in payment_words):
        return (
            "বিসমিল্লাহ ভাই! 💳\n\n"
            "📱 bKash: 01725218874 (Send Money)\n"
            "📱 Nagad: 01725218874 (Send Money)\n\n"
            "📌 Steps:\n"
            "1️⃣ Send Money করুন\n"
            "2️⃣ TrxID copy করুন\n"
            "3️⃣ App এ paste\n"
            "4️⃣ ৫ মিনিটে Access ইনশাআল্লাহ!\n\n"
            "সমস্যায় @ratulhossain56 🙏"
        )

    # How to buy
    buy_words = ["কিভাবে কিনবো", "কিনব", "কিনতে", "buy", "কেনা"]
    if any(b in msg_lower for b in buy_words):
        return (
            "বিসমিল্লাহ প্রিয় ভাই! 🌸\n\n"
            "📌 কেনার Steps:\n\n"
            "1️⃣ App খুলুন (নিচের বাটন)\n"
            "2️⃣ Free Signal try করুন\n"
            "3️⃣ Buy Premium click\n"
            "4️⃣ Promo: RTX4241\n"
            "5️⃣ bKash: 01725218874\n"
            "6️⃣ TrxID submit\n"
            "7️⃣ ৫ মিনিটে Access! ⚡\n\n"
            "নিচের বাটন থেকে শুরু করুন 👇"
        )

    # How app works
    app_words = ["কিভাবে কাজ", "কেমন কাজ", "how it works", "কিভাবে চলে"]
    if any(a in msg_lower for a in app_words):
        return (
            "মাশাআল্লাহ ভাই! 🌸\n\n"
            "🤖 Bot গুলো Real-time Market Data\n"
            "থেকে AI দিয়ে Signal দেয়!\n\n"
            "📊 Qutex Signal/Premium:\n"
            "→ Generate Signal button\n"
            "→ Next candle UP/DOWN\n\n"
            "🚀 RTX PRO MAX AI:\n"
            "→ ৫টি Strategy Mode\n"
            "→ TP1/TP2/TP3 + SL\n\n"
            "নিচের বাটন থেকে দেখুন 👇"
        )

    # Refund
    if "refund" in msg_lower or "রিফান্ড" in msg_lower:
        return (
            "প্রিয় ভাই! 🌸\n\n"
            "Bot ইনশাআল্লাহ সঠিক Signal দেয়!\n"
            "আগে Free Signal try করুন।\n\n"
            "সমস্যায় @ratulhossain56 🤝"
        )

    # Complaint
    complaint_words = ["scam", "fake", "ফেক", "কাজ করছে না", "পাইনি"]
    if any(c in msg_lower for c in complaint_words):
        return (
            "প্রিয় ভাই, বুঝতে পারছি 🙏\n\n"
            "ইনশাআল্লাহ সমাধান হবে।\n"
            "TrxID সহ @ratulhossain56 এ মেসেজ দিন।\n"
            "দ্রুত সাহায্য পাবেন ✅"
        )

    # Thanks
    thanks_words = ["ধন্যবাদ", "thanks", "thank you", "জাযাকাল্লাহ"]
    if any(t in msg_lower for t in thanks_words):
        return random.choice([
            "জাযাকাল্লাহু খাইরান ভাই! 🌸\nআপনার জন্য দোয়া রইলো।\n\nনিচের বাটন দেখুন 👇",
            "আলহামদুলিল্লাহ! আপনাকেও ধন্যবাদ! 🤲\nRTX Family ২৪/২৪ আপনার পাশে 🌟\n\nনিচের বাটন দেখুন 👇",
        ])

    # Free
    free_words = ["free", "ফ্রি", "trial", "বিনামূল্যে"]
    if any(f in msg_lower for f in free_words):
        return (
            "মাশাআল্লাহ ভাই! Free Signal আছে! 🎉\n\n"
            "🥉 Qutex Signal: দৈনিক ৩টি Free\n"
            "🥈 Qutex Premium: দৈনিক ৩টি Free\n"
            "🥇 RTX PRO MAX AI: দৈনিক ২টি Free\n\n"
            "নিচের বাটন থেকে try করুন! 👇"
        )

    # ─── Gemini AI ───
    prompt = f"""
{COMPANY_CONTEXT}

{AI_RULES}

Customer message: "{user_message}"

Rules:
- ৩-৫ লাইনে উত্তর
- বাংলায়
- Islamic tone
- Product mention
- শেষে: "নিচের বাটন থেকে দেখুন 👇"
"""
    try:
        if model:
            response = model.generate_content(prompt)
            reply = response.text.strip()
            if reply and len(reply) > 10:
                if len(reply) > 400:
                    lines = [l for l in reply.split('\n') if l.strip()]
                    reply = '\n'.join(lines[:6])
                if "বাটন" not in reply and "rtxearn2" not in reply:
                    reply += "\n\nনিচের বাটন থেকে দেখুন 👇"
                return reply
    except Exception as e:
        log.warning(f"Gemini error: {e}")

    # Smart fallback (rotate)
    return random.choice([
        (
            "আসসালামু আলাইকুম প্রিয় ভাই! 🌸\n\n"
            "আমি RTX Trading Assistant! 🤖\n"
            "৩টি Powerful AI Signal Bot:\n\n"
            "🥉 Qutex Signal — 1,000tk\n"
            "🥈 Qutex Premium — 2,000tk\n"
            "🥇 RTX PRO MAX AI — 5,000tk\n\n"
            "🎁 Promo: RTX4241\n"
            "নিচের বাটন দেখুন ইনশাআল্লাহ 👇"
        ),
        (
            "বিসমিল্লাহ প্রিয় ভাই! 🌸\n\n"
            "আপনার প্রশ্নের জন্য ধন্যবাদ!\n\n"
            "💎 Real-time AI Signal!\n"
            "আগে Free Signal try করুন।\n\n"
            "🎁 Promo: RTX4241 (500-1000tk ছাড়!)\n"
            "নিচের বাটন থেকে App খুলুন 👇"
        ),
        (
            "মাশাআল্লাহ ভাই! 🌸\n\n"
            "RTX Family ২৪/২৪ পাশে! 🤝\n\n"
            "📱 Apps:\n"
            "🥉 @qutex4241pro_bot\n"
            "🥈 @qutexperiyam_bot\n"
            "🥇 @rtxpromaxai4241_bot\n\n"
            "💳 bKash/Nagad: 01725218874\n\n"
            "নিচের বাটন দেখুন 👇"
        ),
    ])


# ═══════════════════════════════════════
# POST HELPER
# ═══════════════════════════════════════

def _gen(prompt: str, fallback_fn):
    try:
        if model:
            resp = model.generate_content(prompt)
            content = resp.text.strip()
            if content and not _is_duplicate(content):
                return content
    except Exception as e:
        log.warning(f"AI gen error: {e}")
    
    for _ in range(5):
        fb = fallback_fn()
        if not _is_duplicate(fb):
            return fb
    return fallback_fn()


# ═══════════════════════════════════════
# MOTIVATIONAL POST
# ═══════════════════════════════════════

def generate_motivational_post() -> str:
    themes = [
        "সিগমা ট্রেডার মাইন্ডসেট + ধৈর্য",
        "সফলতার গল্প: RTX Bot দিয়ে ধৈর্য ধরে সফল",
        "ডিসিপ্লিন > মোটিভেশন",
        "ভয়কে জয় করুন, সঠিক টুলস দিয়ে এগিয়ে যান",
        "আজকের সিদ্ধান্ত = আগামীর সফলতা",
        "ট্রেডিং হালাল বিজনেস",
        "আল্লাহর ওপর ভরসা + সঠিক Signal",
        "নিজের decision নিজে নিন",
    ]
    theme = random.choice(themes)
    prompt = f"""
{COMPANY_CONTEXT}

{AI_RULES}

Topic: {theme}

Task: Motivational/Sigma post লেখো।

Rules:
- শুরু: "আসসালামু আলাইকুম প্রিয় ট্রেডার ভাই! 🌸\nবিসমিল্লাহির রহমানির রহিম।"
- ১২-১৮ লাইন
- Powerful + Positive
- Emoji
- ━━━ separator
- ইনশাআল্লাহ/আলহামদুলিল্লাহ
- শেষে: bot links + @rtxearn2_bot
- কোনো নেগেটিভ কথা না
"""
    return _gen(prompt, _fb_motivational)


def _fb_motivational():
    return random.choice([
        (
            "━━━━━━━━━━━━━━━━━━━━\n"
            "🌸 আসসালামু আলাইকুম প্রিয় ভাই!\n"
            "━━━━━━━━━━━━━━━━━━━━\n\n"
            "বিসমিল্লাহির রহমানির রহিম 🤲\n\n"
            "🐺 সিগমা ট্রেডার কে?\n\n"
            "🔥 যে ধৈর্য ধরে waiting করে\n"
            "💰 যে emotion control করে\n"
            "⚡ যে সঠিক Signal follow করে\n"
            "🎯 যে discipline maintain করে\n\n"
            "আল্লাহর ভরসা + সঠিক টুলস\n"
            "= সফলতা ইনশাআল্লাহ! 🌟\n\n"
            "━━━━━━━━━━━━━━━━━━━━\n"
            "💎 RTX AI Signal:\n"
            "🥉 @qutex4241pro_bot\n"
            "🥈 @qutexperiyam_bot\n"
            "🥇 @rtxpromaxai4241_bot\n\n"
            "🎁 Promo: RTX4241\n"
            "👉 @rtxearn2_bot\n"
            "━━━━━━━━━━━━━━━━━━━━"
        ),
        (
            "━━━━━━━━━━━━━━━━━━━━\n"
            "🌸 সফলতার গল্প — আলহামদুলিল্লাহ\n"
            "━━━━━━━━━━━━━━━━━━━━\n\n"
            "বিসমিল্লাহ প্রিয় ভাই! 🕋\n\n"
            "একজন সাধারণ ভাই ধৈর্য ধরে\n"
            "RTX Bot এর AI Signal follow করেছেন।\n\n"
            "মাশাআল্লাহ, আজ তিনি সফল ট্রেডার! 💪\n\n"
            "🎯 সিক্রেট:\n"
            "✅ ডিসিপ্লিন\n"
            "✅ সঠিক টুলস (RTX Bot)\n"
            "✅ আল্লাহর ভরসা\n"
            "✅ ধৈর্য\n\n"
            "আপনিও পারবেন ইনশাআল্লাহ! 🔥\n\n"
            "━━━━━━━━━━━━━━━━━━━━\n"
            "🥉 @qutex4241pro_bot (Forex)\n"
            "🥈 @qutexperiyam_bot (1m/5m)\n"
            "🥇 @rtxpromaxai4241_bot (Crypto)\n\n"
            "🎯 @rtxearn2_bot\n"
            "━━━━━━━━━━━━━━━━━━━━"
        ),
        (
            "━━━━━━━━━━━━━━━━━━━━\n"
            "🌸 ট্রেডিং = হালাল বিজনেস\n"
            "━━━━━━━━━━━━━━━━━━━━\n\n"
            "আসসালামু আলাইকুম ভাই! 🕋\n"
            "বিসমিল্লাহির রহমানির রহিম।\n\n"
            "🎯 ট্রেডিং জুয়া নয়,\n"
            "এটি নিখাদ বিজনেস। 💼\n\n"
            "ব্যবসায় চাই:\n"
            "✅ ধৈর্য\n"
            "✅ সঠিক টুলস\n"
            "✅ আল্লাহর ভরসা\n"
            "✅ ডিসিপ্লিন\n\n"
            "মাশাআল্লাহ RTX AI সব দেবে! 🚀\n\n"
            "━━━━━━━━━━━━━━━━━━━━\n"
            "🥉 @qutex4241pro_bot\n"
            "🥈 @qutexperiyam_bot\n"
            "🥇 @rtxpromaxai4241_bot\n\n"
            "🎁 Promo: RTX4241\n"
            "👉 @rtxearn2_bot\n"
            "━━━━━━━━━━━━━━━━━━━━"
        ),
    ])


# ═══════════════════════════════════════
# BOT PROMOTION POST (Rotates 3 bots)
# ═══════════════════════════════════════

_bot_rotation_index = 0

def generate_bot_promo_post() -> str:
    global _bot_rotation_index
    
    bots = [
        {
            "badge": "🥉",
            "name": "Qutex Signal",
            "username": "@qutex4241pro_bot",
            "app": "https://t.me/qutex4241pro_bot/signalapp",
            "type": "Forex Signal",
            "for": "নোভিস/নতুন ট্রেডার",
            "price": "1,500tk → 1,000tk",
            "promo": "RTX4241",
        },
        {
            "badge": "🥈",
            "name": "Qutex Premium",
            "username": "@qutexperiyam_bot",
            "app": "https://t.me/qutexperiyam_bot/qutexsignalbot",
            "type": "Advanced 1m & 5m Forex",
            "for": "এডভান্সড ট্রেডার",
            "price": "3,000tk → 2,000tk",
            "promo": "RTX4241",
        },
        {
            "badge": "🥇",
            "name": "RTX PRO MAX AI",
            "username": "@rtxpromaxai4241_bot",
            "app": "https://t.me/rtxpromaxai4241_bot/binancesignalbot",
            "type": "Binance Crypto Master",
            "for": "ক্রিপ্টো মাস্টার",
            "price": "5,000tk (Fixed)",
            "promo": None,
        },
    ]
    
    bot = bots[_bot_rotation_index % 3]
    _bot_rotation_index += 1
    
    prompt = f"""
{COMPANY_CONTEXT}

{AI_RULES}

Task: এই একটি Bot এর promotional post:

Bot: {bot['name']}
Badge: {bot['badge']}
Username: {bot['username']}
App: {bot['app']}
Type: {bot['type']}
For: {bot['for']}
Price: {bot['price']}
Promo: {bot['promo'] or 'No promo'}

Rules:
- শুরু: "আসসালামু আলাইকুম প্রিয় ভাই! 🌸\nবিসমিল্লাহির রহমানির রহিম।"
- ১২-১৮ লাইন
- এই একটি Bot ই highlight
- Features বলো
- Positive + Sales
- Emoji + ━━━
- Bot username + app link
- ইনশাআল্লাহ
- শেষে: "🎯 @rtxearn2_bot"
"""
    return _gen(prompt, lambda: _fb_bot_promo(bot))


def _fb_bot_promo(bot):
    promo_line = f"🎁 Promo: {bot['promo']}" if bot['promo'] else "⚠️ Fixed Price"
    
    return (
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"🌸 আসসালামু আলাইকুম ভাই!\n"
        f"━━━━━━━━━━━━━━━━━━━━\n\n"
        f"বিসমিল্লাহির রহমানির রহিম 🤲\n\n"
        f"{bot['badge']} {bot['name']}\n"
        f"━━━━━━━━━━━━━━━━━━━━\n\n"
        f"📊 Type: {bot['type']}\n"
        f"⭐ Best for: {bot['for']}\n"
        f"💰 Price: {bot['price']}\n"
        f"{promo_line}\n\n"
        f"✅ Real-time Market Data\n"
        f"✅ Powerful AI Signal\n"
        f"✅ ৫ মিনিটে Access\n"
        f"✅ ২৪/২৪ Support\n\n"
        f"ইনশাআল্লাহ সফলতা আসবে! 🚀\n\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"🤖 Bot: {bot['username']}\n"
        f"📱 App: {bot['app']}\n\n"
        f"🎯 @rtxearn2_bot\n"
        f"👨‍💼 @ratulhossain56\n"
        f"━━━━━━━━━━━━━━━━━━━━"
    )


# ═══════════════════════════════════════
# EDUCATIONAL POST
# ═══════════════════════════════════════

def generate_educational_post() -> str:
    topics = [
        "সঠিক Signal follow করার নিয়ম",
        "Profit Booking কৌশল",
        "Risk Management সহজ পদ্ধতি",
        "Trading Discipline",
        "Mini App কীভাবে ব্যবহার করবেন",
        "৫ মিনিটে Access পাওয়ার steps",
        "Promo Code apply করার নিয়ম",
        "Candle Pattern বেসিক",
        "Support & Resistance",
        "Entry timing perfect করা",
        "Multiple Signal Bot সুবিধা",
        "Forex vs Crypto কোনটা",
        "AI Signal কীভাবে কাজ করে",
        "সঠিক Trade Size determine",
    ]
    topic = random.choice(topics)
    prompt = f"""
{COMPANY_CONTEXT}

{AI_RULES}

Topic: {topic}

Task: হালাল guideline hisebe educational post।

Rules:
- শুরু: "বিসমিল্লাহ প্রিয় ভাই! 🌸"
- ১২-১৬ লাইন
- Practical + Actionable
- Positive
- Emoji + ━━━
- ইনশাআল্লাহ
- শেষে bot links + @rtxearn2_bot
"""
    return _gen(prompt, _fb_educational)


def _fb_educational():
    return random.choice([
        (
            "━━━━━━━━━━━━━━━━━━━━\n"
            "🌸 বিসমিল্লাহ প্রিয় ভাই!\n"
            "━━━━━━━━━━━━━━━━━━━━\n\n"
            "💡 সঠিক Signal Follow করার নিয়ম:\n\n"
            "✅ Signal আসলে দেরি না করে trade\n"
            "✅ Entry price exactly follow\n"
            "✅ Stop Loss অবশ্যই দিন\n"
            "✅ TP1 এ profit book\n"
            "✅ Emotion control\n"
            "✅ একটা trade এ সব capital না\n\n"
            "মাশাআল্লাহ, এই নিয়ম মানলে\n"
            "ইনশাআল্লাহ সফলতা আসবে! 🚀\n\n"
            "━━━━━━━━━━━━━━━━━━━━\n"
            "💎 RTX AI Signal:\n"
            "🥉 @qutex4241pro_bot\n"
            "🥈 @qutexperiyam_bot\n"
            "🥇 @rtxpromaxai4241_bot\n\n"
            "🎯 @rtxearn2_bot\n"
            "━━━━━━━━━━━━━━━━━━━━"
        ),
        (
            "━━━━━━━━━━━━━━━━━━━━\n"
            "🌸 বিসমিল্লাহ প্রিয় ভাই!\n"
            "━━━━━━━━━━━━━━━━━━━━\n\n"
            "📱 Mini App কীভাবে ব্যবহার:\n\n"
            "1️⃣ Bot username এ click\n"
            "2️⃣ App Open করুন\n"
            "3️⃣ Free Signal try করুন\n"
            "4️⃣ Buy Premium click\n"
            "5️⃣ Promo: RTX4241\n"
            "6️⃣ bKash/Nagad: 01725218874\n"
            "7️⃣ TrxID submit\n"
            "8️⃣ ৫ মিনিটে Access! ⚡\n\n"
            "আলহামদুলিল্লাহ, খুবই সহজ! 🎉\n\n"
            "━━━━━━━━━━━━━━━━━━━━\n"
            "🥉 @qutex4241pro_bot\n"
            "🥈 @qutexperiyam_bot\n"
            "🥇 @rtxpromaxai4241_bot\n\n"
            "🎯 @rtxearn2_bot\n"
            "━━━━━━━━━━━━━━━━━━━━"
        ),
        (
            "━━━━━━━━━━━━━━━━━━━━\n"
            "🌸 বিসমিল্লাহ ভাই!\n"
            "━━━━━━━━━━━━━━━━━━━━\n\n"
            "🎁 Promo Code দিয়ে ছাড়!\n\n"
            "🔑 Code: RTX4241\n\n"
            "💰 কীভাবে ব্যবহার:\n"
            "1️⃣ App এ ঢুকুন\n"
            "2️⃣ Buy Premium click\n"
            "3️⃣ Promo field এ paste\n"
            "4️⃣ Discount apply ✅\n"
            "5️⃣ Payment করুন\n\n"
            "মাশাআল্লাহ, ৫০০-১০০০tk ছাড়! 🎉\n\n"
            "━━━━━━━━━━━━━━━━━━━━\n"
            "🥉 Qutex Signal: 1500→1000tk\n"
            "🥈 Qutex Premium: 3000→2000tk\n"
            "🥇 RTX PRO MAX AI: 5000tk\n\n"
            "🎯 @rtxearn2_bot\n"
            "━━━━━━━━━━━━━━━━━━━━"
        ),
    ])


# ═══════════════════════════════════════
# POLL GENERATOR
# ═══════════════════════════════════════

def generate_poll() -> dict:
    polls = [
        {
            "question": "প্রিয় ভাই, আজকের Market trend কেমন মনে হচ্ছে? 📊",
            "options": [
                "🚀 Bullish (উপরে যাবে)",
                "📉 Bearish (নিচে নামবে)",
                "⚖️ Sideways",
                "🎯 RTX Signal দেখে trade করবো",
            ],
        },
        {
            "question": "Trading এ emotion control এর সবচেয়ে বড় হাতিয়ার? 💡",
            "options": [
                "সঠিক Risk Management ✅",
                "বেশি Trade নেওয়া",
                "Strategy বদলানো",
                "AI Signal follow করা 🎯",
            ],
        },
        {
            "question": "ইনশাআল্লাহ আজকে কোন Bot দিয়ে profit? 🔥",
            "options": [
                "🥉 Qutex Signal (Forex)",
                "🥈 Qutex Premium (1m/5m)",
                "🥇 RTX PRO MAX AI (Crypto)",
                "সবগুলোই try করবো!",
            ],
        },
        {
            "question": "সফল Trader হতে সবচেয়ে জরুরি? 🎯",
            "options": [
                "ডিসিপ্লিন ও ধৈর্য 💪",
                "সঠিক AI Tools 🤖",
                "আল্লাহর ভরসা 🤲",
                "সবগুলোই সমান জরুরি ✅",
            ],
        },
        {
            "question": "কোন Market পছন্দ? 📈",
            "options": [
                "Forex 💱",
                "Crypto (Binance) 🪙",
                "দুটোই 🎯",
                "শিখতে চাই 📚",
            ],
        },
        {
            "question": "RTX এর কোন Feature পছন্দ? ⭐",
            "options": [
                "Real-time AI Signal 🤖",
                "৫ মিনিটে Access ⚡",
                "২৪/২৪ Support 🛡️",
                "Promo Discount 🎁",
            ],
        },
        {
            "question": "Trading এ কতদিন? 📊",
            "options": [
                "নতুন, শুরু করবো 🌱",
                "কিছু মাস 📈",
                "১+ বছর 💪",
                "Pro Trader ✨",
            ],
        },
        {
            "question": "Signal follow করলে কী করবেন? 🎯",
            "options": [
                "সাথে সাথে trade ⚡",
                "চেক করে trade ✅",
                "SL/TP set করবো 🎯",
                "সবগুলোই 🔥",
            ],
        },
    ]
    return random.choice(polls)


# ═══════════════════════════════════════
# STARTUP POST
# ═══════════════════════════════════════

def get_startup_post() -> str:
    return (
        "━━━━━━━━━━━━━━━━━━━━\n"
        "🌸 আসসালামু আলাইকুম প্রিয় ভাই!\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"
        "বিসমিল্লাহির রহমানির রহিম 🤲\n\n"
        "🚀 RTX Bot Active! (২৪/২৪)\n\n"
        "✅ AI Signal সচল\n"
        "✅ Auto Post প্রতি ১৫ মিনিটে\n"
        "✅ Interactive Polls\n"
        "✅ সকাল ৫টা - রাত ১২টা\n\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "💎 আমাদের ৩টি Bot:\n\n"
        "🥉 Qutex Signal (Forex)\n"
        "   🤖 @qutex4241pro_bot\n"
        "   💰 1,000tk (Promo: RTX4241)\n\n"
        "🥈 Qutex Premium (1m/5m)\n"
        "   🤖 @qutexperiyam_bot\n"
        "   💰 2,000tk (Promo: RTX4241)\n\n"
        "🥇 RTX PRO MAX AI (Crypto)\n"
        "   🤖 @rtxpromaxai4241_bot\n"
        "   💰 5,000tk\n\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "🎁 Promo: RTX4241\n"
        "💳 bKash/Nagad: 01725218874\n\n"
        "🎯 @rtxearn2_bot\n"
        "👨‍💼 @ratulhossain56\n"
        "📢 @ratulhossain4241\n\n"
        "ইনশাআল্লাহ সফলতা আসবে! 🚀\n"
        "━━━━━━━━━━━━━━━━━━━━"
    )
