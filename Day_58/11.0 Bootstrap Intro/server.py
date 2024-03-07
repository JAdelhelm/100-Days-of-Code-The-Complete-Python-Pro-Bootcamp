from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")



if __name__ == "__main__":
    app.run(debug=True)
    # print(app.url_defaults)


# Exercises https://appbrewery.github.io/bootstrap-layout/
    # the underyling classes should behave like the classes above