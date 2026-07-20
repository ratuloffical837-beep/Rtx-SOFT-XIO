# ═══════════════════════════════════════
# All Button Click (Callback) Handlers
# ═══════════════════════════════════════

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from data.products import PRODUCTS
from config import SUPPORT_USERNAME, BKASH_NUMBER, WHATSAPP_NUMBER


async def buy_product(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Buy button click করলে step-by-step guide"""
    
    query = update.callback_query
    await query.answer()
    
    bot_key = query.data.replace("buy_", "")
    product = PRODUCTS.get(bot_key)
    
    if not product:
        return
    
    # Price determine
    if product["promo_price"]:
        price = product["promo_price"]
        price_text = (
            f"💰 Amount: {price:,}tk\n"
            f"   (Promo Code: {product['promo_code']})\n"
            f"💰 অথবা {product['price']:,}tk (without promo)"
        )
    else:
        price = product["price"]
        price_text = f"💰 Amount: {price:,}tk"
    
    text = (
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"🎉 চমৎকার সিদ্ধান্ত!\n"
        f"━━━━━━━━━━━━━━━━━━━━\n\n"
        f"{product['badge']} {product['name']} কিনতে\n"
        f"নিচের steps follow করুন:\n\n"
        f"━━━━━━━━━━━━━━━━━━━━\n\n"
        f"📌 STEP 1: App খুলুন\n"
        f"নিচের 'Open App' button এ click করুন\n\n"
        f"━━━━━━━━━━━━━━━━━━━━\n\n"
        f"📌 STEP 2: App এ ঢুকে\n"
        f"'Buy Premium' এ click করুন\n\n"
        f"━━━━━━━━━━━━━━━━━━━━\n\n"
        f"📌 STEP 3: Payment করুন\n\n"
        f"📱 bKash: {BKASH_NUMBER} (Send Money)\n"
        f"📱 Nagad: {BKASH_NUMBER} (Send Money)\n\n"
        f"{price_text}\n\n"
        f"━━━━━━━━━━━━━━━━━━━━\n\n"
        f"📌 STEP 4: bKash/Nagad এ\n"
        f"  1. Send Money select\n"
        f"  2. Number: {BKASH_NUMBER}\n"
        f"  3. Amount: {price}\n"
        f"  4. Reference: {product['name'].split()[0]}\n"
        f"  5. PIN দিয়ে Send\n\n"
        f"━━━━━━━━━━━━━━━━━━━━\n\n"
        f"📌 STEP 5: Transaction ID\n"
        f"  SMS থেকে TrxID copy করুন\n"
        f"  App এ paste করুন\n"
    )
    
    if product["promo_code"]:
        text += (
            f"\n📌 STEP 6: Promo Code\n"
            f"  Code: {product['promo_code']}\n"
            f"  App এ Promo field এ paste করুন\n"
        )
    
    text += (
        f"\n━━━━━━━━━━━━━━━━━━━━\n\n"
        f"📌 LAST STEP: Submit করুন\n"
        f"  ⏰ 5 মিনিটে Approve হবে!\n"
        f"  ✅ Access instantly পাবেন!\n\n"
        f"━━━━━━━━━━━━━━━━━━━━\n\n"
        f"🆘 সমস্যা হলে:\n"
        f"👨‍💼 Admin: {SUPPORT_USERNAME}\n"
        f"📞 WhatsApp: {WHATSAPP_NUMBER}\n"
        f"━━━━━━━━━━━━━━━━━━━━"
    )
    
    keyboard = [
        [InlineKeyboardButton("🚀 Open App", url=product["mini_app"])],
        [InlineKeyboardButton("🆘 সমস্যা হচ্ছে", callback_data="help_payment")],
        [InlineKeyboardButton("👨‍💼 Admin Contact", url=f"https://t.me/{SUPPORT_USERNAME.replace('@', '')}")],
        [InlineKeyboardButton("🔙 Products", callback_data="products")],
    ]
    
    await query.edit_message_text(
        text=text,
        reply_markup=InlineKeyboardMarkup(keyboard),
    )


async def show_demo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Demo/proof channel এ পাঠায়"""
    
    query = update.callback_query
    await query.answer()
    
    text = (
        "━━━━━━━━━━━━━━━━━━━━\n"
        "🎬 Demo & Live Proof\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"
        "আমাদের Channel এ পাবেন:\n\n"
        "📸 Bot Screenshots\n"
        "🎬 Video Tutorials\n"
        "📈 Live Signal Results\n"
        "⭐ Customer Reviews\n"
        "📊 Daily Updates\n\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"
        "👇 Channel visit করুন:\n"
        "━━━━━━━━━━━━━━━━━━━━"
    )
    
    keyboard = [
        [InlineKeyboardButton("📢 RTX Channel", url="https://t.me/ratulhossain4241")],
        [InlineKeyboardButton("🔙 Back", callback_data="back_start")],
    ]
    
    await query.edit_message_text(
        text=text,
        reply_markup=InlineKeyboardMarkup(keyboard),
    )


async def show_faq(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """FAQ list দেখায়"""
    
    query = update.callback_query
    await query.answer()
    
    text = (
        "━━━━━━━━━━━━━━━━━━━━\n"
        "❓ Frequently Asked Questions\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"
        "নিচের যেকোনো প্রশ্নে click করুন\n"
        "অথবা নিজে প্রশ্ন লিখে পাঠান! 🙏\n\n"
        "━━━━━━━━━━━━━━━━━━━━"
    )
    
    keyboard = [
        [InlineKeyboardButton("🔒 Bot কি safe?", callback_data="faq_safe")],
        [InlineKeyboardButton("💰 কতটুকু earn করা যায়?", callback_data="faq_earn")],
        [InlineKeyboardButton("📱 কোন device এ চলে?", callback_data="faq_device")],
        [InlineKeyboardButton("⏰ কত সময়ে access পাব?", callback_data="faq_access")],
        [InlineKeyboardButton("🔄 Refund policy?", callback_data="faq_refund")],
        [InlineKeyboardButton("📅 Renewal কীভাবে?", callback_data="faq_renewal")],
        [InlineKeyboardButton("🆓 Free trial আছে?", callback_data="faq_trial")],
        [InlineKeyboardButton("🔙 Back", callback_data="back_start")],
    ]
    
    await query.edit_message_text(
        text=text,
        reply_markup=InlineKeyboardMarkup(keyboard),
    )


async def handle_faq_answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """FAQ button এর answer দেয়"""
    
    query = update.callback_query
    await query.answer()
    
    faq_key = query.data.replace("faq_", "")
    
    answers = {
        "safe": (
            "━━━━━━━━━━━━━━━━━━━━\n"
            "🔒 Bot কি Safe?\n"
            "━━━━━━━━━━━━━━━━━━━━\n\n"
            "হ্যাঁ, সম্পূর্ণ safe! ✅\n\n"
            "• আমরা Twelvedata ও Binance এর\n"
            "  official API use করি\n"
            "• Real market data থেকে signal\n"
            "• আপনার trading account এ \n"
            "  আমাদের কোনো access নেই\n"
            "• শুধু signal দিই, trade আপনি করেন\n"
            "• 500+ active user ব্যবহার করছেন\n\n"
            "━━━━━━━━━━━━━━━━━━━━"
        ),
        "earn": (
            "━━━━━━━━━━━━━━━━━━━━\n"
            "💰 কতটুকু Earn করা যায়?\n"
            "━━━━━━━━━━━━━━━━━━━━\n\n"
            "এটা আপনার investment ও \n"
            "signal follow করার উপর নির্ভর করে।\n\n"
            "⚠️ Important:\n"
            "• Trading ঝুঁকিপূর্ণ\n"
            "• 100% guaranteed profit নেই\n"
            "• আমরা accurate signal দিই\n"
            "• বাকিটা market এর উপর নির্ভর করে\n\n"
            "💡 Tips:\n"
            "• ছোট amount দিয়ে শুরু করুন\n"
            "• Signal সঠিকভাবে follow করুন\n"
            "• Money management মেনে চলুন\n\n"
            "━━━━━━━━━━━━━━━━━━━━"
        ),
        "device": (
            "━━━━━━━━━━━━━━━━━━━━\n"
            "📱 কোন Device এ চলে?\n"
            "━━━━━━━━━━━━━━━━━━━━\n\n"
            "সকল device এ কাজ করে! ✅\n\n"
            "📱 Android Phone\n"
            "📱 iPhone (iOS)\n"
            "💻 Windows PC\n"
            "💻 Mac\n"
            "🌐 Web Browser\n\n"
            "শুধু Telegram install থাকলেই হবে! 🎉\n\n"
            "━━━━━━━━━━━━━━━━━━━━"
        ),
        "access": (
            "━━━━━━━━━━━━━━━━━━━━\n"
            "⏰ কত সময়ে Access পাব?\n"
            "━━━━━━━━━━━━━━━━━━━━\n\n"
            "Payment করার ৫ মিনিটের মধ্যে\n"
            "access পেয়ে যাবেন! ⚡\n\n"
            "📌 Process:\n"
            "1. Payment করুন\n"
            "2. TrxID submit করুন\n"
            "3. Admin verify করবে\n"
            "4. 5 min এ access active! ✅\n\n"
            "━━━━━━━━━━━━━━━━━━━━"
        ),
        "refund": (
            "━━━━━━━━━━━━━━━━━━━━\n"
            "🔄 Refund Policy\n"
            "━━━━━━━━━━━━━━━━━━━━\n\n"
            "⚠️ কোনো Refund নেই।\n\n"
            "কারণ:\n"
            "• Trading নিজেই ঝুঁকিপূর্ণ\n"
            "• Signal purchase এ refund apply হয় না\n"
            "• আমরা accurate signal দিই\n"
            "• Market movement guaranteed না\n\n"
            "💡 Suggestion:\n"
            "• কেনার আগে free signal try করুন\n"
            "• Channel এ proof দেখুন\n"
            "• তারপর decision নিন\n\n"
            "━━━━━━━━━━━━━━━━━━━━"
        ),
        "renewal": (
            "━━━━━━━━━━━━━━━━━━━━\n"
            "📅 Renewal কীভাবে?\n"
            "━━━━━━━━━━━━━━━━━━━━\n\n"
            "Monthly subscription:\n\n"
            "• 30 দিন পর expire হবে\n"
            "• Renew করতে আবার payment করুন\n"
            "• Same process follow করুন\n"
            "• 5 min এ আবার active! ✅\n\n"
            "━━━━━━━━━━━━━━━━━━━━"
        ),
        "trial": (
            "━━━━━━━━━━━━━━━━━━━━\n"
            "🆓 Free Trial আছে?\n"
            "━━━━━━━━━━━━━━━━━━━━\n\n"
            "হ্যাঁ! Free signal আছে! 🎉\n\n"
            "🥉 Qutex Signal: দৈনিক 3টি free\n"
            "🥈 Qutex Premium: দৈনিক 3টি free\n"
            "🥇 RTX PRO MAX AI: দৈনিক 2টি free\n\n"
            "📌 আগে free signal try করুন!\n"
            "পছন্দ হলে premium নিন।\n\n"
            "━━━━━━━━━━━━━━━━━━━━"
        ),
    }
    
    answer = answers.get(faq_key, "দুঃখিত, এই answer পাওয়া যাচ্ছে না।")
    
    keyboard = [
        [InlineKeyboardButton("❓ আরো FAQ", callback_data="faq")],
        [InlineKeyboardButton("📦 Products", callback_data="products")],
        [InlineKeyboardButton("🔙 Home", callback_data="back_start")],
    ]
    
    await query.edit_message_text(
        text=answer,
        reply_markup=InlineKeyboardMarkup(keyboard),
    )


async def show_support(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Support info দেখায়"""
    
    query = update.callback_query
    await query.answer()
    
    text = (
        "━━━━━━━━━━━━━━━━━━━━\n"
        "👨‍💼 RTX Support\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"
        "যেকোনো সমস্যায় যোগাযোগ করুন:\n\n"
        f"💬 Telegram: {SUPPORT_USERNAME}\n"
        f"📞 WhatsApp: {WHATSAPP_NUMBER}\n\n"
        "👥 Community Group:\n"
        "   @ratulhossain424\n\n"
        "📢 Channel:\n"
        "   @ratulhossain4241\n\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "⏰ Response Time: 5-30 মিনিট\n"
        "━━━━━━━━━━━━━━━━━━━━"
    )
    
    keyboard = [
        [InlineKeyboardButton(f"💬 Message Admin", url=f"https://t.me/{SUPPORT_USERNAME.replace('@', '')}")],
        [InlineKeyboardButton(f"📞 WhatsApp", url=f"https://wa.me/88{WHATSAPP_NUMBER}")],
        [InlineKeyboardButton("🔙 Back", callback_data="back_start")],
    ]
    
    await query.edit_message_text(
        text=text,
        reply_markup=InlineKeyboardMarkup(keyboard),
    )


async def help_payment(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Payment সমস্যা help"""
    
    query = update.callback_query
    await query.answer()
    
    text = (
        "━━━━━━━━━━━━━━━━━━━━\n"
        "🆘 Payment Help\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"
        "সমস্যা কোথায় হচ্ছে?\n\n"
        "━━━━━━━━━━━━━━━━━━━━"
    )
    
    keyboard = [
        [InlineKeyboardButton("📱 bKash এ Send Money হচ্ছে না", callback_data="help_bkash")],
        [InlineKeyboardButton("🔑 TrxID কোথায় পাব?", callback_data="help_trxid")],
        [InlineKeyboardButton("⏰ Approve হচ্ছে না", callback_data="help_approve")],
        [InlineKeyboardButton("🎁 Promo Code কাজ করছে না", callback_data="help_promo")],
        [InlineKeyboardButton(f"👨‍💼 Admin কে বলুন", url=f"https://t.me/{SUPPORT_USERNAME.replace('@', '')}")],
        [InlineKeyboardButton("🔙 Back", callback_data="back_start")],
    ]
    
    await query.edit_message_text(
        text=text,
        reply_markup=InlineKeyboardMarkup(keyboard),
    )


async def help_details(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Specific help answers"""
    
    query = update.callback_query
    await query.answer()
    
    help_key = query.data.replace("help_", "")
    
    answers = {
        "bkash": (
            "━━━━━━━━━━━━━━━━━━━━\n"
            "📱 bKash Send Money Guide\n"
            "━━━━━━━━━━━━━━━━━━━━\n\n"
            "1️⃣ bKash app খুলুন\n"
            "2️⃣ 'Send Money' select\n"
            "3️⃣ Number: 01344594241\n"
            "4️⃣ Amount দিন\n"
            "5️⃣ Reference: RTX\n"
            "6️⃣ PIN দিন → Send\n\n"
            "⚠️ 'Send Money' NOT 'Payment'\n"
            "━━━━━━━━━━━━━━━━━━━━"
        ),
        "trxid": (
            "━━━━━━━━━━━━━━━━━━━━\n"
            "🔑 TrxID কোথায় পাবেন?\n"
            "━━━━━━━━━━━━━━━━━━━━\n\n"
            "Payment করার পর bKash/Nagad\n"
            "থেকে SMS আসবে:\n\n"
            "📩 SMS Example:\n"
            "'...TrxID: 8B7X9K2M3P...'\n\n"
            "এই TrxID টা copy করুন\n"
            "App এ paste করুন ✅\n\n"
            "━━━━━━━━━━━━━━━━━━━━"
        ),
        "approve": (
            "━━━━━━━━━━━━━━━━━━━━\n"
            "⏰ Approve হচ্ছে না?\n"
            "━━━━━━━━━━━━━━━━━━━━\n\n"
            "সাধারণত 5 মিনিটে approve হয়।\n\n"
            "যদি 10 মিনিটেও না হয়:\n\n"
            f"👨‍💼 Admin কে contact করুন:\n"
            f"   {SUPPORT_USERNAME}\n"
            f"📞 WhatsApp: {WHATSAPP_NUMBER}\n\n"
            "TrxID ও amount বলুন।\n\n"
            "━━━━━━━━━━━━━━━━━━━━"
        ),
        "promo": (
            "━━━━━━━━━━━━━━━━━━━━\n"
            "🎁 Promo Code Help\n"
            "━━━━━━━━━━━━━━━━━━━━\n\n"
            "Promo Code: RTX4241\n\n"
            "📌 সঠিক ভাবে লিখুন:\n"
            "  R-T-X-4-2-4-1 (Capital letters)\n\n"
            "⚠️ RTX PRO MAX AI তে\n"
            "  promo কাজ করবে না\n"
            "  (5000tk fixed)\n\n"
            f"সমস্যা? Admin: {SUPPORT_USERNAME}\n\n"
            "━━━━━━━━━━━━━━━━━━━━"
        ),
    }
    
    answer = answers.get(help_key, "Admin কে contact করুন।")
    
    keyboard = [
        [InlineKeyboardButton(f"👨‍💼 Admin", url=f"https://t.me/{SUPPORT_USERNAME.replace('@', '')}")],
        [InlineKeyboardButton("🔙 Back", callback_data="back_start")],
    ]
    
    await query.edit_message_text(
        text=answer,
        reply_markup=InlineKeyboardMarkup(keyboard),
    )


async def back_to_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Home screen এ ফিরে যায়"""
    
    query = update.callback_query
    await query.answer()
    
    user = query.from_user
    first_name = user.first_name or "ভাই"
    
    text = (
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"🌟 RTX Trading Signal 🌟\n"
        f"━━━━━━━━━━━━━━━━━━━━\n\n"
        f"কী করতে চান {first_name} ভাই? 👇\n\n"
        f"━━━━━━━━━━━━━━━━━━━━"
    )
    
    keyboard = [
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
    ]
    
    await query.edit_message_text(
        text=text,
        reply_markup=InlineKeyboardMarkup(keyboard),
  )
