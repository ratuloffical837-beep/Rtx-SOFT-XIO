# ═══════════════════════════════════════
# AI Content Generator
# Gemini + Smart Fallback System
# ═══════════════════════════════════════

import google.generativeai as genai
import random
import logging
from config import GEMINI_API_KEY

log = logging.getLogger(__name__)

genai.configure(api_key=GEMINI_API_KEY)

try:
    model = genai.GenerativeModel("gemini-1.5-flash")
except Exception as e:
    log.error(f"Gemini model init failed: {e}")
    model = None

# ═══════════════════════════════════════
# COMPANY CONTEXT (সব prompt এ inject হবে)
# ═══════════════════════════════════════
COMPANY_CONTEXT = """
Company: RTX Trading Signal
Products:
  1. Qutex Signal (@qutex4241pro_bot) — Forex — 1500tk (Promo RTX4241: 1000tk)
     App: https://t.me/qutex4241pro_bot/signalapp
  2. Qutex Premium (@qutexperiyam_bot) — Advanced Forex — 3000tk (Promo RTX4241: 2000tk)
     App: https://t.me/qutexperiyam_bot/qutexsignalbot
  3. RTX PRO MAX AI (@rtxpromaxai4241_bot) — Crypto/Binance — 5000tk (No promo)
     App: https://t.me/rtxpromaxai4241_bot/binancesignalbot
Payment: bKash/Nagad 01725218874
Support: @ratulhossain56
Sales: @rtxearn2_bot
Channel: @ratulhossain4241
Group: @ratulhossain424
Service: ২৪/২৪
No refund | No guaranteed profit | Trading is risky
"""

# ═══════════════════════════════════════
# SMART AI REPLY (User Message Handler)
# ═══════════════════════════════════════

