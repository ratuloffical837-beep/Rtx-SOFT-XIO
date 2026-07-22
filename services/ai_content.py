def generate_smart_reply(user_message: str) -> str:
    """Islamic + Positive + Smart reply"""
    
    msg_lower = user_message.lower().strip()

    # ─── Salam ───
    salam_words = ["salam", "সালাম", "আসসালামু", "assalamu", "assalam"]
    if any(g in msg_lower for g in salam_words):
        return random.choice([
            "ওয়ালাইকুম আসসালাম ওয়া রহমাতুল্লাহ প্রিয় ভাই! 🌸\nকীভাবে সাহায্য করতে পারি?\n\nনিচের বাটন থেকে দেখুন 👇",
            "ওয়ালাইকুম আসসালাম প্রিয় ভাই! 🕋\nআলহামদুলিল্লাহ আপনাকে পেয়ে খুশি!\n\nকোনো প্রশ্ন থাকলে বলুন 👇",
        ])

    # ─── Hi / Hello ───
    greetings = ["hi", "hello", "হাই", "হ্যালো", "hey"]
    if any(g in msg_lower for g in greetings):
        return random.choice([
            "আসসালামু আলাইকুম প্রিয় ভাই! 🌸\nবিসমিল্লাহ, RTX এ স্বাগতম!\n\nনিচের বাটন থেকে যেকোনো কিছু জানুন 👇",
            "আসসালামু আলাইকুম ভাই! 🕋\nমাশাআল্লাহ, কীভাবে সাহায্য করতে পারি? 👇",
        ])

    # ─── How are you ───
    how_are = ["কেমন আছেন", "কেমন আছো", "কেমন আছ", "how are you"]
    if any(h in msg_lower for h in how_are):
        return random.choice([
            "আলহামদুলিল্লাহ ভালো আছি প্রিয় ভাই! 😊\nআপনি কেমন আছেন?\n\nকোনো সাহায্য লাগলে নিচের বাটন দেখুন 👇",
            "আলহামদুলিল্লাহ, মাশাআল্লাহ ভালো আছি! 🌸\nআপনার জন্য দোয়া রইলো।\n\nনিচের বাটন থেকে সব জানতে পারবেন 👇",
        ])

    # ─── Name ───
    name_words = ["নাম কি", "নাম কী", "তোমার নাম", "your name", "name"]
    if any(n in msg_lower for n in name_words):
        return (
            "আসসালামু আলাইকুম! 🌸\n\n"
            "আমি RTX Trading Assistant! 🤖\n"
            "আমি আপনাকে Trading Signal, Bot Info,\n"
            "Payment Help সবকিছুতে সাহায্য করবো\n"
            "ইনশাআল্লাহ! 🚀\n\n"
            "নিচের বাটন থেকে যেকোনো কিছু জানুন 👇"
        )

    # ─── Signal quality ───
    signal_words = ["সিগনাল কেমন", "signal কেমন", "সিগন্যাল", "accuracy", "কতটুকু সঠিক"]
    if any(s in msg_lower for s in signal_words):
        return (
            "মাশাআল্লাহ প্রিয় ভাই! 🌸\n\n"
            "আমাদের ৩টি Bot Real-time Market Data\n"
            "থেকে AI দিয়ে Signal generate করে! 📊\n\n"
            "🥉 Qutex Signal — Forex (Twelvedata)\n"
            "🥈 Qutex Premium — 1m/5m Forex\n"
            "🥇 RTX PRO MAX AI — Binance Crypto\n\n"
            "সঠিক Strategy + AI Signal দিয়ে\n"
            "ইনশাআল্লাহ ভালো result পাবেন! 🚀\n\n"
            "আগে Free Signal try করে দেখুন 👇"
        )

    # ─── Details / বিস্তারিত ───
    detail_words = ["বিস্তারিত", "details", "জানতে চাই", "বলো", "বলুন", "explain"]
    if any(d in msg_lower for d in detail_words):
        return (
            "বিসমিল্লাহ প্রিয় ভাই! 🌸\n\n"
            "💎 আমাদের ৩টি Signal Bot:\n\n"
            "🥉 Qutex Signal — 1,000tk (Promo)\n"
            "   Forex Signal, নতুনদের জন্য সেরা\n"
            "   Free: দৈনিক ৩টি Signal\n\n"
            "🥈 Qutex Premium — 2,000tk (Promo)\n"
            "   1m/5m Advanced Forex Signal\n"
            "   Free: দৈনিক ৩টি Signal\n\n"
            "🥇 RTX PRO MAX AI — 5,000tk\n"
            "   Binance Crypto, ৫টি Strategy\n"
            "   Free: দৈনিক ২টি Signal\n\n"
            "🎁 Promo Code: RTX4241\n"
            "💳 bKash/Nagad: 01725218874\n"
            "⏰ ৫ মিনিটে Access ইনশাআল্লাহ!\n\n"
            "নিচের বাটন থেকে যেকোনো Bot এ ঢুকুন 👇"
        )

    # ─── Price ───
    price_words = ["price", "প্রাইস", "দাম", "কত টাকা", "কত দাম", "খরচ"]
    if any(p in msg_lower for p in price_words):
        return (
            "বিসমিল্লাহ প্রিয় ভাই! 🌸\n\n"
            "💰 RTX Signal Bot Price:\n\n"
            "🥉 Qutex Signal: 1,000tk (Promo RTX4241)\n"
            "🥈 Qutex Premium: 2,000tk (Promo RTX4241)\n"
            "🥇 RTX PRO MAX AI: 5,000tk\n\n"
            "🎁 Promo Code: RTX4241\n"
            "💳 bKash/Nagad: 01725218874\n\n"
            "ইনশাআল্লাহ সঠিক Bot দিয়ে সফলতা আসবে! 🚀\n\n"
            "নিচের বাটন থেকে কিনুন 👇"
        )

    # ─── Promo ───
    promo_words = ["promo", "প্রোমো", "discount", "ছাড়", "code", "কোড"]
    if any(p in msg_lower for p in promo_words):
        return (
            "মাশাআল্লাহ প্রিয় ভাই! 🎁\n\n"
            "🔑 Promo Code: RTX4241\n\n"
            "✅ Qutex Signal: 1500→1000tk (Save 500tk!)\n"
            "✅ Qutex Premium: 3000→2000tk (Save 1000tk!)\n"
            "⚠️ RTX PRO MAX AI: 5000tk (fixed)\n\n"
            "এখনই ব্যবহার করুন ইনশাআল্লাহ! 🌸\n\n"
            "নিচের বাটন দেখুন 👇"
        )

    # ─── Payment ───
    payment_words = ["bkash", "বিকাশ", "nagad", "নগদ", "payment", "পেমেন্ট", "send money", "টাকা পাঠাবো"]
    if any(p in msg_lower for p in payment_words):
        return (
            "বিসমিল্লাহ ভাই! 💳\n\n"
            "📱 bKash: 01725218874 (Send Money)\n"
            "📱 Nagad: 01725218874 (Send Money)\n\n"
            "📌 Steps:\n"
            "1️⃣ Send Money → 01725218874\n"
            "2️⃣ SMS থেকে TrxID copy\n"
            "3️⃣ App এ paste\n"
            "4️⃣ ৫ মিনিটে Access ইনশাআল্লাহ! ⚡\n\n"
            "সমস্যায় @ratulhossain56 🙏"
        )

    # ─── How to buy / কিভাবে কিনবো ───
    buy_words = ["কিভাবে কিনবো", "কিনব", "কিনতে", "কিনি", "buy", "purchase", "কেনা"]
    if any(b in msg_lower for b in buy_words):
        return (
            "বিসমিল্লাহ প্রিয় ভাই! 🌸\n\n"
            "📌 কেনার সহজ Steps:\n\n"
            "1️⃣ নিচের বাটনে Bot App খুলুন\n"
            "2️⃣ Free Signal try করুন\n"
            "3️⃣ Buy Premium click করুন\n"
            "4️⃣ Promo দিন: RTX4241\n"
            "5️⃣ bKash/Nagad: 01725218874\n"
            "6️⃣ TrxID submit করুন\n"
            "7️⃣ ৫ মিনিটে Access! ⚡\n\n"
            "ইনশাআল্লাহ সবকিছু সহজ! 🚀\n\n"
            "নিচের বাটন থেকে শুরু করুন 👇"
        )

    # ─── How app works ───
    app_words = ["কিভাবে কাজ করে", "কেমন কাজ", "how it works", "app কিভাবে", "বট কিভাবে"]
    if any(a in msg_lower for a in app_words):
        return (
            "মাশাআল্লাহ ভাই, চমৎকার প্রশ্ন! 🌸\n\n"
            "🤖 আমাদের Bot গুলো Real-time Market\n"
            "Data (Binance/Twelvedata) থেকে AI দিয়ে\n"
            "Signal generate করে!\n\n"
            "📊 Qutex Signal/Premium:\n"
            "→ Generate Signal button press\n"
            "→ Next candle UP/DOWN predict\n\n"
            "🚀 RTX PRO MAX AI:\n"
            "→ ৫টি Strategy Mode select\n"
            "→ AI Analysis + TP1/TP2/TP3 + SL\n\n"
            "নিচের বাটন থেকে App open করে দেখুন 👇"
        )

    # ─── Refund ───
    if "refund" in msg_lower or "রিফান্ড" in msg_lower:
        return (
            "প্রিয় ভাই! 🌸\n\n"
            "আমাদের Bot ইনশাআল্লাহ সঠিক Signal দেয়!\n"
            "আগে Free Signal try করে দেখুন।\n"
            "পছন্দ হলে Premium নিন!\n\n"
            "সমস্যায় @ratulhossain56 পাশে আছেন 🤝"
        )

    # ─── Complaint ───
    complaint_words = ["scam", "fake", "ফেক", "কাজ করছে না", "পাইনি", "প্রতারণা"]
    if any(c in msg_lower for c in complaint_words):
        return (
            "প্রিয় ভাই, সমস্যাটা বুঝতে পারছি 🙏\n\n"
            "আলহামদুলিল্লাহ সমাধান হবে ইনশাআল্লাহ।\n"
            "TrxID সহ @ratulhossain56 এ মেসেজ দিন।\n"
            "দ্রুত সাহায্য করা হবে ✅"
        )

    # ─── Thanks ───
    thanks_words = ["ধন্যবাদ", "thanks", "thank you", "জাযাকাল্লাহ"]
    if any(t in msg_lower for t in thanks_words):
        return random.choice([
            "জাযাকাল্লাহু খাইরান প্রিয় ভাই! 🌸\n"
            "আপনার জন্য দোয়া রইলো।\n\n"
            "যেকোনো সময় প্রশ্ন করতে পারেন 👇",
            
            "আলহামদুলিল্লাহ! ভাই আপনাকেও ধন্যবাদ! 🤲\n"
            "RTX Family সবসময় আপনার পাশে ২৪/২৪ 🌟\n\n"
            "নিচের বাটন থেকে Bot দেখুন 👇",
        ])

    # ─── Free signal ───
    free_words = ["free", "ফ্রি", "trial", "বিনামূল্যে", "ফ্রিতে"]
    if any(f in msg_lower for f in free_words):
        return (
            "মাশাআল্লাহ ভাই! হ্যাঁ Free Signal আছে! 🎉\n\n"
            "🥉 Qutex Signal: দৈনিক ৩টি Free\n"
            "🥈 Qutex Premium: দৈনিক ৩টি Free\n"
            "🥇 RTX PRO MAX AI: দৈনিক ২টি Free\n\n"
            "নিচের বাটন থেকে App open করে\n"
            "এখনই Free Signal নিন ইনশাআল্লাহ! 👇"
        )

    # ─── Gemini AI Reply ───
    prompt = f"""
{COMPANY_CONTEXT}

{AI_RULES}

Customer message: "{user_message}"

IMPORTANT:
- ৩-৫ লাইনে উত্তর দাও (ছোট)
- বাংলায়
- Islamic tone
- Product info relate করো
- শেষে: "নিচের বাটন থেকে দেখুন 👇"
- কোনো নেগেটিভ কথা না
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

    # ─── Smart Fallback (NOT generic) ───
    return random.choice([
        (
            "আসসালামু আলাইকুম প্রিয় ভাই! 🌸\n\n"
            "আমি RTX Trading Assistant! 🤖\n"
            "আমাদের ৩টি Powerful AI Signal Bot আছে:\n\n"
            "🥉 Qutex Signal — Forex (1,000tk)\n"
            "🥈 Qutex Premium — 1m/5m (2,000tk)\n"
            "🥇 RTX PRO MAX AI — Crypto (5,000tk)\n\n"
            "🎁 Promo: RTX4241\n"
            "নিচের বাটন থেকে দেখুন ইনশাআল্লাহ 👇"
        ),
        (
            "বিসমিল্লাহ প্রিয় ভাই! 🌸\n\n"
            "আপনার প্রশ্নের জন্য ধন্যবাদ!\n\n"
            "💎 আমাদের Bot গুলো Real-time AI Signal দেয়!\n"
            "আগে Free Signal try করুন,\n"
            "পছন্দ হলে Premium নিন!\n\n"
            "🎁 Promo: RTX4241 (500-1000tk ছাড়!)\n"
            "নিচের বাটন থেকে App open করুন 👇"
        ),
        (
            "মাশাআল্লাহ প্রিয় ভাই! 🌸\n\n"
            "RTX Trading Family আপনার পাশে ২৪/২৪! 🤝\n\n"
            "📱 App Link:\n"
            "🥉 @qutex4241pro_bot\n"
            "🥈 @qutexperiyam_bot\n"
            "🥇 @rtxpromaxai4241_bot\n\n"
            "💳 bKash/Nagad: 01725218874\n"
            "ইনশাআল্লাহ সফলতা আসবে! 🚀\n\n"
            "নিচের বাটন দেখুন 👇"
        ),
    ])
