from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["GET","POST"])
def login():
    print(request.method)
    if request.method == 'POST':
        username = request.form["username"]
        password = request.form["password"]
        return  f"<h1>This is a POST:</h1>"\
                f"<h3> Username: {username} </h3>"\
                f"<h3> Password: {password} </h3>"
    else:
        return "GET"


if __name__ == "__main__":
    app.run(debug=True)