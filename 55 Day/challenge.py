# %%
from flask import Flask
from decorators_challenge import *

app = Flask(__name__)

print(__name__)


@app.route('/')
@make_bold
def hello():
    return """
            <h1 style="text-align: center">Hello, World!</h1>
            <p>This is a paragraph</p>
            <img  src="https://www.strayz.de/cdn/shop/articles/brauchen-kitten-kittenfutter-strayz-blog-titel-kitten.jpg?v=1680241030" width=500>"""

@app.route("/bye")
def bye():
    return "Bye"


@app.route("/username/<name>/<int:number>")
def greet(name, number):
    print(type(name))
    print(type(number))
    return f"Hello {name}, your are {number} years old!"


# http://127.0.0.1:5000/username/Joerg
if __name__ == "__main__":
    # Script has to be runned in terminal
    app.run(debug=True)

# %%
