import json

from flask import Flask, request, jsonify
from unicornhatmini import UnicornHATMini

app = Flask(__name__)
panel = UnicornHATMini()

current_color = {
    "r": 0,
    "g": 0,
    "b": 0
}

current_brightness = 1.0

def _update_color_display():
    panel.set_all(current_color["r"], current_color["g"], current_color["b"])
    panel.show()

def _update_brightness_display():
    panel.set_brightness(current_brightness)

panel.set_brightness(current_brightness)
_update_color_display()

@app.route("/")
def healthy():
    return "server is running\n"

@app.route("/color", methods=["PUT"])
def change_color():
    request_data = json.loads(request.data)
    current_color["r"] = request_data["r"]
    current_color["g"] = request_data["g"]
    current_color["b"] = request_data["b"]
    _update_color_display()
    return jsonify(current_color)

@app.route("/brightness", methods=["PUT"])
def change_brightness():
    current_brightness = float(request.data)
    _update_brightness_display()
    return current_brightness

@app.route("/color", methods=["GET"])
def get_color():
    return jsonify(current_color)

@app.route("/brightness", methods=["GET"])
def get_brightness():
    return jsonify(current_brightness)

app.run(host="0.0.0.0", debug=False)

