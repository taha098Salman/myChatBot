import os
from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    try:
        user_message = request.json.get("message", "")

        if not user_message:
            return jsonify({"reply": "Kuch likho toh sahi!"})

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # ya gpt-4 agar enabled ho
            messages=[
                {"role": "user", "content": user_message}
            ]
        )

        bot_reply = response["choices"][0]["message"]["content"]
        return jsonify({"reply": bot_reply.strip()})

    except Exception as e:
        return jsonify({"reply": f"⚠️ Error: {str(e)}"})

if __name__ == "__main__":
    app.run(debug=True)
