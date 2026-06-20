import os
from flask import Flask
from alerts import check_failed_events, check_stockout_orders
from datetime import datetime, timezone

app = Flask(__name__)

@app.route("/", methods=["POST"])
def run_alerts():
    print(f"[{datetime.now(timezone.utc).isoformat()}] Running alert checks...")
    check_failed_events()
    check_stockout_orders()
    print(f"[{datetime.now(timezone.utc).isoformat()}] Alert checks complete.")
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))