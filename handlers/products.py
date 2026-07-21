# ═══════════════════════════════════════
# Product Handlers
# ═══════════════════════════════════════

import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from data.products import PRODUCTS

log = logging.getLogger(__name__)


async def show_all_products(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    text = (
        "━━━━━━━━━━━━━━━━━━━━\n"
        "💎 RTX Signal Bot ৩টি:\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"
    )

    for product in PRODUCTS.values():
        promo = ""
        if product["promo_price"]:
            promo = f"🎁 Promo: {product['promo_price']:,}tk ({product['promo_code']})\n"

        text += (
            f"{product['badge']} {product['name']}\n"
            f"   🤖 {product['username']}\n"
            f"   💰 Price: {product['price']:,}tk\n"
            f"   {promo}"
            f"   📊 {product['type']}\n"
            f"━━━━━━━━━━━━━━━━━━━━\n\n"
        )

    text += "বিস্তারিত দেখতে নিচে click করুন 👇"

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("🥉 Qutex Signal", callback_data="detail_bot1")],
        [InlineKeyboardButton("🥈 Qutex Premium", callback_data="detail_bot2")],
        [InlineKeyboardButton("🥇 RTX PRO MAX AI", callback_data="detail_bot3")],
        [InlineKeyboardButton("🔙 Back", callback_data="back_start")],
    ])

    try:
        await query.edit_message_text(text=text, reply_markup=keyboard)
    except Exception as e:
        log.error(f"show_all_products error: {e}")


async def show_product_detail(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    bot_key = query.data.replace("detail_", "")
    product = PRODUCTS.get(bot_key)
    if not product:
        return

    features = "\n".join(f"  ✅ {f}" for f in product["features"])

    strategies = ""
    if "strategies" in product:
        strategies = "\n🎯 Strategy Modes:\n"
        for i, s in enumerate(product["strategies"], 1):
            strategies += f"  {i}. {s['emoji']} {s['name']} — {s['desc']}\n"

    if product["promo_price"]:
        price_text = (
            f"💰 Price: {product['price']:,}tk\n"
            f"🎁 Promo ({product['promo_code']}): {product['promo_price']:,}tk\n"
            f"💵 Save: {product['price'] - product['promo_price']:,}tk!"
        )
        buy_label = f"🛒 কিনুন — {product['promo_price']:,}tk"
    else:
        price_text = (
            f"💰 Price: {product['price']:,}tk (Fixed)\n"
            f"⚠️ কোনো Promo নেই"
        )
        buy_label = f"🛒 কিনুন — {product['price']:,}tk"

    text = (
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"{product['badge']} {product['name']}\n"
        f"━━━━━━━━━━━━━━━━━━━━\n\n"
        f"🤖 Bot: {product['username']}\n"
        f"📊 Type: {product['type']}\n"
        f"📡 Data: {product['data_source']}\n"
        f"⭐ Best for: {product['best_for']}\n\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"ℹ️ কীভাবে কাজ করে:\n\n"
        f"{product['how_it_works']}\n\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"✨ Features:\n\n"
        f"{features}\n"
        f"{strategies}\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"📊 Free vs Premium:\n"
        f"  Free: দৈনিক {product['free_signals']}টি\n"
        f"  Premium: {product['premium_signals']}\n\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"{price_text}\n\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"📸 Proof: @ratulhossain4241\n"
        f"━━━━━━━━━━━━━━━━━━━━"
    )

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton(buy_label, callback_data=f"buy_{bot_key}")],
        [InlineKeyboardButton("📱 Open App", url=product["mini_app"])],
        [InlineKeyboardButton("🎬 Proof/Demo", url="https://t.me/ratulhossain4241")],
        [InlineKeyboardButton("❓ প্রশ্ন করুন", callback_data="faq")],
        [InlineKeyboardButton("🔙 Back", callback_data="products")],
    ])

    try:
        await query.edit_message_text(text=text, reply_markup=keyboard)
    except Exception as e:
        log.error(f"show_product_detail error: {e}")


async def show_price_list(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    text = (
        "━━━━━━━━━━━━━━━━━━━━\n"
        "💰 RTX Price List\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"
        "🥉 Qutex Signal 📊\n"
        "   🤖 @qutex4241pro_bot\n"
        "   Normal: 1,500tk\n"
        "   🎁 Promo (RTX4241): 1,000tk\n"
        "   ✅ Save: 500tk\n\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"
        "🥈 Qutex Premium 📊💵\n"
        "   🤖 @qutexperiyam_bot\n"
        "   Normal: 3,000tk\n"
        "   🎁 Promo (RTX4241): 2,000tk\n"
        "   ✅ Save: 1,000tk\n\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"
        "🥇 RTX PRO MAX AI 🚀\n"
        "   🤖 @rtxpromaxai4241_bot\n"
        "   Price: 5,000tk (Fixed)\n"
        "   ⚠️ Promo নেই\n\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"
        "💳 Payment:\n"
        "   📱 bKash: 01344594241\n"
        "   📱 Nagad: 01344594241\n\n"
        "━━━━━━━━━━━━━━━━━━━━"
    )

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("🛒 Qutex Signal — 1,000tk", callback_data="buy_bot1")],
        [InlineKeyboardButton("🛒 Qutex Premium — 2,000tk", callback_data="buy_bot2")],
        [InlineKeyboardButton("🛒 RTX PRO MAX AI — 5,000tk", callback_data="buy_bot3")],
        [InlineKeyboardButton("🔙 Back", callback_data="back_start")],
    ])

    try:
        await query.edit_message_text(text=text, reply_markup=keyboard)
    except Exception as e:
        log.error(f"show_price_list error: {e}")


async def show_promo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    text = (
        "━━━━━━━━━━━━━━━━━━━━\n"
        "🎁 Special Promo Code!\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"
        "🔑 Code: RTX4241\n\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"
        "🥉 Qutex Signal:\n"
        "   1,500tk → 1,000tk (Save 500tk!)\n"
        "   🤖 @qutex4241pro_bot\n\n"
        "🥈 Qutex Premium:\n"
        "   3,000tk → 2,000tk (Save 1,000tk!)\n"
        "   🤖 @qutexperiyam_bot\n\n"
        "🥇 RTX PRO MAX AI:\n"
        "   5,000tk Fixed ⚠️ (Promo নেই)\n"
        "   🤖 @rtxpromaxai4241_bot\n\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"
        "📌 কীভাবে ব্যবহার করবেন:\n\n"
        "1️⃣ App Open করুন\n"
        "2️⃣ Buy Premium click করুন\n"
        "3️⃣ Code দিন: RTX4241\n"
        "4️⃣ Discount apply হবে ✅\n"
        "5️⃣ Payment করুন\n\n"
        "━━━━━━━━━━━━━━━━━━━━"
    )

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("🛒 এখনই কিনুন", callback_data="products")],
        [InlineKeyboardButton("🔙 Back", callback_data="back_start")],
    ])

    try:
        await query.edit_message_text(text=text, reply_markup=keyboard)
    except Exception as e:
        log.error(f"show_promo error: {e}")
