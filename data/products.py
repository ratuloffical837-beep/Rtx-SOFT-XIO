# ═══════════════════════════════════════
# RTX Products Database
# ═══════════════════════════════════════

PRODUCTS = {
    "bot1": {
        "name": "Qutex Signal 📊",
        "username": "@qutex4241pro_bot",
        "mini_app": "https://t.me/qutex4241pro_bot/signalapp",
        "price": 1500,
        "promo_price": 1000,
        "promo_code": "RTX4241",
        "type": "Forex Trading",
        "data_source": "Twelvedata API",
        "free_signals": 3,
        "premium_signals": "Unlimited",
        "badge": "🥉",
        "best_for": "নতুন Trader",
        "features": [
            "সকল Forex Market Signal",
            "Next Candle Prediction",
            "Real-time Twelvedata Market Data",
            "Free: দৈনিক ৩টি Signal",
            "Premium: Unlimited Signal",
            "৫ মিনিটে Payment Approve",
            "Signal Generate Button",
        ],
        "how_it_works": (
            "Twelvedata API থেকে real-time market data এনে "
            "প্রতি মিনিটের শেষ ২-৫ সেকেন্ডে Generate Signal "
            "button press করলে পরের candle UP/DOWN predict করে।"
        ),
    },
    "bot2": {
        "name": "Qutex Premium 📊💵",
        "username": "@qutexperiyam_bot",
        "mini_app": "https://t.me/qutexperiyam_bot/qutexsignalbot",
        "price": 3000,
        "promo_price": 2000,
        "promo_code": "RTX4241",
        "type": "Advanced Forex Trading",
        "data_source": "Twelvedata API",
        "free_signals": 3,
        "premium_signals": "Unlimited",
        "badge": "🥈",
        "best_for": "Serious Trader",
        "features": [
            "Qutex Signal এর সব Features",
            "আরো Advanced Indicators",
            "1 Minute Signal ⭐",
            "5 Minute Signal ⭐",
            "Professional UI",
            "Free: দৈনিক ৩টি Signal",
            "Premium: Unlimited Signal",
        ],
        "how_it_works": (
            "Qutex Signal এর সব features + advanced indicators। "
            "১ মিনিট ও ৫ মিনিট signal generate করা যায়। "
            "Twelvedata real-time data দিয়ে accurate signal।"
        ),
    },
    "bot3": {
        "name": "RTX PRO MAX AI 🚀",
        "username": "@rtxpromaxai4241_bot",
        "mini_app": "https://t.me/rtxpromaxai4241_bot/binancesignalbot",
        "price": 5000,
        "promo_price": None,
        "promo_code": None,
        "type": "Crypto Trading (Binance)",
        "data_source": "Binance API",
        "free_signals": 2,
        "premium_signals": "Unlimited",
        "badge": "🥇",
        "best_for": "Pro Trader",
        "features": [
            "Binance Real-time Data",
            "Spot + Future Trading Signal",
            "Signal Grade: A+, A, B+, B",
            "TP1, TP2, TP3 + Stop Loss",
            "৫টি Signal Strategy Mode",
            "Free: দৈনিক ২টি Signal",
            "Premium: Unlimited Signal",
        ],
        "how_it_works": (
            "Binance API থেকে crypto data নিয়ে AI দিয়ে analyze করে। "
            "৫টা strategy mode — SWEEP RECLAIM, CRT+TBS PRO, "
            "WYCKOFF+ICT/SMC, QM+SMC, PRICE ACTION+FIB।"
        ),
        "strategies": [
            {"name": "SWEEP RECLAIM",      "emoji": "🔵", "desc": "Liquidity Sweep + Reclaim"},
            {"name": "CRT + TBS PRO",      "emoji": "🟣", "desc": "Candle Range Theory + Three Bar Setup"},
            {"name": "WYCKOFF + ICT/SMC",  "emoji": "🟡", "desc": "Wyckoff Phase + ICT CHoCH/Order Block"},
            {"name": "QM + SMC",           "emoji": "🟠", "desc": "Quasimodo Reversal + SMC Order Block"},
            {"name": "PRICE ACTION + FIB", "emoji": "🔵", "desc": "Impulsive Move + Fibonacci + Candlestick"},
        ],
    },
}
