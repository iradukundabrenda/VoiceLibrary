from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Load books from JSON
with open("books.json", "r") as f:
    books = json.load(f)

def find_book(title):
    for book in books:
        if book["title"].lower() == title.lower():
            return book
    return None

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/borrow", methods=["POST"])
def borrow():
    data = request.get_json()
    title = data.get("title", "")
    book = find_book(title)
    if book:
        message = f"{book['title']} is available. Book borrowed successfully!"
    else:
        message = f"Sorry, '{title}' is not available."
    return jsonify({"message": message})

if __name__ == "__main__":
    app.run(debug=True)