def generate_smart_reply(user_message: str) -> str:
    """
    User এর message এর জন্য smart, short AI reply।
    সর্বোচ্চ ২-৩ লাইন। শেষে CTA।
    Bot কথায় আটকে থাকবে না।
    """

    # ─── Quick keyword match (AI call ছাড়া) ───
    msg_lower = user_message.lower().strip()

    # Greetings
    greetings = ["hi", "hello", "হাই", "হ্যালো", "assalamu", "আসসালামু", "সালাম", "hey"]
    if any(g in msg_lower for g in greetings):
        return random.choice([
            "ওয়ালাইকুম আসসালাম ভাই! 😊 কীভাবে সাহায্য করতে পারি?\n\nবিস্তারিত জানতে নিচের বাটন দেখুন 👇",
            "হ্যালো ভাই! 👋 RTX তে স্বাগতম!\n\nকোনো প্রশ্ন থাকলে জানান, বা নিচের বাটন দেখুন 👇",
            "আছেন কেমন ভাই! 😊\n\nকীভাবে সাহায্য করতে পারি? নিচের বাটন দেখুন 👇",
        ])

    # How are you
    how_are = ["কেমন আছেন", "কেমন আছো", "কেমন আছ", "how are you"]
    if any(h in msg_lower for h in how_are):
        return random.choice([
            "আলহামদুলিল্লাহ ভালো আছি ভাই! 😊 আপনি কেমন আছেন?\n\nকোনো সাহায্য লাগলে @rtxearn2_bot এ মেসেজ দিন 🙏",
            "ভালো আছি ভাই! 🙂 ধন্যবাদ জিজ্ঞেস করার জন্য!\n\nকোনো সাহায্য লাগলে বলুন 👇",
        ])

    # Price inquiry
    price_words = ["price", "প্রাইস", "দাম", "কত টাকা", "কত দাম", "খরচ"]
    if any(p in msg_lower for p in price_words):
        return (
            "💰 আমাদের price:\n"
            "🥉 Qutex Signal: 1,000tk (promo)\n"
            "🥈 Qutex Premium: 2,000tk (promo)\n"
            "🥇 RTX PRO MAX AI: 5,000tk\n\n"
            "🎁 Promo Code: RTX4241\n"
            "বিস্তারিত নিচের বাটন থেকে দেখুন 👇"
        )

    # Promo
    promo_words = ["promo", "প্রোমো", "discount", "ছাড়", "code", "কোড"]
    if any(p in msg_lower for p in promo_words):
        return (
            "🎁 Promo Code: RTX4241\n\n"
            "✅ Qutex Signal: 1500→1000tk\n"
            "✅ Qutex Premium: 3000→2000tk\n"
            "⚠️ RTX PRO MAX AI তে প্রোমো নেই\n\n"
            "কিনতে নিচের বাটন দেখুন 👇"
        )

    # Payment
    payment_words = ["bkash", "বিকাশ", "nagad", "নগদ", "payment", "পেমেন্ট", "send money"]
    if any(p in msg_lower for p in payment_words):
        return (
            "💳 Payment Numbers:\n"
            "📱 bKash: 01725218874 (Send Money)\n"
            "📱 Nagad: 01725218874 (Send Money)\n\n"
            "সমস্যা হলে @ratulhossain56 এ মেসেজ দিন 🙏"
        )

    # Refund
    if "refund" in msg_lower or "রিফান্ড" in msg_lower:
        return (
            "⚠️ দুঃখিত, আমাদের refund policy নেই।\n\n"
            "কেনার আগে free signal try করুন!\n"
            "সমস্যায় @ratulhossain56 এ মেসেজ দিন 🙏"
        )

    # Access time
    if "কতক্ষণ" in msg_lower or "কত সময়" in msg_lower or "access" in msg_lower:
        return (
            "⚡ Payment এর ৫ মিনিটের মধ্যে access!\n\n"
            "TrxID submit করলেই দ্রুত approve হবে ✅\n"
            "সমস্যায় @ratulhossain56 এ মেসেজ দিন 🙏"
        )

    # Scam/fake/complaint
    complaint_words = ["scam", "fake", "ফেক", "প্রতারণা", "কাজ করছে না", "দেয়নি", "পাইনি"]
    if any(c in msg_lower for c in complaint_words):
        return (
            "দুঃখিত ভাই, সমস্যাটা বুঝতে পারছি 🙏\n\n"
            "অনুগ্রহ করে TrxID সহ @ratulhossain56 এ মেসেজ দিন।\n"
            "দ্রুত দেখা হবে ✅"
        )

    # ─── Gemini AI Reply (complex questions) ───
    prompt = f"""
{COMPANY_CONTEXT}

তুমি RTX Trading Bot এর AI assistant।
তোমার কাজ: Customer এর প্রশ্নের ছোট, smart, friendly উত্তর দাও।

STRICT RULES:
1. সর্বোচ্চ ২-৩ লাইনে উত্তর দাও
2. বাংলায় উত্তর দাও
3. Friendly + Professional tone
4. কখনো refund promise করো না
5. কখনো guaranteed profit বলো না
6. শেষে লেখো: "বিস্তারিত জানতে @rtxearn2_bot এ মেসেজ দিন 🙏"
7. ২৪/২৪ বলো, ২৪/৭ না
8. Robot-like না, human-like লেখো
9. কথা ঘোরাবে না

Customer message: "{user_message}"
"""

    try:
        if model:
            response = model.generate_content(prompt)
            reply = response.text.strip()
            # খুব বড় হলে ছোট করো
            if len(reply) > 300:
                lines = [l for l in reply.split('\n') if l.strip()]
                reply = '\n'.join(lines[:4])
                if "rtxearn2_bot" not in reply:
                    reply += "\n\nবিস্তারিত জানতে @rtxearn2_bot এ মেসেজ দিন 🙏"
            return reply
    except Exception as e:
        log.warning(f"Gemini reply error: {e}")

    # ─── Final Fallback ───
    return (
        "ভাই, ধন্যবাদ! 🙏\n\n"
        "বিস্তারিত জানতে @rtxearn2_bot এ মেসেজ দিন।"
    )


# ═══════════════════════════════════════
# POST GENERATORS
# ═══════════════════════════════════════

def _gen(prompt: str, fallback_fn) -> str:
    """AI generate with fallback"""
    try:
        if model:
            resp = model.generate_content(prompt)
            return resp.text.strip()
    except Exception as e:
        log.warning(f"Post gen error: {e}")
    return fallback_fn()


def generate_promotion_post() -> str:
    prompt = f"""
{COMPANY_CONTEXT}

তুমি RTX এর marketing expert।
Telegram channel এর জন্য professional promotional post লেখো।

Rules:
- বাংলায়
- ১৫-২০ লাইন
- প্রচুর emoji
- ━━━ separator
- প্রতিবার আলাদা style/angle
- Bot usernames এবং links দাও
- ২৪/২৪ লেখো
- Catchy headline
- Trading/crypto focused
"""
    return _gen(prompt, _fb_promotion)


