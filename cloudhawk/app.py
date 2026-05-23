from flask import Flask, render_template, jsonify
from model import run_pipeline
import threading
import time

app = Flask(__name__)

cached_data = []
cached_stats = {
    "total": 0,
    "critical": 0,
    "high": 0,
    "medium": 0,
    "low": 0
}
last_updated = "Not updated yet"


def update_data():
    global cached_data, cached_stats, last_updated

    while True:
        data = run_pipeline()

        stats = {
            "total": len(data),
            "critical": sum(1 for d in data if d["risk"] == "CRITICAL"),
            "high": sum(1 for d in data if d["risk"] == "HIGH"),
            "medium": sum(1 for d in data if d["risk"] == "MEDIUM"),
            "low": sum(1 for d in data if d["risk"] == "LOW"),
        }

        cached_data = data
        cached_stats = stats
        last_updated = time.strftime("%Y-%m-%d %H:%M:%S")

        print("✅ Data updated")
        time.sleep(300)


@app.route("/")
def home():
    return render_template("index.html",
                           alerts=cached_data,
                           stats=cached_stats,
                           last_updated=last_updated)


@app.route("/api/refresh", methods=["GET", "POST"])
def refresh():
    global cached_data, cached_stats, last_updated

    data = run_pipeline()

    stats = {
        "total": len(data),
        "critical": sum(1 for d in data if d["risk"] == "CRITICAL"),
        "high": sum(1 for d in data if d["risk"] == "HIGH"),
        "medium": sum(1 for d in data if d["risk"] == "MEDIUM"),
        "low": sum(1 for d in data if d["risk"] == "LOW"),
    }

    cached_data = data
    cached_stats = stats
    last_updated = time.strftime("%Y-%m-%d %H:%M:%S")

    return jsonify({"status": "success"})


# 🔥 CLEAR ALERTS
@app.route("/api/clear", methods=["POST"])
def clear():
    global cached_data, cached_stats

    cached_data = []
    cached_stats = {
        "total": 0,
        "critical": 0,
        "high": 0,
        "medium": 0,
        "low": 0
    }

    return jsonify({"status": "cleared"})


if __name__ == "__main__":
    thread = threading.Thread(target=update_data, daemon=True)
    thread.start()

    app.run(debug=True)