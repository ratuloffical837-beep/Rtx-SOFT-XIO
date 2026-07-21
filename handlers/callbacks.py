# ═══════════════════════════════════════
# All Callback (Button) Handlers
# ═══════════════════════════════════════

import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from data.products import PRODUCTS
from config import (
    SUPPORT_USERNAME, BKASH_NUMBER, NAGAD_NUMBER,
    WHATSAPP_NUMBER, PROMO_CODE,
)

log = logging.getLogger(__name__)


def _back_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🔙 Home", callback_data="back_start")],
    ])


def _support_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton(
            "👨‍💼 Admin Contact",
            url=f"https://t.me/{SUPPORT_USERNAME.lstrip('@')}"
        )],
        [InlineKeyboardButton("🔙 Back", callback_data="back_start")],
    ])


async def buy_product(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    bot_key = query.data.replace("buy_", "")
    product = PRODUCTS.get(bot_key)
    if not product:
        return

    if product["promo_price"]:
        price = product["promo_price"]
        price_text = (
            f"💰 Amount: {price:,}tk\n"
            f"   (Promo: {product['promo_code']} apply করুন)\n"
            f"   বা {product['price']:,}tk (without promo)"
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

    text = (
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"🎉 চমৎকার সিদ্ধান্ত!\n"
        f"━━━━━━━━━━━━━━━━━━━━\n\n"
        f"{product['badge']} {product['name']}\n"
        f"🤖 {product['username']}\n\n"
        f"━━━━━━━━━━━━━━━━━━━━\n\n"
        f"📌 STEP 1:\n"
        f"নিচে 'Open App' click করুন\n\n"
        f"📌 STEP 2:\n"
        f"App এ 'Buy Premium' click করুন\n\n"
        f"📌 STEP 3: Payment করুন\n"
        f"   📱 bKash: {BKASH_NUMBER} (Send Money)\n"
        f"   📱 Nagad: {NAGAD_NUMBER} (Send Money)\n"
        f"   {price_text}\n\n"
        f"📌 STEP 4: TrxID\n"
        f"   SMS থেকে TrxID copy করুন\n"
        f"   App এ paste করুন\n"
        f"{promo_step}"
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
        [InlineKeyboardButton("🔙 Products", callback_data="products")],
    ])

    try:
        await query.edit_message_text(text=text, reply_markup=keyboard)
    except Exception as e:
        log.error(f"buy_product error: {e}")


async def show_demo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    text = (
        "━━━━━━━━━━━━━━━━━━━━\n"
        "🎬 Demo & Proof\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"
        "আমাদের Channel এ পাবেন:\n"
        "📸 Bot Screenshots\n"
        "📈 Live Signal Results\n"
        "⭐ Customer Reviews\n"
        "📊 Daily Updates\n\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"
        "📱 App সরাসরি দেখুন:\n"
        "🥉 @qutex4241pro_bot\n"
        "🥈 @qutexperiyam_bot\n"
        "🥇 @rtxpromaxai4241_bot\n\n"
        "━━━━━━━━━━━━━━━━━━━━"
    )

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("📢 RTX Channel", url="https://t.me/ratulhossain4241")],
        [InlineKeyboardButton("📱 Qutex Signal App", url="https://t.me/qutex4241pro_bot/signalapp")],
        [InlineKeyboardButton("📱 Qutex Premium App", url="https://t.me/qutexperiyam_bot/qutexsignalbot")],
        [InlineKeyboardButton("📱 RTX PRO MAX AI App", url="https://t.me/rtxpromaxai4241_bot/binancesignalbot")],
        [InlineKeyboardButton("🔙 Back", callback_data="back_start")],
    ])

    try:
        await query.edit_message_text(text=text, reply_markup=keyboard)
    except Exception as e:
        log.error(f"show_demo error: {e}")


async def show_faq(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    text = (
        "━━━━━━━━━━━━━━━━━━━━\n"
        "❓ FAQ\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"
        "যেকোনো প্রশ্নে click করুন\n"
        "বা সরাসরি type করে পাঠান!\n\n"
        "━━━━━━━━━━━━━━━━━━━━"
    )

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("🔒 Bot কি safe?", callback_data="faq_safe")],
        [InlineKeyboardButton("💰 কতটুকু earn?", callback_data="faq_earn")],
        [InlineKeyboardButton("📱 কোন device এ চলে?", callback_data="faq_device")],
        [InlineKeyboardButton("⏰ কত সময়ে access?", callback_data="faq_access")],
        [InlineKeyboardButton("🔄 Refund policy?", callback_data="faq_refund")],
        [InlineKeyboardButton("📅 Renewal কীভাবে?", callback_data="faq_renewal")],
        [InlineKeyboardButton("🆓 Free trial আছে?", callback_data="faq_trial")],
        [InlineKeyboardButton("🔙 Back", callback_data="back_start")],
    ])

    try:
        await query.edit_message_text(text=text, reply_markup=keyboard)
    except Exception as e:
        log.error(f"show_faq error: {e}")