def generate_educational_post() -> str:
    topics = [
        "Risk Management", "Stop Loss কেন জরুরি",
        "Money Management", "Trading Psychology",
        "Candle Pattern Basics", "Support & Resistance",
        "RSI Indicator", "MACD Strategy",
        "Trend Following", "Position Sizing",
        "Risk Reward Ratio", "Trading Journal",
        "Fibonacci Retracement", "Order Block কী",
        "Liquidity Sweep", "ICT Concepts",
        "SMC Basics", "Bollinger Band",
        "Moving Average", "Volume Analysis",
        "Crypto Market Cycles", "Dollar ও Crypto সম্পর্ক",
        "Forex vs Crypto", "Entry & Exit Strategy",
        "Scalping vs Swing Trading",
    ]
    topic = random.choice(topics)
    prompt = f"""
{COMPANY_CONTEXT}

Topic: {topic}

Telegram এ educational trading post লেখো।
Rules:
- বাংলায় সহজভাবে
- ১২-১৫ লাইন
- Emoji
- ━━━ separator
- Informative + practical
- শেষে: "Signal পেতে @rtxearn2_bot"
"""
    return _gen(prompt, _fb_educational)


def generate_success_story() -> str:
    prompt = f"""
{COMPANY_CONTEXT}

RTX user এর success story style post লেখো।
Rules:
- বাংলায়
- Realistic (fake over-promise না)
- Profit: ৫০০-৩০০০tk realistic range
- Names: Rahim/Karim/Sohel/Nasir/Milon
- ১০-১৫ লাইন
- Emoji
- ━━━ separator
- শেষে: "@rtxearn2_bot try করুন"
- Trading risky disclaimer ছোট করে
"""
    return _gen(prompt, _fb_success)


def generate_offer_post() -> str:
    prompt = f"""
{COMPANY_CONTEXT}

Promo offer post।
Promo Code: RTX4241
- Qutex Signal: 1500→1000tk
- Qutex Premium: 3000→2000tk
- RTX PRO MAX AI: 5000tk (no promo)

Rules:
- বাংলায়
- Urgency ("সীমিত সময়!", "আজকেই!")
- Eye-catching
- ১২-১৫ লাইন
- ━━━ separator
- Bot links দাও
"""
    return _gen(prompt, _fb_offer)


def generate_motivational_post() -> str:
    prompt = f"""
Trader দের জন্য motivational post।
RTX Trading Signal company।

Rules:
- বাংলায়
- Trading/crypto/money motivation
- Inspirational
- ১০-১২ লাইন
- Emoji
- ━━━ separator
- শেষে: "RTX Family - ২৪/২৪ আপনার পাশে @rtxearn2_bot"
"""
    return _gen(prompt, _fb_motivational)


def generate_signal_tips_post() -> str:
    tips = [
        "Signal follow করার নিয়ম",
        "Entry timing কখন সঠিক",
        "Stop Loss দেওয়ার নিয়ম",
        "TP1 TP2 TP3 কীভাবে নেবেন",
        "Signal miss করলে কী করবেন",
        "একটা signal এ কত invest করবেন",
        "Emotion control করে trade",
        "Signal পেয়ে দেরি করলে কী হয়",
    ]
    tip = random.choice(tips)
    prompt = f"""
{COMPANY_CONTEXT}

Topic: {tip}

Signal tips post।
Rules:
- বাংলায়
- Professional
- Actionable
- ১২-১৫ লাইন
- ━━━ separator
- শেষে bot links
"""
    return _gen(prompt, _fb_signal_tips)


def generate_sigma_post() -> str:
    prompt = f"""
Sigma mindset + trading post।
RTX Trading Signal।

Rules:
- বাংলায়
- Sigma/hustle/grind mentality
- Powerful, dark, inspiring
- "সবাই ঘুমায়, sigma trader profit করে" style
- Emoji: 🐺🔥💰⚡🎯
- ১০-১৫ লাইন
- ━━━ separator
- শেষে: "Sigma Trader হতে @rtxearn2_bot"
"""
    return _gen(prompt, _fb_sigma)


def generate_emotional_post() -> str:
    themes = [
        "প্রথম loss এর পর হার না মানা",
        "পরিবারের জন্য earn করার motivation",
        "Trading শিখে life change",
        "Failure থেকে comeback",
        "স্বপ্ন দেখার সাহস",
    ]
    theme = random.choice(themes)
    prompt = f"""
Theme: {theme}

Emotional + relatable trading post।
বাংলাদেশী young trader দের জন্য।

Rules:
- বাংলায়
- Touching + motivating
- Relatable
- Emoji: 💔🥺😤💪🔥
- ১০-১৫ লাইন
- ━━━ separator
- শেষে: "RTX Family আপনার পাশে ২৪/২৪ @rtxearn2_bot"
"""
    return _gen(prompt, _fb_emotional)


