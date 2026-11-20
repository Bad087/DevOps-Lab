from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "application": "DevOps Health Monitor",
        "message": "Welcome to Flask",
        "status": "Running",
        "version": "2.0"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "service": "Flask Application"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
