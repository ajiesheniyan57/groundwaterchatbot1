from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

genai.configure(api_key="AIzaSyBofTfyqyv9bSRd0ChlVT91M0k74BGGQ6c")  # Replace with your actual API key

model = genai.GenerativeModel("models/gemini-1.5-flash")  # Or gemini-1.5-pro if allowed

@app.route("/")
def index():
    return render_template("chat.html")

@app.route("/get", methods=["POST"])
def chatbot_response():
    user_msg = request.json["msg"]
    try:
        response = model.generate_content(user_msg)
        reply = response.text
    except Exception as e:
        reply = f"Error: {str(e)}"
    return jsonify({"response": reply})

if __name__ == "__main__":
    app.run(debug=True, port=10000)