def generate_crypto_update_post() -> str:
    topics = [
        "Bitcoin market trend",
        "Ethereum update",
        "BNB market",
        "Crypto market sentiment",
        "Altcoin season outlook",
        "Dollar ও crypto correlation",
        "Crypto volatility tips",
        "Bull/Bear market strategy",
    ]
    topic = random.choice(topics)
    prompt = f"""
{COMPANY_CONTEXT}

Topic: {topic}

Crypto/Forex market update post।
Rules:
- বাংলায়
- General market update (specific price না)
- Professional analysis tone
- Emoji: 📊📈📉💹
- ১২-১৫ লাইন
- ━━━ separator
- শেষে: "Accurate signal @rtxearn2_bot"
- "⚠️ Trading ঝুঁকিপূর্ণ" disclaimer
"""
    return _gen(prompt, _fb_crypto)


def generate_market_analysis_post() -> str:
    topics = [
        "Trading session (London/NY/Tokyo)",
        "High impact news effect on market",
        "Market cycle analysis",
        "Bull vs Bear strategy",
        "Trend analysis tips",
        "Market opening outlook",
        "Forex major pairs trend",
    ]
    topic = random.choice(topics)
    prompt = f"""
{COMPANY_CONTEXT}

Topic: {topic}

Professional market analysis post।
Rules:
- বাংলায়
- Analyst tone
- Educational + informative
- Emoji
- ১২-১৫ লাইন
- ━━━ separator
- শেষে bot links
- "⚠️ Trading ঝুঁকিপূর্ণ" disclaimer
"""
    return _gen(prompt, _fb_market)


def generate_bot_links_post() -> str:
    """Bot links daily post - সবসময় fixed, consistent"""
    options = [
        (
            "━━━━━━━━━━━━━━━━━━━━\n"
            "🔗 RTX Signal Bot Links\n"
            "━━━━━━━━━━━━━━━━━━━━\n\n"
            "💎 আমাদের ৩টি Signal Bot:\n\n"
            "🥉 Qutex Signal (Forex)\n"
            "   🤖 @qutex4241pro_bot\n"
            "   📱 https://t.me/qutex4241pro_bot/signalapp\n"
            "   💰 1,000tk (Promo: RTX4241)\n\n"
            "🥈 Qutex Premium (Advanced Forex)\n"
            "   🤖 @qutexperiyam_bot\n"
            "   📱 https://t.me/qutexperiyam_bot/qutexsignalbot\n"
            "   💰 2,000tk (Promo: RTX4241)\n\n"
            "🥇 RTX PRO MAX AI (Crypto/Binance)\n"
            "   🤖 @rtxpromaxai4241_bot\n"
            "   📱 https://t.me/rtxpromaxai4241_bot/binancesignalbot\n"
            "   💰 5,000tk\n\n"
            "━━━━━━━━━━━━━━━━━━━━\n"
            "🎁 Promo Code: RTX4241\n"
            "💳 bKash/Nagad: 01725218874\n\n"
            "📢 @ratulhossain4241\n"
            "👥 @ratulhossain424\n"
            "🎯 Sales: @rtxearn2_bot\n"
            "👨‍💼 Support: @ratulhossain56\n\n"
            "✅ ২৪/২৪ Service\n"
            "━━━━━━━━━━━━━━━━━━━━"
        ),
        (
            "━━━━━━━━━━━━━━━━━━━━\n"
            "📱 App Direct Links\n"
            "━━━━━━━━━━━━━━━━━━━━\n\n"
            "⚡ সরাসরি App এ ঢুকুন:\n\n"
            "1️⃣ 🥉 Qutex Signal App\n"
            "   👉 https://t.me/qutex4241pro_bot/signalapp\n\n"
            "2️⃣ 🥈 Qutex Premium App\n"
            "   👉 https://t.me/qutexperiyam_bot/qutexsignalbot\n\n"
            "3️⃣ 🥇 RTX PRO MAX AI App\n"
            "   👉 https://t.me/rtxpromaxai4241_bot/binancesignalbot\n\n"
            "━━━━━━━━━━━━━━━━━━━━\n"
            "🎁 Promo: RTX4241 (Save 500-1000tk!)\n"
            "💳 Payment: bKash/Nagad 01725218874\n\n"
            "🆘 সমস্যা? @ratulhossain56\n"
            "━━━━━━━━━━━━━━━━━━━━"
        ),
    ]
    return random.choice(options)