_FAQ_ANSWERS = {
    "safe": (
        "━━━━━━━━━━━━━━━━━━━━\n"
        "🔒 Bot কি Safe?\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"
        "হ্যাঁ, সম্পূর্ণ safe! ✅\n\n"
        "• Official Binance + Twelvedata API\n"
        "• আপনার account এ কোনো access নেই\n"
        "• শুধু signal দিই, trade আপনি করেন\n"
        "• ৫০০+ active users\n\n"
        "━━━━━━━━━━━━━━━━━━━━"
    ),
    "earn": (
        "━━━━━━━━━━━━━━━━━━━━\n"
        "💰 কতটুকু Earn?\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"
        "আপনার investment ও signal follow\n"
        "করার উপর নির্ভর করে।\n\n"
        "⚠️ Trading ঝুঁকিপূর্ণ\n"
        "⚠️ Guaranteed profit নেই\n\n"
        "💡 ছোট amount দিয়ে শুরু করুন\n"
        "💡 Risk management মেনে চলুন\n\n"
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
        "শুধু Telegram থাকলেই হবে!\n\n"
        "━━━━━━━━━━━━━━━━━━━━"
    ),
    "access": (
        "━━━━━━━━━━━━━━━━━━━━\n"
        "⏰ কত সময়ে Access?\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"
        "Payment → TrxID submit → ৫ মিনিটে! ⚡\n\n"
        "Process:\n"
        "1. Payment করুন\n"
        "2. TrxID App এ submit করুন\n"
        "3. Admin verify করবেন\n"
        "4. ৫ মিনিটে access active! ✅\n\n"
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
        "✅ তারপর decision নিন\n\n"
        "━━━━━━━━━━━━━━━━━━━━"
    ),
    "renewal": (
        "━━━━━━━━━━━━━━━━━━━━\n"
        "📅 Renewal\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"
        "৩০ দিন পর expire।\n"
        "আবার same process এ payment → ৫ মিনিটে active! ✅\n\n"
        "━━━━━━━━━━━━━━━━━━━━"
    ),
    "trial": (
        "━━━━━━━━━━━━━━━━━━━━\n"
        "🆓 Free Signal!\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"
        "🥉 Qutex Signal: দৈনিক ৩টি free\n"
        "🥈 Qutex Premium: দৈনিক ৩টি free\n"
        "🥇 RTX PRO MAX AI: দৈনিক ২টি free\n\n"
        "আগে free try করুন! 🎉\n\n"
        "━━━━━━━━━━━━━━━━━━━━"
    ),
}

_HELP_ANSWERS = {
    "bkash": (
        "━━━━━━━━━━━━━━━━━━━━\n"
        "📱 bKash Guide\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"
        "1️⃣ bKash App → Send Money\n"
        "2️⃣ Number: 01344594241\n"
        "3️⃣ Amount দিন\n"
        "4️⃣ Reference: RTX\n"
        "5️⃣ PIN → Send\n\n"
        "⚠️ 'Send Money', 'Payment' না!\n"
        "━━━━━━━━━━━━━━━━━━━━"
    ),
    "trxid": (
        "━━━━━━━━━━━━━━━━━━━━\n"
        "🔑 TrxID কোথায়?\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"
        "Payment SMS এ আসবে:\n"
        "'...TrxID: 8B7X9K2M3P...'\n\n"
        "এটা copy → App এ paste ✅\n"
        "━━━━━━━━━━━━━━━━━━━━"
    ),
    "approve": (
        "━━━━━━━━━━━━━━━━━━━━\n"
        "⏰ Approve হচ্ছে না?\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"
        "সাধারণত ৫ মিনিটে হয়।\n"
        "১০ মিনিটেও না হলে:\n\n"
        f"👨‍💼 TrxID সহ Admin কে জানান\n"
        f"━━━━━━━━━━━━━━━━━━━━"
    ),
    "promo": (
        "━━━━━━━━━━━━━━━━━━━━\n"
        "🎁 Promo Help\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"
        "Code: RTX4241 (Capital letters)\n\n"
        "⚠️ RTX PRO MAX AI তে\n"
        "promo কাজ করে না (5000tk fixed)\n\n"
        "━━━━━━━━━━━━━━━━━━━━"
    ),
}


