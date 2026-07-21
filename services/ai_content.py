# ═══════════════════════════════════════
# AI Content Generator
# Islamic Muslim Assistant - Positive Only
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
# শেষ ৩০টা post এর hash রাখা হয়
# ═══════════════════════════════════════
_recent_hashes = deque(maxlen=30)

def _is_duplicate(content: str) -> bool:
    """Check if content is duplicate"""
    h = hashlib.md5(content.encode()).hexdigest()
    if h in _recent_hashes:
        return True
    _recent_hashes.append(h)
    return False


# ═══════════════════════════════════════
# ISLAMIC POSITIVE COMPANY CONTEXT
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

# ═══════════════════════════════════════
# STRICT AI RULES (Islamic + Positive)
# ═══════════════════════════════════════
AI_RULES = """
🕋 STRICT RULES (কখনো ভাঙবে না):

ইসলামিক পার্সোনা:
1. সালাম দাও: "আসসালামু আলাইকুম" বা "ওয়ালাইকুম আসসালাম"
2. বিসমিল্লাহ ব্যবহার করো
3. "ইনশাআল্লাহ" (ভবিষ্যতের বিষয়)
4. "আলহামদুলিল্লাহ" (সফলতা/ধন্যবাদ)
5. "মাশাআল্লাহ" (প্রশংসা)
6. "প্রিয় ভাই" বা "ভাই" সম্বোধন

পজিটিভ টোন (NO NEGATIVE):
❌ কখনো বলবে না: "৯০% লোক লস করে"
❌ কখনো বলবে না: "ট্রেডিং থেকে দূরে থাকুন"
❌ কখনো বলবে না: "ঝুঁকিপূর্ণ, করবেন না"
❌ কখনো বলবে না: "গ্যারান্টি নেই"
✅ বলবে: "সঠিক স্ট্র্যাটেজি ও পাওয়ারফুল AI দিয়ে সহজ ও প্রফিটেবল"
✅ বলবে: "ডিসিপ্লিন ও সঠিক টুলস দিয়ে সফলতা আসবে ইনশাআল্লাহ"
✅ বলবে: "RTX Bot এর সাথে থাকুন, উইনার মাইন্ডসেট গড়ুন"

Sales Focus:
- প্রতিটা reply এ product/link mention করো
- Buy করার জন্য উৎসাহিত করো
- @rtxearn2_bot mention করো
- 5 minute access highlight করো
"""

# ═══════════════════════════════════════
# SMART AI REPLY (User Message Handler)
# ═══════════════════════════════════════

