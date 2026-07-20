# ═══════════════════════════════════════
# AI Content Generator (Gemini)
# ═══════════════════════════════════════

import google.generativeai as genai
from config import GEMINI_API_KEY
import random

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")


def generate_promotion_post():
    """Product promotion post"""
    prompt = """
    তুমি RTX Trading Signal Bot company এর marketing expert।
    Telegram channel এ professional + stylish promotional post লেখো।

    Products:
    1. Qutex Signal - 1,500tk (Promo RTX4241: 1,000tk) - Forex
    2. Qutex Premium - 3,000tk (Promo RTX4241: 2,000tk) - Advanced Forex
    3. RTX PRO MAX AI - 5,000tk - Crypto Binance Signal

    Sales Bot: @rtxearn2_bot

    নিয়ম:
    - বাংলা ভাষায়
    - প্রচুর Emoji use করো
    - Professional + Catchy
    - 15-20 line
    - ━━━ line separator use করো
    - শেষে @rtxearn2_bot link
    - প্রতিবার আলাদা style
    - Trading focused
    """
    return _generate(prompt, get_fallback_promotion)


def generate_educational_post():
    """Educational trading tips"""
    topics = [
        "Risk Management এর গুরুত্ব",
        "Stop Loss কেন জরুরি",
        "Money Management Rules",
        "Trading Psychology Tips",
        "Candle Pattern Basics",
        "Support ও Resistance",
        "RSI Indicator কী",
        "MACD কীভাবে use করবেন",
        "Trend Follow করার নিয়ম",
        "Emotion Control এ Trading",
        "Position Sizing",
        "Risk Reward Ratio",
        "Market Analysis Tips",
        "Trading Journal রাখার নিয়ম",
        "Fibonacci Retracement",
    ]
    topic = random.choice(topics)
    
    prompt = f"""
    তুমি RTX Trading expert।
    Educational post লিখো।

    Topic: {topic}

    নিয়ম:
    - বাংলা ভাষায় সহজে
    - Emoji use করো
    - 12-15 line
    - Informative + helpful
    - ━━━ separator
    - শেষে "সঠিক signal পেতে @rtxearn2_bot"
    """
    return _generate(prompt, get_fallback_educational)


def generate_success_story():
    """Realistic success story"""
    prompt = """
    RTX Trading Bot এর customer এর success story লিখো।

    Products: Qutex Signal, Qutex Premium, RTX PRO MAX AI
    Bot: @rtxearn2_bot

    নিয়ম:
    - বাংলা ভাষায়
    - Realistic story
    - Customer name (fictional): Rahim, Karim, Sohel, Nasir, Jamal
    - Profit: 500-3000tk (realistic)
    - Emoji use করো
    - 10-12 line
    - Believable
    - ━━━ separator
    - শেষে "আপনিও try করুন @rtxearn2_bot"
    """
    return _generate(prompt, get_fallback_success)


def generate_offer_post():
    """Promo code offer"""
    prompt = """
    RTX এর Promo offer post।

    Promo Code: RTX4241
    - Qutex Signal: 1500tk → 1000tk
    - Qutex Premium: 3000tk → 2000tk
    - RTX PRO MAX AI: 5000tk (no promo)

    Bot: @rtxearn2_bot

    নিয়ম:
    - বাংলা ভাষায়
    - Urgency ("আজকেই!", "Limited!")
    - Prominent emoji
    - 12-15 line
    - Eye-catching
    - ━━━ separator
    """
    return _generate(prompt, get_fallback_offer)


def generate_motivational_post():
    """Motivational for traders"""
    prompt = """
    Trader দের জন্য motivational post।

    নিয়ম:
    - বাংলা ভাষায়
    - Trading motivation
    - Inspirational
    - Emoji use
    - 10-12 line
    - ━━━ separator
    - শেষে "RTX Family - @rtxearn2_bot"
    """
    return _generate(prompt, get_fallback_motivational)


def generate_signal_tips_post():
    """Signal follow করার tips"""
    prompt = """
    Signal follow করার professional tips post।

    Topics (একটা select করো):
    - Signal আসলে সাথে সাথে trade
    - Entry price এ ঢুকতে হবে
    - Stop Loss অবশ্যই দিবে
    - TP এ profit book
    - Emotion control
    - একবারে সব capital না
    - Signal miss করলে skip

    নিয়ম:
    - বাংলা ভাষায়
    - Professional
    - Actionable tips
    - Emoji use
    - 12-15 line
    - ━━━ separator
    - শেষে "RTX PRO MAX AI - @rtxearn2_bot"
    """
    return _generate(prompt, get_fallback_signal_tips)


