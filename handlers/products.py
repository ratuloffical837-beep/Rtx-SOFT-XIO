# ═══════════════════════════════════════
# Product Details Handlers
# ═══════════════════════════════════════

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from data.products import PRODUCTS


async def show_all_products(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """সব products দেখায়"""
    
    query = update.callback_query
    await query.answer()
    
    text = (
        "━━━━━━━━━━━━━━━━━━━━\n"
        "💎 RTX এর ৩টা Signal Bot:\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"
    )
    
    for key, product in PRODUCTS.items():
        promo_text = ""
        if product["promo_price"]:
            promo_text = f"🎁 Promo ({product['promo_code']}): {product['promo_price']:,}tk\n"
        
        text += (
            f"{product['badge']} {product['name']}\n"
            f"💰 Price: {product['price']:,}tk\n"
            f"{promo_text}"
            f"📊 Type: {product['type']}\n"
            f"⭐ Best for: {product['best_for']}\n"
            f"━━━━━━━━━━━━━━━━━━━━\n\n"
        )
    
    text += "কোনটা সম্পর্কে বিস্তারিত জানতে চান? 👇"
    
    keyboard = [
        [InlineKeyboardButton("🥉 Qutex Signal Details", callback_data="detail_bot1")],
        [InlineKeyboardButton("🥈 Qutex Premium Details", callback_data="detail_bot2")],
        [InlineKeyboardButton("🥇 RTX PRO MAX AI Details", callback_data="detail_bot3")],
        [InlineKeyboardButton("🔙 Back", callback_data="back_start")],
    ]
    
    await query.edit_message_text(
        text=text,
        reply_markup=InlineKeyboardMarkup(keyboard),
    )


async def show_product_detail(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Individual product details দেখায়"""
    
    query = update.callback_query
    await query.answer()
    
    bot_key = query.data.replace("detail_", "")
    product = PRODUCTS.get(bot_key)
    
    if not product:
        return
    
    # Features list
    features_text = ""
    for feature in product["features"]:
        features_text += f"  ✅ {feature}\n"
    
    # Strategies (Bot 3 only)
    strategy_text = ""
    if "strategies" in product:
        strategy_text = "\n🎯 Signal Strategy Modes:\n\n"
        for i, strategy in enumerate(product["strategies"], 1):
            strategy_text += (
                f"  {i}️⃣ {strategy['emoji']} {strategy['name']}\n"
                f"     ⚡ {strategy['desc']}\n\n"
            )
    
    # Price text
    price_text = f"💰 Price: {product['price']:,}tk"
    if product["promo_price"]:
        price_text += (
            f"\n🎁 Promo Code: {product['promo_code']}\n"
            f"💰 Promo Price: {product['promo_price']:,}tk\n"
            f"💵 Save: {product['price'] - product['promo_price']:,}tk!"
        )
    else:
        price_text += "\n⚠️ কোনো Promo Code নেই (Fixed Price)"
    
    text = (
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"{product['badge']} {product['name']}\n"
        f"━━━━━━━━━━━━━━━━━━━━\n\n"
        f"📊 Type: {product['type']}\n"
        f"📡 Data: {product['data_source']}\n\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"📊 কীভাবে কাজ করে:\n\n"
        f"{product['how_it_works']}\n\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"✨ Features:\n\n"
        f"{features_text}\n"
        f"{strategy_text}"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"📊 Free vs Premium:\n\n"
        f"  Free: দৈনিক {product['free_signals']}টি Signal\n"
        f"  Premium: {product['premium_signals']} Signal\n\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"{price_text}\n\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"📸 Live Proof দেখুন:\n"
        f"👉 @ratulhossain4241\n"
        f"━━━━━━━━━━━━━━━━━━━━"
    )
    
    # Buy button
    buy_text = f"🛒 কিনুন"
    if product["promo_price"]:
        buy_text += f" - {product['promo_price']:,}tk"
    else:
        buy_text += f" - {product['price']:,}tk"
    
    keyboard = [
        [InlineKeyboardButton(buy_text, callback_data=f"buy_{bot_key}")],
        [InlineKeyboardButton("🎬 Demo/Proof দেখুন", url="https://t.me/ratulhossain4241")],
        [InlineKeyboardButton("❓ প্রশ্ন করুন", callback_data="ask_question")],
        [InlineKeyboardButton("🔙 All Products", callback_data="products")],
    ]
    
    await query.edit_message_text(
        text=text,
        reply_markup=InlineKeyboardMarkup(keyboard),
    )


async def show_price_list(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Price list দেখায়"""
    
    query = update.callback_query
    await query.answer()
    
    text = (
        "━━━━━━━━━━━━━━━━━━━━\n"
        "💰 RTX Price List\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"
        "🥉 Qutex Signal 📊\n"
        "   Normal: 1,500tk\n"
        "   🎁 Promo (RTX4241): 1,000tk\n"
        "   ✅ Save: 500tk!\n\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"
        "🥈 Qutex Premium 📊💵\n"
        "   Normal: 3,000tk\n"
        "   🎁 Promo (RTX4241): 2,000tk\n"
        "   ✅ Save: 1,000tk!\n\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"
        "🥇 RTX PRO MAX AI 🚀\n"
        "   Price: 5,000tk (Fixed)\n"
        "   ⚠️ No promo available\n\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"
        "💳 Payment Methods:\n"
        "   📱 bKash: 01344594241\n"
        "   📱 Nagad: 01344594241\n\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "কোনটা নিবেন? 👇\n"
        "━━━━━━━━━━━━━━━━━━━━"
    )
    
    keyboard = [
        [InlineKeyboardButton("🛒 Qutex Signal - 1,000tk", callback_data="buy_bot1")],
        [InlineKeyboardButton("🛒 Qutex Premium - 2,000tk", callback_data="buy_bot2")],
        [InlineKeyboardButton("🛒 RTX PRO MAX AI - 5,000tk", callback_data="buy_bot3")],
        [InlineKeyboardButton("🔙 Back", callback_data="back_start")],
    ]
    
    await query.edit_message_text(
        text=text,
        reply_markup=InlineKeyboardMarkup(keyboard),
    )


async def show_promo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Promo code দেখায়"""
    
    query = update.callback_query
    await query.answer()
    
    text = (
        "━━━━━━━━━━━━━━━━━━━━\n"
        "🎁 Special Promo Code!\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"
        "🔑 Promo Code: RTX4241\n\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"
        "💰 Discount Details:\n\n"
        "🥉 Qutex Signal:\n"
        "   1,500tk → 1,000tk\n"
        "   ✅ Save: 500tk!\n\n"
        "🥈 Qutex Premium:\n"
        "   3,000tk → 2,000tk\n"
        "   ✅ Save: 1,000tk!\n\n"
        "🥇 RTX PRO MAX AI:\n"
        "   ⚠️ Promo apply হয় না\n"
        "   Price: 5,000tk (fixed)\n\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"
        "📌 কীভাবে ব্যবহার করবেন:\n\n"
        "1️⃣ App এ যান\n"
        "2️⃣ Buy Premium click\n"
        "3️⃣ Promo Code দিন: RTX4241\n"
        "4️⃣ Discount apply হবে\n"
        "5️⃣ Payment করুন\n\n"
        "━━━━━━━━━━━━━━━━━━━━"
    )
    
    keyboard = [
        [InlineKeyboardButton("🛒 এখনই Buy করুন", callback_data="products")],
        [InlineKeyboardButton("🔙 Back", callback_data="back_start")],
    ]
    
    await query.edit_message_text(
        text=text,
        reply_markup=InlineKeyboardMarkup(keyboard),
                                     )
