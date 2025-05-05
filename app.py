from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/api/calcs/<value>", methods=["GET"])
def method_name(value):
    try:
        num = int(value)
        if num <= 0:
            raise ValueError
        return jsonify({
            "dec": num - 1,
            "hex": hex(num)
        })
    except ValueError:
        return "Invalid input", 400

