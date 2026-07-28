# ═══════════════════════════════════════════════
# RTX Bot - Bulletproof Keep Alive System
# Render Free Tier এ কখনো sleep হবে না
# ═══════════════════════════════════════════════

import os
import time
import logging
import requests
from flask import Flask, jsonify
from threading import Thread
from datetime import datetime

log = logging.getLogger(__name__)

# ═══════════════════════════════════════════════
# ⚡ HARDCODED URL (Fail-safe)
# তোমার Render service এর actual URL
# ═══════════════════════════════════════════════
RENDER_APP_URL = "https://rtx-soft-xio.onrender.com"

# ═══════════════════════════════════════════════
# Ping Intervals (Seconds)
# ═══════════════════════════════════════════════
PRIMARY_PING_INTERVAL   = 120   # 2 minutes - Primary ping
BACKUP_PING_INTERVAL    = 180   # 3 minutes - Backup ping
RECOVERY_PING_INTERVAL  = 45    # 45 seconds - When failing

# ═══════════════════════════════════════════════
# Flask App
# ═══════════════════════════════════════════════
flask_app = Flask(__name__)

# Statistics
_stats = {
    "start_time":    datetime.now(),
    "ping_count":    0,
    "ping_success":  0,
    "ping_failed":   0,
    "last_ping":     None,
    "last_success":  None,
}


# ═══════════════════════════════════════════════
# Flask Routes
# ═══════════════════════════════════════════════

