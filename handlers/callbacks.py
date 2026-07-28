# ═══════════════════════════════════════
# All Callback (Button) Handlers
# ═══════════════════════════════════════

import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from data.products import PRODUCTS
from config import (
    SUPPORT_USERNAME, BKASH_NUMBER, NAGAD_NUMBER,
    WHATSAPP_NUMBER, PROMO_CODE, TWELVEDATA_SITE,
)

log = logging.getLogger(__name__)


# ═══════════════════════════════════════
# Category Detail Handler (৪টি button)
# ═══════════════════════════════════════

async def show_category(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """৪টি category বাটনের যেকোনো একটা click করলে detail দেখায়"""
    query = update.callback_query
    await query.answer()

    # cat_binary → binary
    cat_key = query.data.replace("cat_", "")
    product = PRODUCTS.get(cat_key)

    if not product:
        await query.edit_message_text("দুঃখিত, product পাওয়া যায়নি!")
        return

    # Features list
    features = "\n".join(f"  ✅ {f}" for f in product["features"])

    # Strategies (শুধু crypto তে আছে)
    strategies = ""
    if "strategies" in product:
        strategies = "\n━━━━━━━━━━━━━━━━━━━━\n🎯 Strategy Modes:\n"
        for i, s in enumerate(product["strategies"], 1):
            strategies += f"  {i}. {s['emoji']} {s['name']}\n"

    # Price section
    if product["promo_price"]:
        price_text = (
            f"💰 Regular Price: {product['price']:,}tk\n"
            f"🎁 Promo ({product['promo_code']}): {product['promo_price']:,}tk\n"
            f"💵 Save: {product['price'] - product['promo_price']:,}tk!"
        )
        buy_label = f"🛒 কিনুন — {product['promo_price']:,}tk"
    else:
        price_text = (
            f"💰 Price: {product['price']:,}tk (Fixed)\n"
            f"⚠️ কোনো Promo Code নেই"
        )
        buy_label = f"🛒 কিনুন — {product['price']:,}tk"

    # API Key section
    if product["needs_api"]:
        api_section = (
            f"\n━━━━━━━━━━━━━━━━━━━━\n"
            f"🔑 Twelvedata API Key লাগবে\n"
            f"━━━━━━━━━━━━━━━━━━━━\n"
            f"📝 কীভাবে পাবেন:\n"
            f"1️⃣ {TWELVEDATA_SITE} এ যান\n"
            f"2️⃣ Google/Gmail দিয়ে Sign Up\n"
            f"3️⃣ API Key copy করুন\n"
            f"4️⃣ App এর Setting → Paste\n\n"
            f"🎁 Free: 800 calls/day\n"
            f"⚠️ প্রতিজনের আলাদা key লাগবে!\n"
        )
    else:
        api_section = (
            f"\n━━━━━━━━━━━━━━━━━━━━\n"
            f"✨ API Key দরকার নেই!\n"
            f"━━━━━━━━━━━━━━━━━━━━\n"
            f"Binance API built-in!\n"
            f"সরাসরি use করুন।\n"
        )

    # Full message
    text = (
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"{product['badge']} {product['category']}\n"
        f"━━━━━━━━━━━━━━━━━━━━\n\n"
        f"🎯 {product['name']}\n"
        f"🤖 Bot: {product['username']}\n"
        f"📊 Type: {product['type']}\n"
        f"⏰ Timeframe: {product['timeframe']}\n"
        f"⭐ Best for: {product['best_for']}\n\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"ℹ️ কীভাবে কাজ করে:\n\n"
        f"{product['how_it_works']}\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"✨ Features:\n\n"
        f"{features}"
        f"{strategies}\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"🎁 Free Signal: দৈনিক {product['free_signals']}টি\n"
        f"💎 Premium: Unlimited\n\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"{price_text}"
        f"{api_section}"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"💳 Payment: {BKASH_NUMBER}\n"
        f"👨‍💼 Support: {SUPPORT_USERNAME}\n"
        f"━━━━━━━━━━━━━━━━━━━━"
    )

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton(buy_label, callback_data=f"buy_{cat_key}")],
        [InlineKeyboardButton("📱 Open App", url=product["mini_app"])],
        [InlineKeyboardButton("🎬 Live Proof", url="https://t.me/ratulhossain4241")],
        [
            InlineKeyboardButton("❓ FAQ", callback_data="faq"),
            InlineKeyboardButton("👨‍💼 Support", callback_data="support"),
        ],
        [InlineKeyboardButton("🔙 Home", callback_data="back_start")],
    ])

    try:
        await query.edit_message_text(text=text, reply_markup=keyboard)
    except Exception as e:
        log.error(f"show_category error: {e}")