def generate_faq_answer(question):
    """Customer এর প্রশ্নের answer"""
    prompt = f"""
    তুমি RTX Trading Bot company এর customer support।

    Company Info:
    - Products: 3টা Trading Signal Bot
    - Qutex Signal (1500tk, promo RTX4241: 1000tk)
    - Qutex Premium (3000tk, promo RTX4241: 2000tk)
    - RTX PRO MAX AI (5000tk)
    - Payment: bKash/Nagad 01344594241
    - Support: @ratulhossain56
    - Sales Bot: @rtxearn2_bot
    - Channel: @ratulhossain4241
    - No refund
    - No guarantee (Trading risky)
    
    Rules:
    - কখনো refund promise না
    - কখনো guaranteed profit না
    - Trading risky বলো
    - Positive থাকো
    - Product recommend করো smartly
    - Friendly + Professional

    Customer question: "{question}"

    বাংলা ভাষায় short (5-8 line), professional, friendly answer।
    Emoji use করো। শেষে product recommend করো।
    """
    return _generate(prompt, lambda: (
        "ভাই, ধন্যবাদ! 🙏\n\n"
        "বিস্তারিত জানতে:\n"
        "👉 @rtxearn2_bot\n"
        "👨‍💼 @ratulhossain56"
    ))


def _generate(prompt, fallback):
    """AI generate wrapper with fallback"""
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"AI Error: {e}")
        return fallback()


# ═══════════════════════════════════════
# Fallback Posts
# ═══════════════════════════════════════

def get_fallback_promotion():
    posts = [
        (
            "━━━━━━━━━━━━━━━━━━━━\n"
            "🔥 RTX Trading Signal 🔥\n"
            "━━━━━━━━━━━━━━━━━━━━\n\n"
            "💎 3টা Powerful Signal Bot:\n\n"
            "🥉 Qutex Signal - 1,000tk\n"
            "   (Promo: RTX4241)\n"
            "🥈 Qutex Premium - 2,000tk\n"
            "   (Promo: RTX4241)\n"
            "🥇 RTX PRO MAX AI - 5,000tk\n\n"
            "✅ Real-time Data\n"
            "✅ High Accuracy\n"
            "✅ 24/7 Support\n\n"
            "🎯 @rtxearn2_bot"
        ),
        (
            "━━━━━━━━━━━━━━━━━━━━\n"
            "💰 Earn with RTX Signals\n"
            "━━━━━━━━━━━━━━━━━━━━\n\n"
            "📊 Real Market Data\n"
            "🎯 Accurate Signal\n"
            "⚡ Instant Access\n\n"
            "🥇 VIP: RTX PRO MAX AI\n"
            "💎 Only 5000tk\n\n"
            "🚀 Start Now: @rtxearn2_bot"
        ),
    ]
    return random.choice(posts)


def get_fallback_educational():
    posts = [
        (
            "━━━━━━━━━━━━━━━━━━━━\n"
            "💡 Trading Tips 💡\n"
            "━━━━━━━━━━━━━━━━━━━━\n\n"
            "✅ Stop Loss অবশ্যই দিন\n"
            "✅ Risk Management মেনে চলুন\n"
            "✅ Signal follow করুন\n"
            "✅ Patience রাখুন\n"
            "✅ Emotion control করুন\n\n"
            "🎯 @rtxearn2_bot"
        ),
    ]
    return random.choice(posts)


def get_fallback_success():
    return (
        "━━━━━━━━━━━━━━━━━━━━\n"
        "🎉 Success Story!\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"
        "'RTX VIP Bot দিয়ে আজ 2000tk profit!'\n"
        "- Rahim, Dhaka\n\n"
        "📈 আপনিও start করুন!\n"
        "👉 @rtxearn2_bot"
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
        "👉 @rtxearn2_bot"
    )


def get_fallback_motivational():
    return (
        "━━━━━━━━━━━━━━━━━━━━\n"
        "🌟 Never Give Up! 🌟\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"
        "💪 Consistency is key\n"
        "📈 Learn from mistakes\n"
        "🎯 Trust the process\n\n"
        "RTX Family: @rtxearn2_bot"
    )


def get_fallback_signal_tips():
    return (
        "━━━━━━━━━━━━━━━━━━━━\n"
        "📊 Signal Tips 📊\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"
        "✅ Signal আসলে সাথে সাথে trade\n"
        "✅ Entry price ঠিক রাখুন\n"
        "✅ Stop Loss অবশ্যই\n"
        "✅ TP এ profit book\n\n"
        "🚀 @rtxearn2_bot"
    )
