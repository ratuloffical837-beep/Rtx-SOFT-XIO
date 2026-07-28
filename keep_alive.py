# ═══════════════════════════════════════
# Keep Alive System (Fixed)
# ═══════════════════════════════════════

import os
import time
import logging
import requests
from flask import Flask
from threading import Thread
from config import RENDER_URL, PING_INTERVAL

log = logging.getLogger(__name__)

flask_app = Flask(__name__)


@flask_app.route("/")
def home():
    return "✅ RTX Marketing Bot is ALIVE! 🚀", 200


@flask_app.route("/health")
def health():
    return "OK", 200


def _run_flask():
    port = int(os.environ.get("PORT", 8080))
    flask_app.run(host="0.0.0.0", port=port, use_reloader=False)


def keep_alive():
    """Flask server start"""
    Thread(target=_run_flask, daemon=True).start()
    log.info("✅ Flask keep-alive server started")


def _self_ping():
    """Self-ping to prevent sleep"""
    if not RENDER_URL:
        log.warning("⚠️ RENDER_URL not set — ping disabled")
        return
    
    while True:
        try:
            r = requests.get(f"{RENDER_URL}/health", timeout=10)
            log.info(f"✅ Self-ping OK ({r.status_code})")
        except Exception as e:
            log.warning(f"⚠️ Ping failed: {e}")
        time.sleep(PING_INTERVAL)


def start_ping():
    """Self-ping thread start"""
    Thread(target=_self_ping, daemon=True).start()
    log.info("✅ Self-ping system started")
