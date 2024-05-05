#%%
from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap5
from website_forms import ContactForm

app = Flask(__name__,
            static_folder="./assets",
            template_folder="./html"
            )
bootstrap = Bootstrap5(app)

import os
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

@app.route("/", methods=["GET","POST"])
def home():
    most_stars_github_links = ["https://github.com/freeCodeCamp/freeCodeCamp", "https://github.com/EbookFoundation/free-programming-books", 
                               "https://github.com/sindresorhus/awesome", "https://github.com/public-apis/public-apis"]
    contact_form = ContactForm()

    if contact_form.validate_on_submit() == True:
        print(contact_form.data)
    

    return render_template('index.html', links=most_stars_github_links, form=contact_form)



if __name__ == "__main__":
    app.run(debug=True)