# ═══════════════════════════════════════
# Buy Handler
# ═══════════════════════════════════════

async def buy_product(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """কেনার instruction দেখায়"""
    query = update.callback_query
    await query.answer()

    cat_key = query.data.replace("buy_", "")
    product = PRODUCTS.get(cat_key)
    if not product:
        return

    # Price + Promo
    if product["promo_price"]:
        price = product["promo_price"]
        price_text = (
            f"💰 Amount: {price:,}tk\n"
            f"   (Promo Code: {product['promo_code']})\n"
            f"   Regular: {product['price']:,}tk"
        )
        promo_step = (
            f"\n📌 STEP 5: Promo Code\n"
            f"   Code: {product['promo_code']}\n"
            f"   App এ Promo field এ enter করুন\n"
        )
    else:
        price = product["price"]
        price_text = f"💰 Amount: {price:,}tk (Fixed)"
        promo_step = ""

    # API Step
    if product["needs_api"]:
        api_step = (
            f"\n📌 STEP 6: API Key Setup\n"
            f"   1. {TWELVEDATA_SITE} → Gmail Login\n"
            f"   2. API Key copy করুন\n"
            f"   3. App → Setting → Paste\n"
        )
    else:
        api_step = "\n✨ API Key লাগে না!\n"

    text = (
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"🎉 চমৎকার সিদ্ধান্ত!\n"
        f"━━━━━━━━━━━━━━━━━━━━\n\n"
        f"{product['badge']} {product['name']}\n"
        f"🤖 {product['username']}\n\n"
        f"━━━━━━━━━━━━━━━━━━━━\n\n"
        f"📌 STEP 1: App Open\n"
        f"   নিচে 'Open App' click করুন\n\n"
        f"📌 STEP 2: Free Signal Try\n"
        f"   আগে free signal try করুন\n\n"
        f"📌 STEP 3: Buy Premium\n"
        f"   App এ 'Buy Premium' click\n\n"
        f"📌 STEP 4: Payment\n"
        f"   📱 bKash: {BKASH_NUMBER} (Send Money)\n"
        f"   📱 Nagad: {NAGAD_NUMBER} (Send Money)\n"
        f"   {price_text}"
        f"{promo_step}"
        f"{api_step}"
        f"\n━━━━━━━━━━━━━━━━━━━━\n\n"
        f"⏰ ৫ মিনিটে Approve!\n"
        f"✅ Instantly access!\n\n"
        f"🆘 সমস্যায়: {SUPPORT_USERNAME}\n"
        f"━━━━━━━━━━━━━━━━━━━━"
    )

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("🚀 Open App", url=product["mini_app"])],
        [InlineKeyboardButton("🆘 সমস্যা হচ্ছে", callback_data="help_payment")],
        [InlineKeyboardButton("👨‍💼 Admin", url=f"https://t.me/{SUPPORT_USERNAME.lstrip('@')}")],
        [InlineKeyboardButton("🔙 Back", callback_data=f"cat_{cat_key}")],
        [InlineKeyboardButton("🏠 Home", callback_data="back_start")],
    ])

    try:
        await query.edit_message_text(text=text, reply_markup=keyboard)
    except Exception as e:
        log.error(f"buy_product error: {e}")


# ═══════════════════════════════════════
# FAQ System
# ═══════════════════════════════════════

async def show_faq(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """FAQ menu"""
    query = update.callback_query
    await query.answer()

    text = (
        "━━━━━━━━━━━━━━━━━━━━\n"
        "❓ Frequently Asked Questions\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"
        "যেকোনো প্রশ্নে click করুন 👇\n\n"
        "━━━━━━━━━━━━━━━━━━━━"
    )

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("🔑 API Key কীভাবে পাবো?", callback_data="faq_api")],
        [InlineKeyboardButton("🔒 Bot safe কিনা?", callback_data="faq_safe")],
        [InlineKeyboardButton("💰 কত income হয়?", callback_data="faq_earn")],
        [InlineKeyboardButton("📱 কোন device এ চলে?", callback_data="faq_device")],
        [InlineKeyboardButton("⏰ কত সময়ে access?", callback_data="faq_access")],
        [InlineKeyboardButton("🔄 Refund policy?", callback_data="faq_refund")],
        [InlineKeyboardButton("🎁 Promo কীভাবে?", callback_data="faq_promo")],
        [InlineKeyboardButton("💳 Payment কীভাবে?", callback_data="faq_payment")],
        [InlineKeyboardButton("🆓 Free trial আছে?", callback_data="faq_trial")],
        [InlineKeyboardButton("🔙 Home", callback_data="back_start")],
    ])

    try:
        await query.edit_message_text(text=text, reply_markup=keyboard)
    except Exception as e:
        log.error(f"show_faq error: {e}")


