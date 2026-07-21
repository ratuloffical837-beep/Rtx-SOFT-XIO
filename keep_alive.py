# ═══════════════════════════════════════
# Keep Alive System
# ═══════════════════════════════════════

from flask import Flask
from threading import Thread
import requests
import time
import logging
from config import RENDER_URL, PING_INTERVAL

log = logging.getLogger(__name__)
app = Flask(__name__)


@app.route("/")
def home():
    return "✅ RTX Marketing Bot is ALIVE! 🚀", 200


@app.route("/health")
def health():
    return "OK", 200


def _run_flask():
    app.run(host="0.0.0.0", port=8080, use_reloader=False)


def keep_alive():
    Thread(target=_run_flask, daemon=True).start()
    log.info("✅ Flask keep-alive server started")


def _self_ping():
    while True:
        try:
            if RENDER_URL:
                r = requests.get(f"{RENDER_URL}/health", timeout=10)
                log.info(f"✅ Ping OK ({r.status_code})")
        except Exception as e:
            log.warning(f"⚠️ Ping failed: {e}")
        time.sleep(PING_INTERVAL)


def start_ping():
    Thread(target=_self_ping, daemon=True).start()
    log.info("✅ Self-ping system started")
