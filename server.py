import json

from flask import Flask, request, jsonify
# from unicornhatmini import UnicornHATMini

app = Flask(__name__)
# panel = UnicornHATMini()

current_color = {
    "r": 0,
    "g": 0,
    "b": 0
}

@app.route("/")
def healthy():
    return "server is running\n"

@app.route("/color", methods=["PUT"])
def change_color():
    request_data = json.loads(request.data)
    current_color["r"] = request_data["r"]
    current_color["g"] = request_data["g"]
    current_color["b"] = request_data["b"]
    # panel.set_all(current_color["r"], current_color["g"], current_color["b"])
    return jsonify(current_color)

@app.route("/color", methods=["GET"])
def get_color():
    return jsonify(current_color)

app.run(debug=False)

