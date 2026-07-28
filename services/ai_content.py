# ═══════════════════════════════════════
# Smart Reply Generator (Gemini + Fallback)
# শুধু group/private reply এর জন্য
# Channel post এ ব্যবহার হয় না
# ═══════════════════════════════════════

import logging
import random
from config import GEMINI_API_KEY

log = logging.getLogger(__name__)

# ─── Gemini Setup (Optional) ───
model = None
try:
    import google.generativeai as genai
    if GEMINI_API_KEY:
        genai.configure(api_key=GEMINI_API_KEY)
        model = genai.GenerativeModel("gemini-1.5-flash")
        log.info("✅ Gemini AI initialized")
    else:
        log.warning("⚠️ GEMINI_API_KEY missing — using fallback only")
except Exception as e:
    log.error(f"❌ Gemini init failed: {e}")
    model = None


# ═══════════════════════════════════════
# Context for Gemini
# ═══════════════════════════════════════

COMPANY_CONTEXT = """
Company: RTX Trading Signal (Bangladesh)

Products (৪টি Trading Bot):

📈 Binary Trading — Qutex Signal (@qutex4241pro_bot)
   Price: 1500tk (Promo RTX4241: 1000tk)
   Timeframe: 1M | Free: 3/day
   
💎 Binary Premium — Qutex Premium (@qutexperiyam_bot)
   Price: 3000tk (Promo RTX4241: 2000tk)
   Timeframe: 1M + 5M | Free: 3/day
   
💹 Forex Trading — RTX EXNESS (@rtxexness_bot)
   Price: 8000tk (Fixed, No promo)
   Timeframe: 15M | Free: 5/day
   
🪙 Crypto Trading — RTX PRO MAX AI (@rtxpromaxai4241_bot)
   Price: 5000tk (Fixed, No promo)
   Binance based | Free: 2/day
   ⭐ API Key লাগে না!

API Key: Binary + Forex এ Twelvedata API লাগে
- twelvedata.com → Google Login → Free key
- 800 calls/day free
- প্রতিজনের আলাদা key

Payment: bKash/Nagad 01725218874
Support: @ratulhossain56
Sales Bot: @rtxearn2_bot
Channel: @ratulhossain4241
Group: @ratulhossain424
Promo: RTX4241
"""


# ═══════════════════════════════════════
# Fixed Smart Replies (Priority Match)
# ═══════════════════════════════════════

