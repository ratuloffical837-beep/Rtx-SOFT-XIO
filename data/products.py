# ═══════════════════════════════════════
# RTX Products Database (4 Products)
# ═══════════════════════════════════════

PRODUCTS = {
    # ─── 📈 Binary Trading ───
    "binary": {
        "category":     "📈 Binary Trading",
        "name":         "Qutex Signal",
        "username":     "@qutex4241pro_bot",
        "mini_app":     "https://t.me/qutex4241pro_bot/signalapp",
        "price":        1500,
        "promo_price":  1000,
        "promo_code":   "RTX4241",
        "badge":        "📈",
        "type":         "Binary Trading (Forex based)",
        "needs_api":    True,
        "data_source":  "Twelvedata API",
        "free_signals": 3,
        "best_for":     "নতুন Binary Trader",
        "timeframe":    "1M candle",
        "features": [
            "সব Forex pair support",
            "Next candle UP/DOWN prediction",
            "Real-time Twelvedata Market Data",
            "Free: দৈনিক ৩টি Signal",
            "Premium: Unlimited Signal",
            "Beginner Friendly UI",
            "৫ মিনিটে Payment Approve",
        ],
        "how_it_works": (
            "Twelvedata API থেকে real-time market data নিয়ে "
            "Generate Signal button press করলে পরের candle এর "
            "direction (UP/DOWN) predict করে।"
        ),
    },

    # ─── 💎 Binary Premium ───
    "binary_premium": {
        "category":     "💎 Binary Premium",
        "name":         "Qutex Premium",
        "username":     "@qutexperiyam_bot",
        "mini_app":     "https://t.me/qutexperiyam_bot/qutexsignalbot",
        "price":        3000,
        "promo_price":  2000,
        "promo_code":   "RTX4241",
        "badge":        "💎",
        "type":         "Advanced Binary (1M + 5M)",
        "needs_api":    True,
        "data_source":  "Twelvedata API",
        "free_signals": 3,
        "best_for":     "Serious/Advanced Trader",
        "timeframe":    "1M + 5M candle",
        "features": [
            "সব Binary Signal features",
            "1 Minute Timeframe ⭐",
            "5 Minute Timeframe ⭐",
            "Advanced AI Indicators",
            "Professional UI",
            "Free: দৈনিক ৩টি Signal",
            "Premium: Unlimited Signal",
        ],
        "how_it_works": (
            "Twelvedata API থেকে real-time data নিয়ে advanced "
            "indicator দিয়ে ১ মিনিট ও ৫ মিনিটের signal generate "
            "করে। Advanced traders দের জন্য perfect।"
        ),
    },

    # ─── 💹 Forex Trading ───
    "forex": {
        "category":     "💹 Forex Trading",
        "name":         "RTX EXNESS",
        "username":     "@rtxexness_bot",
        "mini_app":     "http://t.me/rtxexness_bot/rtxexsignalbot",
        "price":        8000,
        "promo_price":  None,
        "promo_code":   None,
        "badge":        "💹",
        "type":         "Real Forex Trading (Exness)",
        "needs_api":    True,
        "data_source":  "Twelvedata API",
        "free_signals": 5,
        "best_for":     "Real Forex Trader (Exness)",
        "timeframe":    "15 Minute Entry",
        "features": [
            "সব Forex pair support",
            "15 Minute Timeframe Entry",
            "AI Market Analysis",
            "Real-time Market Data",
            "Free: দৈনিক ৫টি Signal",
            "Premium: Unlimited Signal",
            "Fast Execution Support",
            "২৪/২৪ Premium Support",
        ],
        "how_it_works": (
            "Twelvedata API থেকে real-time forex data নিয়ে AI দিয়ে "
            "analyze করে ১৫ মিনিটের timeframe এ Entry signal দেয়। "
            "সব forex pair support করে।"
        ),
    },

    # ─── 🪙 Crypto Trading ───
    "crypto": {
        "category":     "🪙 Crypto Trading",
        "name":         "RTX PRO MAX AI",
        "username":     "@rtxpromaxai4241_bot",
        "mini_app":     "https://t.me/rtxpromaxai4241_bot/binancesignalbot",
        "price":        5000,
        "promo_price":  None,
        "promo_code":   None,
        "badge":        "🪙",
        "type":         "Crypto Trading (Binance)",
        "needs_api":    False,   # ⚠️ Crypto তে API key দরকার নেই
        "data_source":  "Binance API (Built-in)",
        "free_signals": 2,
        "best_for":     "Pro Crypto Trader",
        "timeframe":    "Multi-timeframe",
        "features": [
            "Binance Spot Market Signal",
            "Binance Future Market Signal",
            "৫টি Advanced Strategy Mode",
            "TP1, TP2, TP3 + Stop Loss",
            "Signal Grade: A+, A, B+, B",
            "Real-time Binance Data",
            "Free: দৈনিক ২টি Signal",
            "Premium: Unlimited Signal",
            "❌ API Key লাগে না (Built-in)",
        ],
        "how_it_works": (
            "Binance API built-in — কোনো API key setup লাগে না। "
            "৫টা strategy — SWEEP RECLAIM, CRT+TBS PRO, "
            "WYCKOFF+ICT/SMC, QM+SMC, PRICE ACTION+FIB।"
        ),
        "strategies": [
            {"name": "SWEEP RECLAIM",      "emoji": "🔵", "desc": "Liquidity Sweep + Reclaim"},
            {"name": "CRT + TBS PRO",      "emoji": "🟣", "desc": "Candle Range Theory + TBS"},
            {"name": "WYCKOFF + ICT/SMC",  "emoji": "🟡", "desc": "Wyckoff + ICT Order Block"},
            {"name": "QM + SMC",           "emoji": "🟠", "desc": "Quasimodo + SMC"},
            {"name": "PRICE ACTION + FIB", "emoji": "🟢", "desc": "Price Action + Fibonacci"},
        ],
    },
}