# ═══════════════════════════════════════
# FALLBACK POSTS
# ═══════════════════════════════════════

def _fb_promotion():
    return random.choice([
        (
            "━━━━━━━━━━━━━━━━━━━━\n"
            "🔥 RTX Trading Signal 🔥\n"
            "━━━━━━━━━━━━━━━━━━━━\n\n"
            "💎 ৩টা Powerful Signal Bot!\n\n"
            "🥉 Qutex Signal - 1,000tk\n"
            "   👉 @qutex4241pro_bot\n"
            "🥈 Qutex Premium - 2,000tk\n"
            "   👉 @qutexperiyam_bot\n"
            "🥇 RTX PRO MAX AI - 5,000tk\n"
            "   👉 @rtxpromaxai4241_bot\n\n"
            "✅ Real-time Data\n"
            "✅ High Accuracy\n"
            "✅ ২৪/২৪ Support\n\n"
            "🎁 Promo: RTX4241\n"
            "🎯 Start: @rtxearn2_bot\n"
            "━━━━━━━━━━━━━━━━━━━━"
        ),
        (
            "━━━━━━━━━━━━━━━━━━━━\n"
            "💰 RTX দিয়ে Earn করুন!\n"
            "━━━━━━━━━━━━━━━━━━━━\n\n"
            "📊 Real Binance/Forex Data\n"
            "🎯 AI Powered Signal\n"
            "⚡ ৫ মিনিটে Access\n"
            "✅ ২৪/২৪ Active\n\n"
            "🥇 RTX PRO MAX AI\n"
            "   @rtxpromaxai4241_bot — 5,000tk\n\n"
            "🥈 Qutex Premium\n"
            "   @qutexperiyam_bot — 2,000tk\n\n"
            "🥉 Qutex Signal\n"
            "   @qutex4241pro_bot — 1,000tk\n\n"
            "🚀 @rtxearn2_bot\n"
            "━━━━━━━━━━━━━━━━━━━━"
        ),
    ])


def _fb_educational():
    return (
        "━━━━━━━━━━━━━━━━━━━━\n"
        "💡 Trading Tips 💡\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"
        "✅ Stop Loss সবসময় দিন\n"
        "✅ Risk Management মেনে চলুন\n"
        "✅ Signal follow করুন\n"
        "✅ Patience রাখুন\n"
        "✅ Emotion control করুন\n"
        "✅ একবারে সব capital না\n\n"
        "⚠️ Trading ঝুঁকিপূর্ণ\n\n"
        "🎯 Signal: @rtxearn2_bot\n"
        "━━━━━━━━━━━━━━━━━━━━"
    )


def _fb_success():
    names = ["Rahim", "Karim", "Sohel", "Nasir", "Milon"]
    profits = ["1,200", "800", "2,500", "1,500", "3,000"]
    name = random.choice(names)
    profit = random.choice(profits)
    return (
        "━━━━━━━━━━━━━━━━━━━━\n"
        "🎉 User Experience\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"
        f"'{name} ভাই RTX PRO MAX AI signal\n"
        f"follow করে এই সপ্তাহে {profit}tk profit করেছেন!'\n\n"
        "📈 তিনি বলেন:\n"
        "Signal গুলো accurate ছিল।\n"
        "Stop Loss follow করেছি।\n"
        "Result ভালো হয়েছে।\n\n"
        "⚠️ Trading ঝুঁকিপূর্ণ।\n"
        "নিজ দায়িত্বে trade করুন।\n\n"
        "👉 @rtxearn2_bot\n"
        "━━━━━━━━━━━━━━━━━━━━"
    )


def _fb_offer():
    return (
        "━━━━━━━━━━━━━━━━━━━━\n"
        "🎁 Special Promo! 🎁\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"
        "🔑 Code: RTX4241\n\n"
        "💰 Qutex Signal:\n"
        "   1,500tk → 1,000tk ✅\n"
        "   @qutex4241pro_bot\n\n"
        "💰 Qutex Premium:\n"
        "   3,000tk → 2,000tk ✅\n"
        "   @qutexperiyam_bot\n\n"
        "⚠️ RTX PRO MAX AI:\n"
        "   5,000tk (প্রোমো নেই)\n"
        "   @rtxpromaxai4241_bot\n\n"
        "⏰ সীমিত সময়!\n"
        "👉 @rtxearn2_bot\n"
        "━━━━━━━━━━━━━━━━━━━━"
    )