_FAQ_ANSWERS = {
    "api": (
        "━━━━━━━━━━━━━━━━━━━━\n"
        "🔑 Twelvedata API Key\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"
        "📌 কোথায় লাগবে?\n"
        "✅ Qutex Signal (Binary)\n"
        "✅ Qutex Premium (Binary)\n"
        "✅ RTX EXNESS (Forex)\n"
        "❌ RTX PRO MAX AI (Crypto) — লাগে না\n\n"
        "📝 কীভাবে পাবো?\n"
        "1️⃣ twelvedata.com ভিজিট\n"
        "2️⃣ Google/Gmail দিয়ে Sign Up\n"
        "3️⃣ Dashboard → API Key copy\n"
        "4️⃣ Bot App → Setting → Paste\n\n"
        "🎁 Free Plan:\n"
        "• 800 API calls/day\n"
        "• 8 calls per minute\n"
        "• সম্পূর্ণ Free (No card)\n\n"
        "⚠️ প্রতিজনের আলাদা key লাগবে!\n"
        "একই key শেয়ার করলে quota\n"
        "দ্রুত শেষ হবে।\n"
        "━━━━━━━━━━━━━━━━━━━━"
    ),
    "safe": (
        "━━━━━━━━━━━━━━━━━━━━\n"
        "🔒 Bot কি Safe?\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"
        "হ্যাঁ, সম্পূর্ণ safe! ✅\n\n"
        "• Official Twelvedata + Binance API\n"
        "• আপনার account এ কোনো access নেই\n"
        "• শুধু signal দিই, trade আপনি করেন\n"
        "• ৫০০+ active users\n"
        "• API key শুধু আপনার device এ save\n\n"
        "━━━━━━━━━━━━━━━━━━━━"
    ),
    "earn": (
        "━━━━━━━━━━━━━━━━━━━━\n"
        "💰 কত Income?\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"
        "আপনার investment ও signal follow\n"
        "করার discipline এর উপর নির্ভর করে।\n\n"
        "⚠️ Trading এ ঝুঁকি আছে\n"
        "⚠️ Guaranteed profit নেই\n\n"
        "💡 Tips:\n"
        "• ছোট amount দিয়ে শুরু\n"
        "• Risk management মেনে চলুন\n"
        "• Free signal দিয়ে test করুন\n\n"
        "━━━━━━━━━━━━━━━━━━━━"
    ),
    "device": (
        "━━━━━━━━━━━━━━━━━━━━\n"
        "📱 কোন Device?\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"
        "সব device এ চলে! ✅\n\n"
        "📱 Android / iPhone\n"
        "💻 PC / Mac\n"
        "🌐 Browser\n\n"
        "শুধু Telegram থাকলেই হবে!\n"
        "━━━━━━━━━━━━━━━━━━━━"
    ),
    "access": (
        "━━━━━━━━━━━━━━━━━━━━\n"
        "⏰ কত সময়ে Access?\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"
        "Payment → TrxID → ৫ মিনিটে! ⚡\n\n"
        "Process:\n"
        "1️⃣ Payment করুন\n"
        "2️⃣ TrxID App এ submit\n"
        "3️⃣ Admin verify\n"
        "4️⃣ ৫ মিনিটে active! ✅\n"
        "━━━━━━━━━━━━━━━━━━━━"
    ),
    "refund": (
        "━━━━━━━━━━━━━━━━━━━━\n"
        "🔄 Refund Policy\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"
        "⚠️ কোনো Refund নেই।\n\n"
        "কেনার আগে:\n"
        "✅ Free signal try করুন\n"
        "✅ Channel এ proof দেখুন\n"
        "✅ তারপর decision নিন\n"
        "━━━━━━━━━━━━━━━━━━━━"
    ),
    "promo": (
        "━━━━━━━━━━━━━━━━━━━━\n"
        "🎁 Promo Code Guide\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"
        "🔑 Code: RTX4241\n\n"
        "✅ কোথায় কাজ করে?\n"
        "• Qutex Signal: 1500 → 1000tk\n"
        "• Qutex Premium: 3000 → 2000tk\n\n"
        "❌ কোথায় কাজ করে না?\n"
        "• RTX EXNESS (8000tk fixed)\n"
        "• RTX PRO MAX AI (5000tk fixed)\n\n"
        "📌 কীভাবে use:\n"
        "1️⃣ App এ Buy Premium\n"
        "2️⃣ Promo field → RTX4241\n"
        "3️⃣ Discount apply ✅\n"
        "━━━━━━━━━━━━━━━━━━━━"
    ),
    "payment": (
        "━━━━━━━━━━━━━━━━━━━━\n"
        "💳 Payment Guide\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"
        "📱 bKash: 01725218874\n"
        "📱 Nagad: 01725218874\n\n"
        "📌 Steps:\n"
        "1️⃣ Send Money করুন\n"
        "   (Payment না, Send Money!)\n"
        "2️⃣ TrxID SMS থেকে copy\n"
        "3️⃣ App এ TrxID paste\n"
        "4️⃣ Submit\n"
        "5️⃣ ৫ মিনিটে Access ✅\n\n"
        "সমস্যায়: @ratulhossain56\n"
        "━━━━━━━━━━━━━━━━━━━━"
    ),
    "trial": (
        "━━━━━━━━━━━━━━━━━━━━\n"
        "🆓 Free Signal Available!\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"
        "📈 Qutex Signal: দৈনিক ৩টি\n"
        "💎 Qutex Premium: দৈনিক ৩টি\n"
        "💹 RTX EXNESS: দৈনিক ৫টি\n"
        "🪙 RTX PRO MAX AI: দৈনিক ২টি\n\n"
        "🎁 মোট ১৩টি Free Signal/day!\n"
        "আগে Free try করুন 🚀\n"
        "━━━━━━━━━━━━━━━━━━━━"
    ),
}


