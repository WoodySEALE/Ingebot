from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Le serveur Flask fonctionne ! 🚀"

@app.route("/api/message", methods=["POST"])
def receive_message():
    data = request.get_json()
    return jsonify({"response": f"Tu as dit : {data['text']}"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