def generate_smart_reply(user_message: str) -> str:
    """Islamic + Positive smart reply for user messages"""
    
    msg_lower = user_message.lower().strip()

    # ─── Greetings + Salam ───
    salam_words = ["salam", "সালাম", "আসসালামু", "assalamu", "assalam"]
    if any(g in msg_lower for g in salam_words):
        return random.choice([
            "ওয়ালাইকুম আসসালাম ওয়া রহমাতুল্লাহ প্রিয় ভাই! 🌸\n"
            "বিসমিল্লাহির রহমানির রহিম।\n\n"
            "কীভাবে সাহায্য করতে পারি? RTX এর ৩টি Powerful Signal Bot আছে ইনশাআল্লাহ! 👇",
            
            "ওয়ালাইকুম আসসালাম প্রিয় ভাই! 🕋\n"
            "আলহামদুলিল্লাহ আপনাকে পেয়ে খুশি হলাম।\n\n"
            "কোন Bot সম্পর্কে জানতে চান? নিচের বাটন দেখুন 👇",
        ])

    # Hi / Hello
    greetings = ["hi", "hello", "হাই", "হ্যালো", "hey"]
    if any(g in msg_lower for g in greetings):
        return random.choice([
            "আসসালামু আলাইকুম প্রিয় ভাই! 🌸\n"
            "বিসমিল্লাহ, RTX Trading Family তে স্বাগতম!\n\n"
            "৩টি Powerful AI Signal Bot আছে ইনশাআল্লাহ 👇",
            
            "আসসালামু আলাইকুম ভাই! 🕋\n"
            "মাশাআল্লাহ, RTX এ আপনাকে পেয়ে খুশি!\n\n"
            "কীভাবে সাহায্য করতে পারি? 👇",
        ])

    # How are you
    how_are = ["কেমন আছেন", "কেমন আছো", "কেমন আছ", "how are you"]
    if any(h in msg_lower for h in how_are):
        return random.choice([
            "আলহামদুলিল্লাহ ভালো আছি প্রিয় ভাই! 🌸\n"
            "আপনি কেমন আছেন?\n\n"
            "RTX Signal নিয়ে কোনো প্রশ্ন থাকলে বলুন 👇",
            
            "আলহামদুলিল্লাহ, মাশাআল্লাহ ভালো আছি ভাই! 😊\n"
            "আপনার জন্য দোয়া রইলো।\n\n"
            "Bot সম্পর্কে জানতে @rtxearn2_bot এ মেসেজ দিন 🙏",
        ])

    # Price
    price_words = ["price", "প্রাইস", "দাম", "কত টাকা", "কত দাম", "খরচ"]
    if any(p in msg_lower for p in price_words):
        return (
            "বিসমিল্লাহ প্রিয় ভাই! 🌸\n\n"
            "💰 RTX Signal Bot Price:\n"
            "🥉 Qutex Signal: 1,000tk (Promo)\n"
            "🥈 Qutex Premium: 2,000tk (Promo)\n"
            "🥇 RTX PRO MAX AI: 5,000tk\n\n"
            "🎁 Promo Code: RTX4241\n"
            "ইনশাআল্লাহ সঠিক Bot দিয়ে সফলতা আসবে 🤲\n\n"
            "বিস্তারিত @rtxearn2_bot এ 👇"
        )

    # Promo
    promo_words = ["promo", "প্রোমো", "discount", "ছাড়", "code", "কোড"]
    if any(p in msg_lower for p in promo_words):
        return (
            "মাশাআল্লাহ প্রিয় ভাই! 🎁\n\n"
            "🔑 Promo Code: RTX4241\n\n"
            "✅ Qutex Signal: 1500→1000tk\n"
            "✅ Qutex Premium: 3000→2000tk\n"
            "⚠️ RTX PRO MAX AI: 5000tk fixed\n\n"
            "এখনই ব্যবহার করুন ইনশাআল্লাহ! 🌸\n"
            "👉 @rtxearn2_bot"
        )

    # Payment
    payment_words = ["bkash", "বিকাশ", "nagad", "নগদ", "payment", "পেমেন্ট", "send money"]
    if any(p in msg_lower for p in payment_words):
        return (
            "বিসমিল্লাহ ভাই! 💳\n\n"
            "📱 bKash: 01725218874 (Send Money)\n"
            "📱 Nagad: 01725218874 (Send Money)\n\n"
            "৫ মিনিটে Access পাবেন ইনশাআল্লাহ! ⚡\n"
            "সমস্যায় @ratulhossain56 এ মেসেজ দিন 🙏"
        )

    # Refund
    if "refund" in msg_lower or "রিফান্ড" in msg_lower:
        return (
            "প্রিয় ভাই! 🌸\n\n"
            "আমাদের Bot গুলো ইনশাআল্লাহ সঠিক signal দেয়!\n"
            "আগে Free signal try করে দেখুন।\n\n"
            "কোনো সমস্যায় @ratulhossain56 সবসময় পাশে আছেন 🤝"
        )

    # Access
    if "কতক্ষণ" in msg_lower or "কত সময়" in msg_lower or "access" in msg_lower:
        return (
            "আলহামদুলিল্লাহ ভাই! ⚡\n\n"
            "Payment এর মাত্র ৫ মিনিটে Access!\n"
            "TrxID submit করলেই দ্রুত approve হবে ইনশাআল্লাহ ✅\n\n"
            "@rtxearn2_bot এ ঢুকে শুরু করুন 🚀"
        )

    # Complaint (respectful handling)
    complaint_words = ["scam", "fake", "ফেক", "কাজ করছে না", "পাইনি"]
    if any(c in msg_lower for c in complaint_words):
        return (
            "প্রিয় ভাই, সমস্যাটা বুঝতে পারছি 🙏\n\n"
            "চিন্তা নেই, আলহামদুলিল্লাহ সমাধান হবে ইনশাআল্লাহ।\n"
            "TrxID সহ @ratulhossain56 এ মেসেজ দিন।\n\n"
            "দ্রুত সাহায্য করা হবে ✅"
        )

    # ─── AI Reply (complex questions) ───
    prompt = f"""
{COMPANY_CONTEXT}

{AI_RULES}

তুমি RTX Trading Bot এর AI Muslim Assistant।
Customer message: "{user_message}"

Instructions:
- সালাম দিয়ে শুরু করো (যদি প্রথম কথা হয়)
- ২-৪ লাইনে ছোট reply দাও
- বাংলায় উত্তর দাও
- Islamic tone + positive tone
- Product/Bot link mention করো
- শেষে "@rtxearn2_bot" mention করো
- ইনশাআল্লাহ/আলহামদুলিল্লাহ ব্যবহার করো
- কোনো নেগেটিভ কথা না
"""

    try:
        if model:
            response = model.generate_content(prompt)
            reply = response.text.strip()
            if len(reply) > 400:
                lines = [l for l in reply.split('\n') if l.strip()]
                reply = '\n'.join(lines[:5])
                if "rtxearn2_bot" not in reply:
                    reply += "\n\n👉 @rtxearn2_bot"
            return reply
    except Exception as e:
        log.warning(f"Gemini reply error: {e}")

    return (
        "আসসালামু আলাইকুম প্রিয় ভাই! 🌸\n"
        "আলহামদুলিল্লাহ, আপনার প্রশ্নের জন্য ধন্যবাদ!\n\n"
        "বিস্তারিত জানতে @rtxearn2_bot এ মেসেজ দিন ইনশাআল্লাহ 🙏"
    )


