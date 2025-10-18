from flask import Flask, render_template, request, jsonify
from voice_utils import recognize_speech, speak_text
import json
import os

app = Flask(__name__)

# Load books
with open("books.json") as f:
    books = json.load(f)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/borrow", methods=["POST"])
def borrow_book():
    data = request.get_json()
    user_input = data.get("book")

    # If user clicks the voice option, capture it
    if user_input == "voice":
        user_input = recognize_speech()

    for book in books:
        if user_input and user_input.lower() in book["title"].lower():
            message = f"'{book['title']}' by {book['author']} is available."
            speak_text(message)
            return jsonify({"message": message})

    message = f"Sorry, I couldn’t find '{user_input}'."
    speak_text(message)
    return jsonify({"message": message})


if __name__ == "__main__":
    import os
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)