async def handle_faq_answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """FAQ answer show"""
    query = update.callback_query
    await query.answer()

    key = query.data.replace("faq_", "")
    answer = _FAQ_ANSWERS.get(key, "দুঃখিত, answer পাওয়া যাচ্ছে না।")

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("❓ আরো FAQ", callback_data="faq")],
        [InlineKeyboardButton("🎯 Sales Bot", url="https://t.me/rtxearn2_bot")],
        [InlineKeyboardButton("👨‍💼 Support", url=f"https://t.me/{SUPPORT_USERNAME.lstrip('@')}")],
        [InlineKeyboardButton("🏠 Home", callback_data="back_start")],
    ])

    try:
        await query.edit_message_text(text=answer, reply_markup=keyboard)
    except Exception as e:
        log.error(f"handle_faq_answer error: {e}")


# ═══════════════════════════════════════
# Support Handler
# ═══════════════════════════════════════

async def show_support(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Support info"""
    query = update.callback_query
    await query.answer()

    clean_wa = WHATSAPP_NUMBER.lstrip("0")

    text = (
        "━━━━━━━━━━━━━━━━━━━━\n"
        "👨‍💼 RTX Support Team\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"
        f"💬 Telegram: {SUPPORT_USERNAME}\n"
        f"📞 WhatsApp: {WHATSAPP_NUMBER}\n\n"
        "👥 Group: @ratulhossain424\n"
        "📢 Channel: @ratulhossain4241\n\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "⏰ Response: ৫-৩০ মিনিট\n"
        "✅ ২৪/২৪ Available\n"
        "🌟 Fast Solution\n"
        "━━━━━━━━━━━━━━━━━━━━"
    )

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("💬 Telegram Admin", url=f"https://t.me/{SUPPORT_USERNAME.lstrip('@')}")],
        [InlineKeyboardButton("📞 WhatsApp", url=f"https://wa.me/880{clean_wa}")],
        [InlineKeyboardButton("🎯 Sales Bot", url="https://t.me/rtxearn2_bot")],
        [InlineKeyboardButton("🏠 Home", callback_data="back_start")],
    ])

    try:
        await query.edit_message_text(text=text, reply_markup=keyboard)
    except Exception as e:
        log.error(f"show_support error: {e}")


# ═══════════════════════════════════════
# Payment Help
# ═══════════════════════════════════════

async def help_payment(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Payment help menu"""
    query = update.callback_query
    await query.answer()

    text = (
        "━━━━━━━━━━━━━━━━━━━━\n"
        "🆘 Payment Help\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"
        "কোন সমস্যা হচ্ছে? 👇\n"
        "━━━━━━━━━━━━━━━━━━━━"
    )

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("📱 bKash Guide", callback_data="help_bkash")],
        [InlineKeyboardButton("🔑 TrxID কোথায়?", callback_data="help_trxid")],
        [InlineKeyboardButton("⏰ Approve হচ্ছে না", callback_data="help_approve")],
        [InlineKeyboardButton("🎁 Promo কাজ করছে না", callback_data="help_promo")],
        [InlineKeyboardButton("🔑 API Key সমস্যা", callback_data="help_api")],
        [InlineKeyboardButton("👨‍💼 Admin Contact", url=f"https://t.me/{SUPPORT_USERNAME.lstrip('@')}")],
        [InlineKeyboardButton("🏠 Home", callback_data="back_start")],
    ])

    try:
        await query.edit_message_text(text=text, reply_markup=keyboard)
    except Exception as e:
        log.error(f"help_payment error: {e}")


