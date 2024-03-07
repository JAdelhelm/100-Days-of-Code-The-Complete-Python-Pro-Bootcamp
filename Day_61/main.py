from flask import Flask, render_template, request
from login import LoginPage
from flask_bootstrap import Bootstrap5
import os

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''



app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods =["GET", "POST"])
def login():
    login_page = LoginPage()
    print(login_page.validate_on_submit())
    if request.method == "POST":
        if login_page.validate_on_submit():
            return render_template('success.html')
        else: 
            return render_template('denied.html')
    else:
        return render_template('login.html', form=login_page)


if __name__ == '__main__':
    bootstrap = Bootstrap5(app)

    SECRET_KEY = os.urandom(32)
    app.config['SECRET_KEY'] = SECRET_KEY   
    app.run(debug=True)