async def handle_faq_answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    key = query.data.replace("faq_", "")
    answer = _FAQ_ANSWERS.get(key, "দুঃখিত, answer পাওয়া যাচ্ছে না।")

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("❓ আরো FAQ", callback_data="faq")],
        [InlineKeyboardButton("📦 Products", callback_data="products")],
        [InlineKeyboardButton("🎯 Sales Bot", url="https://t.me/rtxearn2_bot")],
        [InlineKeyboardButton("🔙 Home", callback_data="back_start")],
    ])

    try:
        await query.edit_message_text(text=answer, reply_markup=keyboard)
    except Exception as e:
        log.error(f"handle_faq_answer error: {e}")


async def show_support(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    text = (
        "━━━━━━━━━━━━━━━━━━━━\n"
        "👨‍💼 RTX Support\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"
        f"💬 Telegram: {SUPPORT_USERNAME}\n"
        f"📞 WhatsApp: {WHATSAPP_NUMBER}\n\n"
        "👥 Group: @ratulhossain424\n"
        "📢 Channel: @ratulhossain4241\n\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "⏰ Response: ৫-৩০ মিনিট\n"
        "✅ ২৪/২৪ Available\n"
        "━━━━━━━━━━━━━━━━━━━━"
    )

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("💬 Admin", url=f"https://t.me/{SUPPORT_USERNAME.lstrip('@')}")],
        [InlineKeyboardButton("📞 WhatsApp", url=f"https://wa.me/88{WHATSAPP_NUMBER}")],
        [InlineKeyboardButton("🔙 Back", callback_data="back_start")],
    ])

    try:
        await query.edit_message_text(text=text, reply_markup=keyboard)
    except Exception as e:
        log.error(f"show_support error: {e}")


async def help_payment(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    text = (
        "━━━━━━━━━━━━━━━━━━━━\n"
        "🆘 Payment Help\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"
        "সমস্যা কোথায়?\n\n"
        "━━━━━━━━━━━━━━━━━━━━"
    )

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("📱 bKash Guide", callback_data="help_bkash")],
        [InlineKeyboardButton("🔑 TrxID কোথায়?", callback_data="help_trxid")],
        [InlineKeyboardButton("⏰ Approve হচ্ছে না", callback_data="help_approve")],
        [InlineKeyboardButton("🎁 Promo কাজ করছে না", callback_data="help_promo")],
        [InlineKeyboardButton("👨‍💼 Admin", url=f"https://t.me/{SUPPORT_USERNAME.lstrip('@')}")],
        [InlineKeyboardButton("🔙 Back", callback_data="back_start")],
    ])

    try:
        await query.edit_message_text(text=text, reply_markup=keyboard)
    except Exception as e:
        log.error(f"help_payment error: {e}")


async def help_details(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    key = query.data.replace("help_", "")
    answer = _HELP_ANSWERS.get(key, f"সমস্যায় Admin কে জানান: {SUPPORT_USERNAME}")

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("👨‍💼 Admin", url=f"https://t.me/{SUPPORT_USERNAME.lstrip('@')}")],
        [InlineKeyboardButton("🔙 Back", callback_data="back_start")],
    ])

    try:
        await query.edit_message_text(text=answer, reply_markup=keyboard)
    except Exception as e:
        log.error(f"help_details error: {e}")


async def back_to_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    user = query.from_user
    first_name = user.first_name or "ভাই"

    text = (
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"🌟 RTX Trading Signal\n"
        f"━━━━━━━━━━━━━━━━━━━━\n\n"
        f"কী করতে চান {first_name} ভাই? 👇\n\n"
        f"━━━━━━━━━━━━━━━━━━━━"
    )

    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("📦 Products", callback_data="products"),
            InlineKeyboardButton("💰 Price", callback_data="price_list"),
        ],
        [
            InlineKeyboardButton("🎁 Promo", callback_data="promo"),
            InlineKeyboardButton("🎬 Demo", callback_data="demo"),
        ],
        [
            InlineKeyboardButton("❓ FAQ", callback_data="faq"),
            InlineKeyboardButton("👨‍💼 Support", callback_data="support"),
        ],
        [
            InlineKeyboardButton("📢 Channel", url="https://t.me/ratulhossain4241"),
            InlineKeyboardButton("👥 Group", url="https://t.me/ratulhossain424"),
        ],
        [
            InlineKeyboardButton("🎯 Sales Bot", url="https://t.me/rtxearn2_bot"),
        ],
    ])

    try:
        await query.edit_message_text(text=text, reply_markup=keyboard)
    except Exception as e:
        log.error(f"back_to_start error: {e}")
