from flask import Flask, render_template, request, jsonify
import json

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

    # Skip voice input for cloud deployment
    # if user_input == "voice":
    #     from voice_utils import recognize_speech
    #     user_input = recognize_speech()

    # Search books
    for book in books:
        if user_input.lower() in book["title"].lower():
            message = f"'{book['title']}' by {book['author']} is available."
            # Skip text-to-speech for cloud
            # from voice_utils import speak_text
            # speak_text(message)
            return jsonify({"message": message})

    message = f"Sorry, I couldn’t find '{user_input}'."
    # speak_text(message)
    return jsonify({"message": message})

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

