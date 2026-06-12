"""
main.py — Flask web server exposing HID emulator via REST API
Open ui/index.html in browser and control everything from there.
"""
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import threading, os, sys

sys.path.insert(0, os.path.dirname(__file__))
from emulator.keyboard import press_key, type_text, hotkey
from emulator.mouse import click, move, scroll
from emulator.macro_runner import load_and_run

app = Flask(__name__, static_folder="ui")
CORS(app)

@app.route("/")
def index():
    return send_from_directory("ui", "index.html")

@app.route("/api/key", methods=["POST"])
def api_key():
    data = request.json
    press_key(data.get("key", ""))
    return jsonify({"ok": True})

@app.route("/api/type", methods=["POST"])
def api_type():
    data = request.json
    threading.Thread(target=type_text, args=(data.get("text", ""),), daemon=True).start()
    return jsonify({"ok": True})

@app.route("/api/hotkey", methods=["POST"])
def api_hotkey():
    data = request.json
    hotkey(*data.get("keys", []))
    return jsonify({"ok": True})

@app.route("/api/mouse/click", methods=["POST"])
def api_click():
    data = request.json
    click(data.get("button", "left"), data.get("count", 1))
    return jsonify({"ok": True})

@app.route("/api/mouse/move", methods=["POST"])
def api_move():
    data = request.json
    move(data["x"], data["y"])
    return jsonify({"ok": True})

@app.route("/api/mouse/scroll", methods=["POST"])
def api_scroll():
    data = request.json
    scroll(data.get("dx", 0), data.get("dy", -3))
    return jsonify({"ok": True})

@app.route("/api/macro", methods=["POST"])
def api_macro():
    data = request.json
    path = f"macros/{data.get('file', 'gaming.json')}"
    threading.Thread(target=load_and_run, args=(path,), daemon=True).start()
    return jsonify({"ok": True})

if __name__ == "__main__":
    print("HID Emulator running → http://localhost:5001")
    app.run(host="0.0.0.0", port=5001, debug=False)