@flask_app.route("/")
def home():
    uptime = datetime.now() - _stats["start_time"]
    hours   = int(uptime.total_seconds() // 3600)
    minutes = int((uptime.total_seconds() % 3600) // 60)
    seconds = int(uptime.total_seconds() % 60)

    success_rate = 0
    if _stats["ping_count"] > 0:
        success_rate = (_stats["ping_success"] / _stats["ping_count"]) * 100

    html = f"""
    <html>
    <head>
        <title>RTX Bot Status</title>
        <meta http-equiv="refresh" content="30">
        <style>
            body {{
                font-family: Arial;
                background: #1a1a2e;
                color: #eee;
                padding: 20px;
                max-width: 600px;
                margin: auto;
            }}
            h1 {{ color: #00ff88; }}
            .stat {{
                background: #16213e;
                padding: 15px;
                margin: 10px 0;
                border-radius: 8px;
                border-left: 4px solid #00ff88;
            }}
            .label {{ color: #888; font-size: 12px; }}
            .value {{ font-size: 18px; font-weight: bold; }}
        </style>
    </head>
    <body>
        <h1>✅ RTX Marketing Bot ALIVE! 🚀</h1>

        <div class="stat">
            <div class="label">⏰ UPTIME</div>
            <div class="value">{hours}h {minutes}m {seconds}s</div>
        </div>

        <div class="stat">
            <div class="label">📊 TOTAL PINGS</div>
            <div class="value">{_stats['ping_count']}</div>
        </div>

        <div class="stat">
            <div class="label">✅ SUCCESS RATE</div>
            <div class="value">{success_rate:.1f}% ({_stats['ping_success']}/{_stats['ping_count']})</div>
        </div>

        <div class="stat">
            <div class="label">❌ FAILED</div>
            <div class="value">{_stats['ping_failed']}</div>
        </div>

        <div class="stat">
            <div class="label">🕐 LAST PING</div>
            <div class="value">{_stats['last_ping'] or 'Waiting...'}</div>
        </div>

        <div class="stat">
            <div class="label">✨ LAST SUCCESS</div>
            <div class="value">{_stats['last_success'] or 'Waiting...'}</div>
        </div>

        <p style="text-align:center; color:#888; margin-top:20px;">
            Auto-refresh every 30 seconds
        </p>
    </body>
    </html>
    """
    return html, 200


@flask_app.route("/health")
def health():
    """Health check endpoint - Used by pingers"""
    uptime_seconds = int((datetime.now() - _stats["start_time"]).total_seconds())
    return jsonify({
        "status":         "ok",
        "uptime_seconds": uptime_seconds,
        "ping_count":     _stats["ping_count"],
        "success":        _stats["ping_success"],
    }), 200


@flask_app.route("/ping")
def ping_endpoint():
    """Simple ping endpoint"""
    return "pong", 200


@flask_app.route("/wake")
def wake():
    """Wake endpoint"""
    return "awake", 200


# ═══════════════════════════════════════════════
# Flask Server Thread
# ═══════════════════════════════════════════════

def _run_flask():
    """Flask server runner"""
    port = int(os.environ.get("PORT", 8080))
    log.info(f"🌐 Flask server starting on port {port}")
    try:
        flask_app.run(
            host="0.0.0.0",
            port=port,
            use_reloader=False,
            threaded=True,
            debug=False,
        )
    except Exception as e:
        log.critical(f"❌ Flask server crashed: {e}")


def keep_alive():
    """Start Flask server thread"""
    thread = Thread(target=_run_flask, daemon=True, name="FlaskServer")
    thread.start()
    log.info("✅ Flask keep-alive server thread started")


# ═══════════════════════════════════════════════
# Primary Self-Ping (Every 2 Minutes)
# ═══════════════════════════════════════════════

def _primary_ping_loop():
    """Primary ping - Every 2 minutes"""
    log.info("═" * 45)
    log.info(f"🔄 PRIMARY PING System Started")
    log.info(f"🌐 URL: {RENDER_APP_URL}")
    log.info(f"⏰ Interval: {PRIMARY_PING_INTERVAL}s (2 min)")
    log.info("═" * 45)

    # Wait 30 seconds before first ping (let server start)
    time.sleep(30)

    consecutive_failures = 0

    while True:
        try:
            _stats["ping_count"] += 1
            _stats["last_ping"] = datetime.now().strftime("%H:%M:%S")

            response = requests.get(
                f"{RENDER_APP_URL}/health",
                timeout=20,
                headers={
                    "User-Agent": "RTX-Primary-Ping/2.0",
                    "Cache-Control": "no-cache",
                },
            )

            if response.status_code == 200:
                _stats["ping_success"] += 1
                _stats["last_success"] = datetime.now().strftime("%H:%M:%S")
                consecutive_failures = 0
                log.info(
                    f"✅ PRIMARY Ping OK ({response.status_code}) | "
                    f"Success: {_stats['ping_success']}/{_stats['ping_count']}"
                )
            else:
                _stats["ping_failed"] += 1
                consecutive_failures += 1
                log.warning(
                    f"⚠️ PRIMARY Ping returned {response.status_code} | "
                    f"Failures: {consecutive_failures}"
                )

        except requests.exceptions.Timeout:
            _stats["ping_failed"] += 1
            consecutive_failures += 1
            log.warning(f"⏰ PRIMARY Timeout | Failures: {consecutive_failures}")

        except requests.exceptions.ConnectionError:
            _stats["ping_failed"] += 1
            consecutive_failures += 1
            log.warning(f"🔌 PRIMARY Connection error | Failures: {consecutive_failures}")

        except Exception as e:
            _stats["ping_failed"] += 1
            consecutive_failures += 1
            log.error(f"❌ PRIMARY Ping error: {e}")

        # Adaptive sleep - Fast retry on failures
        if consecutive_failures >= 3:
            log.warning(
                f"🚨 {consecutive_failures} failures — "
                f"Fast retry in {RECOVERY_PING_INTERVAL}s"
            )
            time.sleep(RECOVERY_PING_INTERVAL)
        else:
            time.sleep(PRIMARY_PING_INTERVAL)


def start_ping():
    """Start primary ping thread"""
    thread = Thread(target=_primary_ping_loop, daemon=True, name="PrimaryPing")
    thread.start()
    log.info("✅ Primary ping thread started")


# ═══════════════════════════════════════════════
# Backup Ping (Every 3 Minutes - Different endpoint)
# ═══════════════════════════════════════════════

def _backup_ping_loop():
    """Backup ping - Every 3 minutes, uses different endpoints"""
    log.info(f"🔄 BACKUP PING System Started (Interval: {BACKUP_PING_INTERVAL}s)")

    # Wait 60 seconds before first ping (offset from primary)
    time.sleep(60)

    endpoints = ["/", "/ping", "/wake", "/health"]
    endpoint_index = 0

    while True:
        # Rotate through endpoints
        endpoint = endpoints[endpoint_index % len(endpoints)]
        endpoint_index += 1

        try:
            response = requests.get(
                f"{RENDER_APP_URL}{endpoint}",
                timeout=15,
                headers={
                    "User-Agent": "RTX-Backup-Ping/2.0",
                    "Cache-Control": "no-cache",
                },
            )
            log.info(f"🔁 BACKUP Ping {endpoint} → {response.status_code}")

        except Exception as e:
            log.debug(f"⚠️ Backup ping failed on {endpoint}: {e}")

        time.sleep(BACKUP_PING_INTERVAL)


def start_backup_ping():
    """Start backup ping thread"""
    thread = Thread(target=_backup_ping_loop, daemon=True, name="BackupPing")
    thread.start()
    log.info("✅ Backup ping thread started")


# ═══════════════════════════════════════════════
# Aggressive Ping (Every 60 Seconds - Final layer)
# ═══════════════════════════════════════════════

def _aggressive_ping_loop():
    """Aggressive ping - Every 60 seconds - Final safety net"""
    log.info("🔄 AGGRESSIVE PING System Started (60s interval)")

    # Wait 90 seconds before starting
    time.sleep(90)

    while True:
        try:
            requests.get(
                f"{RENDER_APP_URL}/ping",
                timeout=10,
                headers={"User-Agent": "RTX-Aggressive-Ping/2.0"},
            )
        except Exception:
            pass

        time.sleep(60)


def start_aggressive_ping():
    """Start aggressive ping thread"""
    thread = Thread(target=_aggressive_ping_loop, daemon=True, name="AggressivePing")
    thread.start()
    log.info("✅ Aggressive ping thread started (60s)")


# ═══════════════════════════════════════════════
# Master Function - Start Everything
# ═══════════════════════════════════════════════

def start_all_keepalive():
    """One function to start everything"""
    log.info("═" * 45)
    log.info("🚀 STARTING TRIPLE-LAYER KEEP-ALIVE")
    log.info("═" * 45)

    keep_alive()             # Flask server
    start_ping()             # Primary (2 min)
    start_backup_ping()      # Backup (3 min)
    start_aggressive_ping()  # Aggressive (60s)

    log.info("═" * 45)
    log.info("✅ ALL KEEP-ALIVE SYSTEMS ACTIVE!")
    log.info(f"🌐 URL: {RENDER_APP_URL}")
    log.info("⚡ Layer 1: Primary ping every 120s")
    log.info("⚡ Layer 2: Backup ping every 180s")
    log.info("⚡ Layer 3: Aggressive ping every 60s")
    log.info("💪 Server will NEVER sleep!")
    log.info("═" * 45)