def generate_smart_reply(user_message: str) -> str:
    """Islamic + Smart + Sales-focused reply"""
    
    msg_lower = user_message.lower().strip()

    # ─── Salam ───
    if any(g in msg_lower for g in ["salam", "সালাম", "আসসালামু", "assalamu", "assalam"]):
        return random.choice([
            "ওয়ালাইকুম আসসালাম ওয়া রহমাতুল্লাহ প্রিয় ভাই! 🌸\n"
            "কীভাবে সাহায্য করতে পারি?\n\n"
            "নিচের বাটন থেকে দেখুন 👇",
            
            "ওয়ালাইকুম আসসালাম প্রিয় ভাই! 🕋\n"
            "আলহামদুলিল্লাহ আপনাকে পেয়ে খুশি!\n\n"
            "৪টি Trading Bot আছে আমাদের।\n"
            "নিচে থেকে দেখুন 👇",
        ])

    # ─── Greeting ───
    if any(g in msg_lower for g in ["hi", "hello", "হাই", "হ্যালো", "hey"]):
        return (
            "আসসালামু আলাইকুম প্রিয় ভাই! 🌸\n"
            "বিসমিল্লাহ, RTX এ স্বাগতম!\n\n"
            "কোন Trading এ interested?\n"
            "নিচের বাটন থেকে দেখুন 👇"
        )

    # ─── How are you ───
    if any(h in msg_lower for h in ["কেমন আছেন", "কেমন আছো", "কেমন আছ", "how are you"]):
        return (
            "আলহামদুলিল্লাহ ভালো আছি প্রিয় ভাই! 😊\n"
            "আপনি কেমন আছেন?\n\n"
            "কীভাবে সাহায্য করতে পারি?\n"
            "নিচের বাটন দেখুন 👇"
        )

    # ─── API Key ───
    if any(a in msg_lower for a in ["api", "এপিআই", "twelvedata", "টুয়েলভ", "key", "কী"]):
        return (
            "🔑 Twelvedata API Key Info! 🌸\n\n"
            "📌 কোথায় লাগে?\n"
            "✅ Binary Trading\n"
            "✅ Binary Premium\n"
            "✅ Forex Trading\n"
            "❌ Crypto তে লাগে না\n\n"
            "📝 কীভাবে পাবেন?\n"
            "1️⃣ twelvedata.com এ যান\n"
            "2️⃣ Google/Gmail দিয়ে Sign Up\n"
            "3️⃣ API Key copy করুন\n"
            "4️⃣ App Setting এ paste\n\n"
            "🎁 Free: 800 calls/day\n"
            "⚠️ প্রতিজনের আলাদা key!\n\n"
            "বিস্তারিত FAQ তে 👇"
        )

    # ─── Price ───
    if any(p in msg_lower for p in ["price", "প্রাইস", "দাম", "কত টাকা", "মূল্য"]):
        return (
            "💰 RTX Price List:\n\n"
            "📈 Binary Trading: 1,000tk (Promo)\n"
            "💎 Binary Premium: 2,000tk (Promo)\n"
            "💹 Forex Trading: 8,000tk (Fixed)\n"
            "🪙 Crypto Trading: 5,000tk (Fixed)\n\n"
            "🎁 Promo: RTX4241\n"
            "💳 bKash/Nagad: 01725218874\n\n"
            "বিস্তারিত নিচে দেখুন 👇"
        )

    # ─── Promo ───
    if any(p in msg_lower for p in ["promo", "প্রোমো", "discount", "ছাড়", "code", "কোড"]):
        return (
            "🎁 Promo Code: RTX4241 🌸\n\n"
            "✅ কাজ করে:\n"
            "• Binary: 1500 → 1000tk\n"
            "• Premium: 3000 → 2000tk\n\n"
            "❌ কাজ করে না:\n"
            "• Forex (8000tk fixed)\n"
            "• Crypto (5000tk fixed)\n\n"
            "নিচের বাটন দেখুন 👇"
        )

    # ─── Payment ───
    if any(p in msg_lower for p in ["bkash", "বিকাশ", "nagad", "নগদ", "payment", "পেমেন্ট"]):
        return (
            "💳 Payment Guide! 🌸\n\n"
            "📱 bKash: 01725218874 (Send Money)\n"
            "📱 Nagad: 01725218874 (Send Money)\n\n"
            "📌 Steps:\n"
            "1️⃣ Send Money করুন\n"
            "2️⃣ TrxID copy করুন\n"
            "3️⃣ App এ paste করুন\n"
            "4️⃣ ৫ মিনিটে Access!\n\n"
            "সমস্যায়: @ratulhossain56"
        )

    # ─── Free ───
    if any(f in msg_lower for f in ["free", "ফ্রি", "trial", "বিনামূল্যে", "ডেমো"]):
        return (
            "🎁 Free Signal! 🌸\n\n"
            "📈 Binary: দৈনিক ৩টি free\n"
            "💎 Premium: দৈনিক ৩টি free\n"
            "💹 Forex: দৈনিক ৫টি free\n"
            "🪙 Crypto: দৈনিক ২টি free\n\n"
            "মোট ১৩টি Free Signal/day! 🚀\n"
            "নিচের বাটন থেকে try করুন 👇"
        )

    # ─── Crypto ───
    if any(c in msg_lower for c in ["crypto", "ক্রিপ্টো", "bitcoin", "binance", "বাইনান্স"]):
        return (
            "🪙 RTX PRO MAX AI (Crypto)! 🌸\n\n"
            "✅ Binance Spot + Future\n"
            "✅ ৫টি Advanced Strategy\n"
            "✅ TP1/TP2/TP3 + SL\n"
            "✅ API Key লাগে না!\n\n"
            "💰 5,000tk (Fixed)\n"
            "🤖 @rtxpromaxai4241_bot\n"
            "🎁 Free: ২টি Signal/day\n\n"
            "বিস্তারিত নিচে 👇"
        )

    # ─── Forex ───
    if any(f in msg_lower for f in ["forex", "ফরেক্স", "exness", "এক্সনেস", "fx"]):
        return (
            "💹 RTX EXNESS (Forex)! 🌸\n\n"
            "✅ সব Forex Pair support\n"
            "✅ 15 Minute Timeframe\n"
            "✅ AI Market Analysis\n"
            "✅ Real Twelvedata\n\n"
            "💰 8,000tk (Fixed)\n"
            "🤖 @rtxexness_bot\n"
            "🎁 Free: ৫টি Signal/day\n\n"
            "🔑 Twelvedata API লাগবে!\n"
            "বিস্তারিত নিচে 👇"
        )

    # ─── Binary ───
    if any(b in msg_lower for b in ["binary", "বাইনারি", "quotex", "কোটেক্স"]):
        return (
            "📈 Binary Trading Bot! 🌸\n\n"
            "🌱 Beginner: Qutex Signal (1,000tk)\n"
            "💎 Advanced: Qutex Premium (2,000tk)\n\n"
            "✅ Real-time Signal\n"
            "✅ 1M + 5M Timeframe\n"
            "✅ AI Powered\n\n"
            "🎁 Promo: RTX4241\n"
            "🔑 Twelvedata API লাগবে\n\n"
            "নিচের বাটন দেখুন 👇"
        )

    # ─── Signal ───
    if any(s in msg_lower for s in ["signal", "সিগনাল", "সিগন্যাল", "accuracy"]):
        return (
            "📊 RTX AI Signal! 🌸\n\n"
            "৪টি Bot থেকে Real-time Signal:\n\n"
            "📈 Binary — 1M candle\n"
            "💎 Premium — 1M + 5M\n"
            "💹 Forex — 15M entry\n"
            "🪙 Crypto — Multi-timeframe\n\n"
            "সঠিক Strategy + AI + Discipline\n"
            "= সফলতা ইনশাআল্লাহ! 🚀\n\n"
            "নিচের বাটন দেখুন 👇"
        )

    # ─── Buy ───
    if any(b in msg_lower for b in ["কিনব", "কিনতে", "buy", "কেনা", "কিনি"]):
        return (
            "🛒 কেনার Steps! 🌸\n\n"
            "1️⃣ Bot select করুন (৪টার একটা)\n"
            "2️⃣ App Open করুন\n"
            "3️⃣ Free Signal try করুন\n"
            "4️⃣ Buy Premium click\n"
            "5️⃣ Promo: RTX4241\n"
            "6️⃣ bKash: 01725218874\n"
            "7️⃣ TrxID submit\n"
            "8️⃣ ৫ মিনিটে Access! ⚡\n\n"
            "নিচের বাটন থেকে শুরু 👇"
        )

    # ─── Complaint ───
    if any(c in msg_lower for c in ["scam", "fake", "ফেক", "ভুয়া", "কাজ করছে না"]):
        return (
            "প্রিয় ভাই, বুঝতে পারছি 🙏\n\n"
            "ইনশাআল্লাহ সমাধান হবে।\n"
            "TrxID সহ @ratulhossain56 এ message দিন।\n"
            "দ্রুত সাহায্য পাবেন ✅"
        )

    # ─── Thanks ───
    if any(t in msg_lower for t in ["ধন্যবাদ", "thanks", "thank you", "জাযাকাল্লাহ"]):
        return random.choice([
            "জাযাকাল্লাহু খাইরান ভাই! 🌸\n"
            "আপনার জন্য দোয়া রইলো।\n\n"
            "আরো কিছু লাগলে বলুন 👇",
            
            "আলহামদুলিল্লাহ! আপনাকেও ধন্যবাদ! 🤲\n"
            "RTX Family ২৪/২৪ পাশে 🌟\n\n"
            "নিচের বাটন দেখুন 👇",
        ])

    # ─── Support/Admin ───
    if any(s in msg_lower for s in ["admin", "এডমিন", "support", "সাপোর্ট", "help"]):
        return (
            "👨‍💼 RTX Support! 🌸\n\n"
            "💬 Telegram: @ratulhossain56\n"
            "📞 WhatsApp: 01344594241\n"
            "🎯 Sales Bot: @rtxearn2_bot\n\n"
            "⏰ Response: ৫-৩০ মিনিট\n"
            "✅ ২৪/২৪ Available\n\n"
            "সরাসরি message দিন! 🚀"
        )

    # ─── Gemini AI Fallback ───
    if model:
        try:
            prompt = f"""
{COMPANY_CONTEXT}

Customer message: "{user_message}"

Rules:
- ৩-৫ লাইনে বাংলায় উত্তর
- Islamic tone (আসসালামু, ইনশাআল্লাহ, মাশাআল্লাহ)
- Positive + Sales focused
- Bot/product mention
- শেষে: "নিচের বাটন থেকে দেখুন 👇"
"""
            response = model.generate_content(prompt)
            reply = response.text.strip()
            
            if reply and len(reply) > 10:
                if len(reply) > 500:
                    lines = [l for l in reply.split('\n') if l.strip()]
                    reply = '\n'.join(lines[:7])
                if "বাটন" not in reply:
                    reply += "\n\nনিচের বাটন থেকে দেখুন 👇"
                return reply
        except Exception as e:
            log.warning(f"Gemini error: {e}")

    # ─── Ultimate Fallback ───
    return random.choice([
        (
            "আসসালামু আলাইকুম প্রিয় ভাই! 🌸\n\n"
            "RTX এ ৪টি Powerful Signal Bot:\n\n"
            "📈 Binary — 1,000tk\n"
            "💎 Premium — 2,000tk\n"
            "💹 Forex — 8,000tk\n"
            "🪙 Crypto — 5,000tk\n\n"
            "🎁 Promo: RTX4241\n"
            "নিচের বাটন দেখুন 👇"
        ),
        (
            "বিসমিল্লাহ প্রিয় ভাই! 🌸\n\n"
            "আপনার প্রশ্নের জন্য ধন্যবাদ!\n"
            "৪টি Bot এর একটা try করুন।\n\n"
            "🎁 Free Signal available!\n"
            "🎁 Promo: RTX4241\n\n"
            "নিচের বাটন থেকে দেখুন 👇"
        ),
        (
            "মাশাআল্লাহ ভাই! 🌸\n\n"
            "RTX Family ২৪/২৪ পাশে! 🤝\n\n"
            "🎯 Sales: @rtxearn2_bot\n"
            "👨‍💼 Support: @ratulhossain56\n\n"
            "নিচের বাটন দেখুন 👇"
        ),
    ])
