from flask import Flask, render_template, request
from pprint import pprint

app = Flask(__name__)

all_books = []

@app.route("/")
def home():
    return render_template('home.html', book_list = all_books)


@app.route("/add",methods=["GET", "POST"])
def add_book():
    if request.method == "POST":
        all_books.append(dict(request.form))
        # pprint(all_books)
    return render_template('add-book.html')



if __name__ == "__main__":
    app.run(debug=True)
    