# ═══════════════════════════════════════
# 260+ Keywords for Smart Reply
# গ্রুপে user message এ এই keyword থাকলে
# bot reply দেবে (Mode B)
# ═══════════════════════════════════════

REPLY_KEYWORDS = [
    # ─── 💰 Trading Related (35) ───
    "trade", "trading", "ট্রেড", "ট্রেডিং", "ট্রেডার",
    "buy", "sell", "কিনব", "কিনতে", "কিনি", "কেনা", "কেনার",
    "বিক্রি", "বিক্রয়", "order", "position", "entry", "exit",
    "long", "short", "spot", "future", "স্পট", "ফিউচার",
    "candle", "ক্যান্ডেল", "chart", "চার্ট", "pip", "lot",
    "leverage", "লিভারেজ", "margin", "মার্জিন", "hedge",

    # ─── 📊 Signal Related (30) ───
    "signal", "সিগনাল", "সিগন্যাল", "সিগ্নাল",
    "accurate", "accuracy", "সঠিক", "কতটুকু", "সঠিকতা",
    "win", "loss", "লস", "প্রফিট", "profit", "লাভ",
    "up", "down", "আপ", "ডাউন", "call", "put",
    "green", "red", "সবুজ", "লাল", "buy signal", "sell signal",
    "prediction", "predict", "ভবিষ্যদ্বাণী", "auto signal",

    # ─── 💵 Money/Price (35) ───
    "price", "প্রাইস", "দাম", "মূল্য", "কত", "কতটাকা",
    "টাকা", "taka", "tk", "cost", "খরচ", "fee", "চার্জ",
    "বিনিয়োগ", "invest", "investment", "capital", "ক্যাপিটাল",
    "cheap", "সস্তা", "expensive", "দামি", "budget", "বাজেট",
    "money", "মানি", "cash", "ক্যাশ", "amount", "এমাউন্ট",
    "balance", "ব্যালেন্স", "deposit", "withdraw", "উইথড্র",

    # ─── 📈 Market (30) ───
    "market", "মার্কেট", "মারকেট", "বাজার",
    "forex", "ফরেক্স", "ফরেক্স", "fx",
    "crypto", "ক্রিপ্টো", "ক্রাপ্ট", "ক্রিপ্টু",
    "bitcoin", "btc", "বিটকয়েন", "eth", "ইথেরিয়াম",
    "binance", "বাইনান্স", "বাইনান্ট", "exness", "এক্সনেস",
    "binary", "বাইনারি", "বাইনেরি", "quotex", "কোটেক্স",
    "usd", "eur", "gbp", "jpy", "pair", "পেয়ার",

    # ─── 🤖 Bot/App (25) ───
    "bot", "বট", "রোবট",
    "app", "এপ", "অ্যাপ", "application", "সফটওয়্যার",
    "mini app", "মিনি এপ", "telegram bot", "টেলিগ্রাম",
    "qutex", "কিউটেক্স", "rtx", "আরটিএক্স",
    "pro max", "প্রিমিয়াম", "premium", "signal bot",
    "install", "ইনস্টল", "download", "ডাউনলোড", "setup",

    # ─── 👨‍💼 Admin/Support (25) ───
    "admin", "এডমিন", "এ্যাডমিন", "admin ভাই",
    "support", "সাপোর্ট", "সাপোট", "help", "হেল্প",
    "সাহায্য", "মাদাত", "মদদ", "assist",
    "contact", "যোগাযোগ", "কন্টাক্ট", "message",
    "সমস্যা", "problem", "issue", "trouble", "সমাধান",
    "call", "কল", "whatsapp", "হোয়াটসঅ্যাপ", "wa",

    # ─── 💳 Payment (30) ───
    "payment", "পেমেন্ট", "পেমিন্ট", "pay", "paid",
    "bkash", "বিকাশ", "বীকাশ", "nagad", "নগদ",
    "rocket", "রকেট", "upay", "উপায়",
    "send money", "সেন্ড মানি", "cash out", "ক্যাশ আউট",
    "trxid", "ট্রানজেকশন", "transaction", "transaction id",
    "receipt", "রিসিপ্ট", "verify", "verification", "যাচাই",
    "approve", "approval", "একসেস", "access", "unlock",
    "renew", "renewal", "রিনিউ",

    # ─── 🎁 Promo/Offer (20) ───
    "promo", "প্রোমো", "প্রমো", "promo code",
    "discount", "ছাড়", "ডিসকাউন্ট", "offer", "অফার",
    "code", "কোড", "coupon", "কুপন", "deal",
    "free", "ফ্রি", "trial", "ট্রায়াল", "demo", "ডেমো",
    "cashback", "ক্যাশব্যাক", "bonus", "বোনাস",

    # ─── 🔑 API Key / Twelvedata (25) ───
    "api", "এপিআই", "এপি", "api key", "এপিআই কী", "কী",
    "twelvedata", "টুয়েলভ", "twelve data", "টুয়েলভডাটা",
    "setting", "সেটিং", "সেটিংস", "config", "configure",
    "input", "ইনপুট", "paste", "পেস্ট", "add",
    "connect", "কানেক্ট", "connection", "link",
    "gmail", "জিমেল", "google", "গুগল", "sign up", "signup",
    "register", "রেজিস্টার", "login", "লগইন", "লগিং",

    # ─── 🕋 Islamic/Greeting (25) ───
    "salam", "সালাম", "আসসালামু", "assalamu", "assalam",
    "walaikum", "ওয়ালাইকুম", "আসসালাম",
    "bismillah", "বিসমিল্লাহ", "আলহামদুলিল্লাহ",
    "মাশাআল্লাহ", "ইনশাআল্লাহ", "জাযাকাল্লাহ",
    "ভাই", "bhai", "ভাইয়া", "brother", "bro",
    "hi", "hello", "হাই", "হ্যালো", "hey", "namaskar",
    "good morning", "good night", "শুভ সকাল",

    # ─── 💪 Motivation/Income (20) ───
    "success", "সফল", "সফলতা", "সাকসেস",
    "income", "আয়", "উপার্জন", "earn", "earning",
    "rich", "ধনী", "বড়লোক", "লাখপতি", "কোটিপতি",
    "future", "ভবিষ্যৎ", "career", "ক্যারিয়ার",
    "job", "চাকরি", "business", "ব্যবসা", "hustle",

    # ─── 🙋 General/Question (25) ───
    "কেমন", "how", "how are you", "কেমন আছেন", "কেমন আছো",
    "কী", "কি", "what", "কী করে", "how to", "কীভাবে",
    "কেন", "why", "কখন", "when", "কোথায়", "where",
    "thanks", "ধন্যবাদ", "thank you", "shukria",
    "please", "প্লিজ", "দয়া করে",
    "yes", "no", "হ্যাঁ", "না", "ok", "ওকে",

    # ─── ⚠️ Complaint/Doubt (15) ───
    "scam", "স্ক্যাম", "fake", "ফেক", "ভুয়া",
    "genuine", "আসল", "real", "রিয়েল", "প্রকৃত",
    "cheat", "প্রতারণা", "কাজ করছে না", "পাইনি", "পায়নি",
    "refund", "রিফান্ড", "ফেরত",

    # ─── 🎯 Miscellaneous (20) ───
    "time", "সময়", "কতক্ষণ", "duration", "period",
    "day", "দিন", "মাস", "month", "year", "বছর",
    "start", "শুরু", "begin", "স্টার্ট",
    "stop", "থামা", "close", "বন্ধ",
    "restart", "রিস্টার্ট", "reset", "update", "আপডেট",
]

# Total: 260+ keywords ✅
