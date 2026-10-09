from flask import Flask, request

app = Flask(__name__)

VERIFY_TOKEN = "ikro_teste_2026"


@app.route("/webhook", methods=["GET"])
def verificar_webhook():
    if request.args.get("hub.verify_token") == VERIFY_TOKEN:
        return request.args.get("hub.challenge"), 200

    return "Token inválido", 403

@app.route("/webhook", methods=["POST"])
def receber_webhook():
    dados = request.get_json(silent=True) or {}
    try:
        value = dados["entry"][0]["changes"][0]["value"]
        mensagem = value["messages"][0]
        numero = mensagem["from"]
        texto = mensagem.get("text", {}).get("body", "")

        print(f"NUMERO: {numero}", flush=True)
        print(f"MENSAGEM: {texto}", flush=True)
        resposta = f"Recebi sua mensagem: {texto}"
        print(resposta, flush=True)
        return "EVENT_RECEIVED", 200
    except (KeyError, IndexError, TypeError):
        print("Evento recebido sem mensagem de texto.", flush=True)
        return "EVENT_RECEIVED", 200


if __name__ == "__main__":
    app.run(host="0.0.0", port=int(_import_("os").environ.get("PORT", 5000)))