# ═══════════════════════════════════════
# POST GENERATORS
# ═══════════════════════════════════════

def _gen(prompt: str, fallback_fn):
    """AI generate with duplicate check + fallback"""
    try:
        if model:
            resp = model.generate_content(prompt)
            content = resp.text.strip()
            if content and not _is_duplicate(content):
                return content
    except Exception as e:
        log.warning(f"AI gen error: {e}")
    
    # Fallback (try until non-duplicate)
    for _ in range(5):
        fb = fallback_fn()
        if not _is_duplicate(fb):
            return fb
    return fallback_fn()


# ───────────────────────────────────────
# MOTIVATIONAL / SIGMA POST
# ───────────────────────────────────────

def generate_motivational_post() -> str:
    themes = [
        "সিগমা ট্রেডার মাইন্ডসেট + ধৈর্য + আল্লাহর ওপর ভরসা",
        "সফলতার গল্প: RTX Bot দিয়ে ধৈর্য ধরে সফল হওয়া",
        "ডিসিপ্লিন > মোটিভেশন — রিয়েল ট্রেডার মাইন্ডসেট",
        "ভয়কে জয় করুন, সঠিক টুলস দিয়ে এগিয়ে যান",
        "আজকের সিদ্ধান্তই আগামী দিনের সফলতা",
        "ট্রেডিং একটি হালাল বিজনেস, জুয়া নয়",
        "আল্লাহর ওপর ভরসা + সঠিক Signal = সফলতা",
        "লিডারশিপ: নিজের decision নিজে নিন",
    ]
    theme = random.choice(themes)
    prompt = f"""
{COMPANY_CONTEXT}

{AI_RULES}

Topic: {theme}

Task: Telegram channel এ powerful motivational/sigma post লেখো।

Rules:
- শুরু: "আসসালামু আলাইকুম ওয়া রহমাতুল্লাহ প্রিয় ট্রেডার ভাই! 🌸\nবিসমিল্লাহির রহমানির রহিম।"
- ১২-১৮ লাইন
- Powerful + Positive
- Emoji use করো
- ━━━ separator
- মাঝে ইনশাআল্লাহ/আলহামদুলিল্লাহ
- শেষে RTX Bot recommendation:
   "👉 @rtxearn2_bot" বা bot links
- কোনো নেগেটিভ কথা না
- সিগমা + মুসলিম উইনার মাইন্ডসেট
"""
    return _gen(prompt, _fb_motivational)


