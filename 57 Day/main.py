from flask import Flask, render_template
import requests
import json 
from pprint import pprint

app = Flask(__name__)

API_ENDPOINT_BLOG = ""

def api_endpoint_blog():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url).json()
    return response

# @app.route('/post/<int:id>')
# def blog_post(id):
#     return render_template("post.html", post=api_endpoint_blog()[id])


@app.route('/blog')
def blog():
    return render_template('post.html', api_blog=api_endpoint_blog())

@app.route('/post/<recent_id>')
def blog_post(recent_id):
    id_to_int = int(recent_id)
    json_from_api = api_endpoint_blog()[id_to_int-1]
    return render_template('post_detail.html', api_blog_with_id=json_from_api)


@app.route('/')
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
