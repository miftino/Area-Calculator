from flask import Flask, request, jsonify
from flask_cors import CORS
import math

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Flask Calculator API is live!"

# Area Routes
@app.route("/area/square")
def area_square():
    try:
        side = float(request.args.get("side"))
        return jsonify({"shape": "square", "area": side ** 2})
    except:
        return jsonify({"error": "Missing or invalid input: side"}), 400

@app.route("/area/rectangle")
def area_rectangle():
    try:
        length = float(request.args.get("length"))
        width = float(request.args.get("width"))
        return jsonify({"shape": "rectangle", "area": length * width})
    except:
        return jsonify({"error": "Missing or invalid inputs: length and width"}), 400

@app.route("/area/triangle")
def area_triangle():
    try:
        base = float(request.args.get("base"))
        height = float(request.args.get("height"))
        return jsonify({"shape": "triangle", "area": 0.5 * base * height})
    except:
        return jsonify({"error": "Missing or invalid inputs: base and height"}), 400

@app.route("/area/circle")
def area_circle():
    try:
        radius = float(request.args.get("radius"))
        return jsonify({"shape": "circle", "area": math.pi * radius ** 2})
    except:
        return jsonify({"error": "Missing or invalid input: radius"}), 400

# Arithmetic Routes
@app.route("/math/add")
def math_add():
    try:
        a = float(request.args.get("a"))
        b = float(request.args.get("b"))
        return jsonify({"operation": "add", "result": a + b})
    except:
        return jsonify({"error": "Missing or invalid inputs: a and b"}), 400

@app.route("/math/subtract")
def math_subtract():
    try:
        a = float(request.args.get("a"))
        b = float(request.args.get("b"))
        return jsonify({"operation": "subtract", "result": a - b})
    except:
        return jsonify({"error": "Missing or invalid inputs: a and b"}), 400

@app.route("/math/multiply")
def math_multiply():
    try:
        a = float(request.args.get("a"))
        b = float(request.args.get("b"))
        return jsonify({"operation": "multiply", "result": a * b})
    except:
        return jsonify({"error": "Missing or invalid inputs: a and b"}), 400

@app.route("/math/divide")
def math_divide():
    try:
        a = float(request.args.get("a"))
        b = float(request.args.get("b"))
        if b == 0:
            return jsonify({"error": "Division by zero is not allowed"}), 400
        return jsonify({"operation": "divide", "result": a / b})
    except:
        return jsonify({"error": "Missing or invalid inputs: a and b"}), 400

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
