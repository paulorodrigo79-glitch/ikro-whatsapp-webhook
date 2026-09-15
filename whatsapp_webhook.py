from flask import Flask, request

app = Flask(__name__)

VERIFY_TOKEN = "ikro_teste_2026"


@app.route("/webhook", methods=["GET"])
def verificar_webhook():
    if request.args.get("hub.verify_token") == VERIFY_TOKEN:
        return request.args.get("hub.challenge"), 200

    return "Token inválido", 403


if __name__ == "__main__":
    app.run(host="0.0.0"port=5000)