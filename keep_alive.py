# ═══════════════════════════════════════
# Keep Alive System
# Bot যাতে কখনো ঘুমিয়ে না যায়
# প্রতি 2 মিনিটে নিজেকে নিজে ping করে
# ═══════════════════════════════════════

from flask import Flask
from threading import Thread
import requests
import time
from config import RENDER_URL, PING_INTERVAL

app = Flask(__name__)


@app.route("/")
def home():
    return "✅ RTX Marketing Bot is ALIVE! 🚀"


@app.route("/health")
def health():
    return "OK", 200


def run_flask():
    """Flask server চালু করে"""
    app.run(host="0.0.0.0", port=8080)


def keep_alive():
    """Flask server background এ চালু করে"""
    t = Thread(target=run_flask, daemon=True)
    t.start()


def self_ping():
    """
    নিজেকে নিজে ping করে যাতে bot ঘুমিয়ে না যায়
    প্রতি 2 মিনিটে একবার
    """
    while True:
        try:
            if RENDER_URL:
                requests.get(f"{RENDER_URL}/health", timeout=10)
                print(f"✅ Self-ping successful!")
        except Exception as e:
            print(f"⚠️ Ping failed: {e}")
        time.sleep(PING_INTERVAL)


def start_ping():
    """Ping system background এ চালু করে"""
    t = Thread(target=self_ping, daemon=True)
    t.start()
