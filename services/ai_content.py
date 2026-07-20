# ═══════════════════════════════════════
# AI Content Generator (Gemini)
# Stylish + Professional post তৈরি করে
# ═══════════════════════════════════════

import google.generativeai as genai
from config import GEMINI_API_KEY
import random

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-pro")


def generate_promotion_post():
    """Product promotion post generate করে"""
    prompt = """
    তুমি RTX নামের একটি Trading Signal Bot company এর 
    marketing expert। 

    তোমার কাজ হলো Telegram channel/group এ 
    professional + stylish promotional post লেখা।

    Products:
    1. Qutex Signal - 1,500tk (Promo: 1,000tk, Code: RTX4241) - Forex Signal
    2. Qutex Premium - 3,000tk (Promo: 2,000tk, Code: RTX4241) - Advanced Forex
    3. RTX PRO MAX AI - 5,000tk (No promo) - Crypto/Binance Signal

    Sales Bot: @rtxearn2_bot
    Channel: @ratulhossain4241

    নিয়ম:
    - বাংলা তে লিখবে
    - Emoji ভালো মতো use করবে
    - Professional + catchy হবে
    - Customer কে attract করবে
    - 15-20 line এর মধ্যে
    - শেষে @rtxearn2_bot link দিবে
    - প্রতিবার আলাদা style এ লিখবে
    - Line separator ═══ বা ━━━ use করো
    """
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return get_fallback_promotion()


def generate_educational_post():
    """Educational/tips post generate করে"""
    topics = [
        "Risk Management কেন জরুরি",
        "Signal follow করার সঠিক নিয়ম",
        "Trading psychology tips",
        "কখন trade করবেন কখন করবেন না",
        "Money management rules",
        "Forex vs Crypto trading পার্থক্য",
        "Candle pattern basics",
        "Support ও Resistance কী",
        "নতুন trader এর common mistakes",
        "Profit consistent রাখার tips",
    ]
    
    topic = random.choice(topics)
    
    prompt = f"""
    তুমি RTX Trading এর expert। 
    Telegram group এ educational post লিখবে।

    Topic: {topic}

    নিয়ম:
    - বাংলা তে সহজ ভাষায়
    - Emoji use করো
    - 10-15 line
    - Informative + helpful
    - শেষে RTX Bot এর কথা mention করো
    - Sales Bot: @rtxearn2_bot
    - Professional style
    - Line separator use করো
    """
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return get_fallback_educational()


def generate_success_story():
    """Success story post generate করে"""
    prompt = """
    তুমি RTX Trading Bot এর marketing expert।
    একটা realistic success story post লিখো।

    Products: Qutex Signal, Qutex Premium, RTX PRO MAX AI
    Sales Bot: @rtxearn2_bot

    নিয়ম:
    - বাংলা তে
    - Realistic story (কিন্তু attractive)
    - Customer name fictional রাখো
    - Profit amount realistic রাখো (500-3000tk range)
    - Emoji use করো
    - 10-15 line
    - শেষে "আপনিও try করুন" বলে @rtxearn2_bot link
    """
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return get_fallback_success()


def generate_offer_post():
    """Special offer post generate করে"""
    prompt = """
    তুমি RTX এর marketing expert।
    Promo code offer post লিখো।

    Promo Code: RTX4241
    - Qutex Signal: 1500tk → 1000tk
    - Qutex Premium: 3000tk → 2000tk
    - RTX PRO MAX AI: 5000tk (no promo)

    Sales Bot: @rtxearn2_bot

    নিয়ম:
    - বাংলা তে
    - Urgency create করো ("Limited time!", "আজকেই!")
    - Emoji ভালো মতো use করো
    - 10-15 line
    - Eye-catching
    - Professional
    """
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return get_fallback_offer()


def generate_motivational_post():
    """Motivational post generate করে"""
    prompt = """
    তুমি RTX Trading Community এর leader।
    রাতের motivational post লিখো traders দের জন্য।

    নিয়ম:
    - বাংলা তে
    - Trading related motivation
    - Inspirational
    - Emoji use করো
    - 8-12 line
    - শেষে RTX community join করতে বলো
    - Bot: @rtxearn2_bot
    """
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return get_fallback_motivational()