def _fb_motivational():
    posts = [
        (
            "━━━━━━━━━━━━━━━━━━━━\n"
            "🌸 আসসালামু আলাইকুম প্রিয় ভাই!\n"
            "━━━━━━━━━━━━━━━━━━━━\n\n"
            "বিসমিল্লাহির রহমানির রহিম 🤲\n\n"
            "🐺 সিগমা ট্রেডার কে হয় জানেন?\n\n"
            "🔥 যে ধৈর্য ধরে waiting করে\n"
            "💰 যে emotion control করে\n"
            "⚡ যে সঠিক Signal follow করে\n"
            "🎯 যে discipline maintain করে\n\n"
            "আল্লাহর ওপর ভরসা + সঠিক টুলস\n"
            "= সফলতা ইনশাআল্লাহ! 🌟\n\n"
            "━━━━━━━━━━━━━━━━━━━━\n"
            "💎 RTX Powerful AI Signal:\n"
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
            "মাশাআল্লাহ, আজ তিনি একজন\n"
            "সফল ট্রেডার! 💪\n\n"
            "🎯 তাঁর সিক্রেট:\n"
            "✅ ডিসিপ্লিন\n"
            "✅ সঠিক টুলস (RTX Bot)\n"
            "✅ আল্লাহর ওপর ভরসা\n"
            "✅ ধৈর্য\n\n"
            "আপনিও পারবেন ইনশাআল্লাহ! 🔥\n\n"
            "━━━━━━━━━━━━━━━━━━━━\n"
            "💎 শুরু করুন আজই:\n"
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
            "🎯 মনে রাখুন:\n\n"
            "ট্রেডিং কোনো জুয়া নয়,\n"
            "এটি একটি নিখাদ বিজনেস। 💼\n\n"
            "ব্যবসায় চাই:\n"
            "✅ ধৈর্য\n"
            "✅ সঠিক টুলস\n"
            "✅ আল্লাহর ওপর ভরসা\n"
            "✅ ডিসিপ্লিন\n\n"
            "মাশাআল্লাহ, RTX AI Signal Bot\n"
            "আপনাকে সব দেবে ইনশাআল্লাহ! 🚀\n\n"
            "━━━━━━━━━━━━━━━━━━━━\n"
            "💎 আমাদের ৩টি Bot:\n"
            "🥉 @qutex4241pro_bot\n"
            "🥈 @qutexperiyam_bot\n"
            "🥇 @rtxpromaxai4241_bot\n\n"
            "🎁 Promo: RTX4241\n"
            "👉 @rtxearn2_bot\n"
            "━━━━━━━━━━━━━━━━━━━━"
        ),
    ]
    return random.choice(posts)


# ───────────────────────────────────────
# BOT PROMOTION POST (Rotates 3 bots)
# ───────────────────────────────────────

# Track which bot to promote next (round robin)
_bot_rotation_index = 0

def generate_bot_promo_post() -> str:
    """৩টা bot rotate করে promotion"""
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
    
    # Try AI first
    prompt = f"""
{COMPANY_CONTEXT}

{AI_RULES}

Task: এই একটি Bot এর জন্য promotional post লেখো:

Bot Info:
- Name: {bot['name']}
- Badge: {bot['badge']}
- Username: {bot['username']}
- App Link: {bot['app']}
- Type: {bot['type']}
- Best for: {bot['for']}
- Price: {bot['price']}
- Promo: {bot['promo'] or 'No promo (fixed price)'}

Rules:
- শুরু: "আসসালামু আলাইকুম প্রিয় ভাই! 🌸\nবিসমিল্লাহির রহমানির রহিম।"
- ১২-১৮ লাইন
- এই একটি Bot ই highlight করো
- Features বলো
- Positive + Sales tone
- Emoji
- ━━━ separator
- Bot username এবং app link দাও
- ইনশাআল্লাহ ব্যবহার করো
- শেষে: "🎯 @rtxearn2_bot এ মেসেজ দিন"
"""
    return _gen(prompt, lambda: _fb_bot_promo(bot))