def _fb_motivational():
    return (
        "━━━━━━━━━━━━━━━━━━━━\n"
        "🌟 হার মানবো না! 🌟\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"
        "💪 Consistency is key\n"
        "📈 ভুল থেকে শিখুন\n"
        "🎯 Process কে trust করুন\n"
        "🔥 Dream বড় রাখুন\n"
        "⚡ Every loss is a lesson\n\n"
        "RTX Family ২৪/২৪ আপনার পাশে 🤝\n"
        "🎯 @rtxearn2_bot\n"
        "━━━━━━━━━━━━━━━━━━━━"
    )


def _fb_signal_tips():
    return (
        "━━━━━━━━━━━━━━━━━━━━\n"
        "📊 Signal Tips 📊\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"
        "✅ Signal আসলে দেরি না করে trade\n"
        "✅ Entry price exactly follow করুন\n"
        "✅ Stop Loss অবশ্যই দিন\n"
        "✅ TP1 এ profit book করুন\n"
        "✅ Signal miss → skip করুন\n"
        "✅ একটা trade এ সব capital না\n\n"
        "⚠️ Trading ঝুঁকিপূর্ণ\n\n"
        "🥇 @rtxpromaxai4241_bot\n"
        "🎯 @rtxearn2_bot\n"
        "━━━━━━━━━━━━━━━━━━━━"
    )


def _fb_sigma():
    return (
        "━━━━━━━━━━━━━━━━━━━━\n"
        "🐺 Sigma Trader Mindset\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"
        "🔥 যখন সবাই ঘুমায়\n"
        "   Sigma trader chart দেখে 📊\n\n"
        "💰 যখন সবাই complain করে\n"
        "   Sigma trader system follow করে\n\n"
        "⚡ Discipline > Emotion\n"
        "🎯 Consistency > Luck\n"
        "🐺 Process > Result\n\n"
        "Sigma Trader হতে চাইলে:\n"
        "👉 @rtxearn2_bot\n"
        "━━━━━━━━━━━━━━━━━━━━"
    )


def _fb_emotional():
    return (
        "━━━━━━━━━━━━━━━━━━━━\n"
        "💔 Loss হয়েছে?\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"
        "হার মানা মানে\n"
        "স্বপ্ন ছেড়ে দেওয়া 🥺\n\n"
        "💪 প্রতিটা loss একটা lesson\n"
        "📈 প্রতিটা mistake একটা শিক্ষা\n"
        "🔥 থামবো না, শিখবো, জিতবো!\n\n"
        "RTX Family ২৪/২৪ আপনার পাশে 🤝\n"
        "👉 @rtxearn2_bot\n"
        "━━━━━━━━━━━━━━━━━━━━"
    )


def _fb_crypto():
    return (
        "━━━━━━━━━━━━━━━━━━━━\n"
        "📊 Crypto Market Update\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"
        "🔍 Market Sentiment: Volatile\n"
        "📈 BTC: Key level এ আছে\n"
        "📊 ETH: Watch করুন\n"
        "💹 Altcoins: Selective moves\n\n"
        "⚡ Accurate signal এর জন্য:\n"
        "🥇 @rtxpromaxai4241_bot (Crypto)\n"
        "🥉 @qutex4241pro_bot (Forex)\n\n"
        "⚠️ Trading ঝুঁকিপূর্ণ\n"
        "🎯 @rtxearn2_bot\n"
        "━━━━━━━━━━━━━━━━━━━━"
    )


def _fb_market():
    return (
        "━━━━━━━━━━━━━━━━━━━━\n"
        "🔍 Market Analysis\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"
        "📊 আজকের Overview:\n\n"
        "• Forex: Major pairs range-bound\n"
        "• Crypto: Volume increasing\n"
        "• Dollar: Stable zone\n\n"
        "💡 Strategy: Clear signal এর জন্য wait\n"
        "✅ RTX Bot accurate signal দেয়\n\n"
        "⚠️ Trading ঝুঁকিপূর্ণ\n"
        "🎯 @rtxearn2_bot\n"
        "━━━━━━━━━━━━━━━━━━━━"
    )
