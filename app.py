from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

# 🔑 Replace with your OpenAI API key
openai.api_key = "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"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json["message"]

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # ya "gpt-4" agar use kar rahe ho
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input},
            ]
        )
        reply = response["choices"][0]["message"]["content"]
        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"reply": f"Error: {str(e)}"})

if __name__ == "__main__":
    app.run(debug=True)
