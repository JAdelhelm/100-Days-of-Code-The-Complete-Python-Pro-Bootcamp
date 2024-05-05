from flask import Flask, render_template, url_for
import requests

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/home")
def home():
    image_url = url_for('static', filename='assets/img/home-bg.jpg')

    return render_template("index.html", image_url=image_url, json_with_posts=RESPONSE_BLOG)

@app.route("/about")
def about():
    image_url = url_for('static', filename='assets/img/about-bg.jpg')
    return render_template("about.html", image_url=image_url)

@app.route("/contact")
def contact():
    image_url = url_for('static', filename='assets/img/contact-bg.jpg')
    return render_template("contact.html", image_url=image_url)

@app.route("/post/<int:clicked_post_id>")
def blog_post(clicked_post_id):
    response_post_with_id = RESPONSE_BLOG[clicked_post_id-1]

    return render_template("post.html", id_of_post=response_post_with_id)

if __name__ == "__main__":
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    RESPONSE_BLOG = requests.get(blog_url).json()

    app.run(debug=True)