def _fb_bot_promo(bot):
    promo_line = f"🎁 Promo Code: {bot['promo']}" if bot['promo'] else "⚠️ Fixed Price (No Promo)"
    
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
        f"🎯 Sales: @rtxearn2_bot\n"
        f"👨‍💼 Support: @ratulhossain56\n"
        f"━━━━━━━━━━━━━━━━━━━━"
    )


# ───────────────────────────────────────
# EDUCATIONAL POST
# ───────────────────────────────────────

def generate_educational_post() -> str:
    topics = [
        "সঠিক Signal follow করার নিয়ম",
        "Profit Booking কৌশল",
        "Risk Management এর সহজ পদ্ধতি",
        "Trading Discipline",
        "Mini App কীভাবে ব্যবহার করবেন",
        "৫ মিনিটে Access পাওয়ার সহজ steps",
        "Promo Code apply করার নিয়ম",
        "Candle Pattern বেসিক",
        "Support & Resistance সহজ ভাবে",
        "Entry timing perfect করার tips",
        "Multiple Signal Bot এর সুবিধা",
        "Forex vs Crypto — কোনটা choose করবেন",
        "AI Signal কীভাবে কাজ করে",
        "সঠিক Trade Size determine করা",
    ]
    topic = random.choice(topics)
    prompt = f"""
{COMPANY_CONTEXT}

{AI_RULES}

Topic: {topic}

Task: হালাল বিজনেস guideline hisebe educational post লেখো।

Rules:
- শুরু: "বিসমিল্লাহ প্রিয় ভাই! 🌸"
- ১২-১৬ লাইন
- Practical + Actionable
- Positive tone
- Emoji
- ━━━ separator
- ইনশাআল্লাহ ব্যবহার করো
- শেষে RTX Bot mention:
   "🥉 @qutex4241pro_bot\n🥈 @qutexperiyam_bot\n🥇 @rtxpromaxai4241_bot"
- "🎯 @rtxearn2_bot"
"""
    return _gen(prompt, _fb_educational)


def _fb_educational():
    posts = [
        (
            "━━━━━━━━━━━━━━━━━━━━\n"
            "🌸 বিসমিল্লাহ প্রিয় ভাই!\n"
            "━━━━━━━━━━━━━━━━━━━━\n\n"
            "💡 সঠিক Signal Follow করার নিয়ম:\n\n"
            "✅ Signal আসলে দেরি না করে trade\n"
            "✅ Entry price exactly follow করুন\n"
            "✅ Stop Loss অবশ্যই দিন\n"
            "✅ TP1 এ profit book করুন\n"
            "✅ Emotion control করুন\n"
            "✅ একটা trade এ সব capital না\n\n"
            "মাশাআল্লাহ, এই নিয়ম মানলে\n"
            "ইনশাআল্লাহ সফলতা আসবে! 🚀\n\n"
            "━━━━━━━━━━━━━━━━━━━━\n"
            "💎 Powerful AI Signal Bot:\n"
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
            "📱 Mini App কীভাবে ব্যবহার করবেন:\n\n"
            "1️⃣ Bot username এ click করুন\n"
            "2️⃣ App Open করুন\n"
            "3️⃣ Free Signal try করে দেখুন\n"
            "4️⃣ Buy Premium click করুন\n"
            "5️⃣ Promo Code দিন: RTX4241\n"
            "6️⃣ bKash/Nagad: 01725218874\n"
            "7️⃣ TrxID submit করুন\n"
            "8️⃣ ৫ মিনিটে Access! ⚡\n\n"
            "আলহামদুলিল্লাহ, খুবই সহজ! 🎉\n\n"
            "━━━━━━━━━━━━━━━━━━━━\n"
            "💎 এখনই Try করুন:\n"
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
            "🎁 Promo Code দিয়ে ছাড় নিন!\n\n"
            "🔑 Code: RTX4241\n\n"
            "💰 কীভাবে ব্যবহার করবেন:\n"
            "1️⃣ App এ ঢুকুন\n"
            "2️⃣ Buy Premium click\n"
            "3️⃣ Promo field এ paste করুন\n"
            "4️⃣ Discount apply হবে ✅\n"
            "5️⃣ Payment করুন\n\n"
            "মাশাআল্লাহ, ৫০০-১০০০tk ছাড়! 🎉\n\n"
            "━━━━━━━━━━━━━━━━━━━━\n"
            "🥉 Qutex Signal: 1500→1000tk\n"
            "🥈 Qutex Premium: 3000→2000tk\n"
            "🥇 RTX PRO MAX AI: 5000tk fixed\n\n"
            "🎯 @rtxearn2_bot\n"
            "━━━━━━━━━━━━━━━━━━━━"
        ),
    ]
    return random.choice(posts)