_HELP_ANSWERS = {
    "bkash": (
        "━━━━━━━━━━━━━━━━━━━━\n"
        "📱 bKash Guide\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"
        f"1️⃣ bKash App → Send Money\n"
        f"2️⃣ Number: {BKASH_NUMBER}\n"
        f"3️⃣ Amount দিন\n"
        f"4️⃣ Reference: RTX\n"
        f"5️⃣ PIN → Send\n\n"
        "⚠️ 'Send Money' করুন, 'Payment' না!\n"
        "━━━━━━━━━━━━━━━━━━━━"
    ),
    "trxid": (
        "━━━━━━━━━━━━━━━━━━━━\n"
        "🔑 TrxID কোথায়?\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"
        "Payment SMS এ আসবে:\n"
        "'...TrxID: 8B7X9K2M3P...'\n\n"
        "এটা copy করে App এ paste ✅\n"
        "━━━━━━━━━━━━━━━━━━━━"
    ),
    "approve": (
        "━━━━━━━━━━━━━━━━━━━━\n"
        "⏰ Approve হচ্ছে না?\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"
        "সাধারণত ৫ মিনিটে হয়।\n"
        "১০ মিনিটেও না হলে:\n\n"
        f"👨‍💼 TrxID সহ {SUPPORT_USERNAME} কে জানান\n"
        "দ্রুত solution পাবেন ইনশাআল্লাহ ✅\n"
        "━━━━━━━━━━━━━━━━━━━━"
    ),
    "promo": (
        "━━━━━━━━━━━━━━━━━━━━\n"
        "🎁 Promo Help\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"
        f"Code: {PROMO_CODE} (Capital letters)\n\n"
        "⚠️ কোথায় কাজ করে না:\n"
        "❌ RTX EXNESS (8000tk fixed)\n"
        "❌ RTX PRO MAX AI (5000tk fixed)\n\n"
        "✅ কোথায় কাজ করে:\n"
        "✅ Qutex Signal\n"
        "✅ Qutex Premium\n"
        "━━━━━━━━━━━━━━━━━━━━"
    ),
    "api": (
        "━━━━━━━━━━━━━━━━━━━━\n"
        "🔑 API Key Problem?\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"
        "📝 সঠিক নিয়ম:\n"
        f"1️⃣ {TWELVEDATA_SITE} ভিজিট\n"
        "2️⃣ Google/Gmail দিয়ে Sign Up\n"
        "3️⃣ Dashboard → API Key\n"
        "4️⃣ Copy → App Setting → Paste\n"
        "5️⃣ Save\n\n"
        "⚠️ Common mistakes:\n"
        "• Extra space paste করা\n"
        "• Wrong key copy\n"
        "• Save না করা\n\n"
        f"সমস্যায়: {SUPPORT_USERNAME}\n"
        "━━━━━━━━━━━━━━━━━━━━"
    ),
}


async def help_details(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Help detail answer"""
    query = update.callback_query
    await query.answer()

    key = query.data.replace("help_", "")
    answer = _HELP_ANSWERS.get(key, f"সমস্যায় Admin কে জানান: {SUPPORT_USERNAME}")

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("👨‍💼 Admin", url=f"https://t.me/{SUPPORT_USERNAME.lstrip('@')}")],
        [InlineKeyboardButton("🆘 আরো Help", callback_data="help_payment")],
        [InlineKeyboardButton("🏠 Home", callback_data="back_start")],
    ])

    try:
        await query.edit_message_text(text=answer, reply_markup=keyboard)
    except Exception as e:
        log.error(f"help_details error: {e}")


# ═══════════════════════════════════════
# Back to Start
# ═══════════════════════════════════════

async def back_to_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Home এ ফেরত"""
    from handlers.start import start_command
    await start_command(update, context)
