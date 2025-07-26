import os
from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

# ✅ Get API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json["message"]

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4-1106-preview",  # ya "gpt-3.5-turbo"
            messages=[
                {"role": "user", "content": user_input}
            ]
        )
        reply = response.choices[0].message["content"]
        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