# ═══════════════════════════════════════
# POLL GENERATOR
# ═══════════════════════════════════════

def generate_poll() -> dict:
    """Interactive poll generate করে"""
    polls = [
        {
            "question": "প্রিয় ভাই, আজকের Forex ও Crypto Market এর trend আপনার কাছে কেমন মনে হচ্ছে? 📊",
            "options": [
                "🚀 সম্পূর্ণ Bullish (উপরে যাবে)",
                "📉 Bearish (নিচে নামবে)",
                "⚖️ Sideways (এক জায়গায় ঘোরাঘুরি)",
                "🎯 RTX Signal দেখে trade করবো ইনশাআল্লাহ",
            ],
        },
        {
            "question": "বিসমিল্লাহ বলে বলুন তো — Trading এ emotion control এর সবচেয়ে বড় হাতিয়ার কোনটি? 💡",
            "options": [
                "সঠিক Risk Management ✅",
                "বেশি Trade নেওয়া",
                "বারবার Strategy বদলানো",
                "AI Signal Bot follow করা 🎯",
            ],
        },
        {
            "question": "ইনশাআল্লাহ আজকে আপনি কোন Bot দিয়ে profit করতে চান? 🔥",
            "options": [
                "🥉 Qutex Signal (Forex)",
                "🥈 Qutex Premium (1m/5m)",
                "🥇 RTX PRO MAX AI (Crypto)",
                "সবগুলোই try করবো!",
            ],
        },
        {
            "question": "প্রিয় ভাই, একজন সফল Trader হতে সবচেয়ে জরুরি কী? 🎯",
            "options": [
                "ডিসিপ্লিন ও ধৈর্য 💪",
                "সঠিক AI Tools 🤖",
                "আল্লাহর ওপর ভরসা 🤲",
                "সবগুলোই সমান জরুরি ✅",
            ],
        },
        {
            "question": "মাশাআল্লাহ! আপনি কোন Market এ trade করতে বেশি পছন্দ করেন? 📈",
            "options": [
                "Forex Market 💱",
                "Crypto (Binance) 🪙",
                "দুটোই সমান 🎯",
                "শিখতে চাচ্ছি, guide চাই 📚",
            ],
        },
        {
            "question": "প্রিয় ভাই, RTX এর কোন Feature আপনার সবচেয়ে পছন্দ? ⭐",
            "options": [
                "Real-time AI Signal 🤖",
                "৫ মিনিটে Access ⚡",
                "২৪/২৪ Support 🛡️",
                "Promo Code Discount 🎁",
            ],
        },
        {
            "question": "ইনশাআল্লাহ Trading এ কতদিন ধরে আছেন? 📊",
            "options": [
                "নতুন, শুরু করবো 🌱",
                "কিছু মাস হয়েছে 📈",
                "১+ বছর হয়েছে 💪",
                "Pro Trader ✨",
            ],
        },
        {
            "question": "বিসমিল্লাহ! Signal follow করলে কী কাজ করবেন? 🎯",
            "options": [
                "সাথে সাথে trade নেবো ⚡",
                "চেক করে trade নেবো ✅",
                "SL/TP set করবো 🎯",
                "সবগুলোই করবো 🔥",
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
        "✅ সকাল ৫টা - রাত ১টা\n\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "💎 আমাদের ৩টি Powerful Bot:\n\n"
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
        "🎯 Sales: @rtxearn2_bot\n"
        "👨‍💼 Support: @ratulhossain56\n"
        "📢 Channel: @ratulhossain4241\n\n"
        "ইনশাআল্লাহ সফলতা আসবে! 🚀\n"
        "━━━━━━━━━━━━━━━━━━━━"
        )