def generate_faq_answer(question):
    """Customer এর প্রশ্নের smart answer দেয়"""
    prompt = f"""
    তুমি RTX Trading Bot company এর customer support expert।

    Company Info:
    - Company: RTX
    - Products: 3টা Trading Signal Bot
    - Qutex Signal (1500tk, promo 1000tk)
    - Qutex Premium (3000tk, promo 2000tk)  
    - RTX PRO MAX AI (5000tk)
    - Promo Code: RTX4241
    - Payment: bKash/Nagad 01344594241
    - Support: @ratulhossain56
    - Sales Bot: @rtxearn2_bot
    - No refund policy
    - No guarantee (Trading is risky)
    - Signal accuracy high but not 100%
    - Works on all devices (phone + PC)
    - Telegram Mini Web App based
    
    Important Rules:
    - কখনো refund promise করবে না
    - কখনো guaranteed profit বলবে না
    - Trading risky বলবে
    - কিন্তু positive থাকবে
    - Product recommend করবে smartly
    - Customer কে comfortable feel করাবে

    Customer এর প্রশ্ন: "{question}"

    বাংলা তে professional, friendly, 
    helpful answer দাও। Emoji use করো।
    শেষে product recommend করো subtly।
    """
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return (
            "ভাই, আপনার প্রশ্নের জন্য ধন্যবাদ! 🙏\n\n"
            "বিস্তারিত জানতে আমাদের admin এর সাথে কথা বলুন:\n"
            f"👨‍💼 Support: @ratulhossain56\n"
            f"📞 WhatsApp: 01344594241"
        )


# ═══════════════════════════════════════
# Fallback Posts (AI fail করলে)
# ═══════════════════════════════════════

def get_fallback_promotion():
    posts = [
        (
            "━━━━━━━━━━━━━━━━━━━━\n"
            "🔥 RTX Trading Signal 🔥\n"
            "━━━━━━━━━━━━━━━━━━━━\n\n"
            "💎 3টা Powerful Bot:\n\n"
            "🥉 Qutex Signal - 1,000tk\n"
            "   (Promo: RTX4241)\n\n"
            "🥈 Qutex Premium - 2,000tk\n"
            "   (Promo: RTX4241)\n\n"
            "🥇 RTX PRO MAX AI - 5,000tk\n\n"
            "✅ Real-time Data\n"
            "✅ High Accuracy\n"
            "✅ Instant Access\n\n"
            "🎯 Details: @rtxearn2_bot\n"
            "📢 Channel: @ratulhossain4241\n"
            "━━━━━━━━━━━━━━━━━━━━"
        ),
    ]
    return random.choice(posts)


def get_fallback_educational():
    return (
        "━━━━━━━━━━━━━━━━━━━━\n"
        "💡 Trading Tips 💡\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"
        "✅ সবসময় Stop Loss use করুন\n"
        "✅ একবারে বেশি invest করবেন না\n"
        "✅ Signal follow করুন\n"
        "✅ Patience রাখুন\n\n"
        "🎯 Accurate Signal পেতে:\n"
        "👉 @rtxearn2_bot\n"
        "━━━━━━━━━━━━━━━━━━━━"
    )


def get_fallback_success():
    return (
        "━━━━━━━━━━━━━━━━━━━━\n"
        "🎉 Success Story!\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"
        "আমাদের একজন VIP user আজকে\n"
        "RTX PRO MAX AI দিয়ে দারুণ profit করেছে!\n\n"
        "📈 Signal follow করলে result আসেই!\n\n"
        "👉 Try করুন: @rtxearn2_bot\n"
        "━━━━━━━━━━━━━━━━━━━━"
    )


def get_fallback_offer():
    return (
        "━━━━━━━━━━━━━━━━━━━━\n"
        "🎁 Special Promo! 🎁\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"
        "Code: RTX4241\n\n"
        "💰 Qutex Signal: 1500→1000tk\n"
        "💰 Qutex Premium: 3000→2000tk\n\n"
        "⏰ Limited time!\n\n"
        "👉 @rtxearn2_bot\n"
        "━━━━━━━━━━━━━━━━━━━━"
    )


def get_fallback_motivational():
    return (
        "━━━━━━━━━━━━━━━━━━━━\n"
        "🌟 Good Night Traders! 🌟\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"
        "আজকের দিন শেষ, কালকে নতুন সুযোগ!\n\n"
        "💪 Never give up!\n"
        "📈 Consistency is key!\n\n"
        "🎯 RTX Family: @rtxearn2_bot\n"
        "━━━━━━━━━━━━━━━━━━━━"
  )
