from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Flask API is running"})

@app.route("/about")
def about():
    return jsonify({
        "name": "Simple REST API",
        "version": "1.0",
        "description": "Docker networking with Flask, MySQL and Redis"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)