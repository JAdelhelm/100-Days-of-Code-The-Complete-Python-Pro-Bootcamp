from flask import Flask, render_template, redirect, url_for, jsonify, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text, update
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date

from datetime import datetime
# from time import strftime

from form_project import PostForm

'''
Make sure the required packages are installed: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from the requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)
ckeditor = CKEditor(app)

# CREATE DATABASE
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


with app.app_context():
    db.create_all()


@app.route('/')
def get_all_posts():
    # TODO: Query the database for all the posts. Convert the data to a python list.
    all_rows_as_list = BlogPost.query.all()
    # print(all_rows_as_list)
    posts = [blog.to_dict() for blog in all_rows_as_list]
    # print(posts)
    return render_template("index.html", all_posts=posts)

# TODO: Add a route so that you can click on individual posts.

@app.route('/<post_id>', methods=["GET","POST"])
def show_post(post_id):
    # TODO: Retrieve a BlogPost from the database based on the post_id
    requested_post = BlogPost.query.get(post_id)
    # print(requested_post)
    return render_template("post.html", post=requested_post)


# TODO: add_new_post() to create a new blog post
@app.route("/new__post", methods=['GET','POST'])
def make_new_post():
    form = PostForm()
    print(form.validate_on_submit())
    if form.validate_on_submit():
        today = datetime.now()
        new_blog_post = BlogPost(
            title = form.title.data,
            date = today.strftime("%B %d,%Y"),
            body = form.body.data,
            author = form.author.data,
            img_url = form.img_url.data,
            subtitle = form.subtitle.data
            
        )
        db.session.add(new_blog_post)
        db.session.commit()
        print(new_blog_post)

        return redirect(url_for('get_all_posts'))

    return render_template("make-post.html", form=form, post = None)


# TODO: edit_post() to change an existing blog post
@app.route("/edit-post/<post_id>", methods=["GET", "POST"])
def edit_selected_post(post_id):
    # print(request.methods)
    requested_post = BlogPost.query.get(post_id)
    form = PostForm()
    print(form.validate_on_submit())
    print(form.errors)
    if form.validate_on_submit():
        blog_post_to_change = BlogPost.query.filter_by(id=post_id)
        # print(blog_post_to_change)
        if blog_post_to_change:
            blog_post_to_change = blog_post_to_change.update(dict(
            title = form.title.data,
            date = requested_post.date,
            body = form.body.data,
            author = form.author.data,
            img_url = form.img_url.data,
            subtitle = form.subtitle.data
            ))


            db.session.commit()
            return redirect(url_for('show_post', post_id=post_id))
        else:
            return jsonify(error={"No Blog post with that id."})

    form.body.data = requested_post.body

    # print(post_id)
    return render_template('make-post.html', post=requested_post, form=form)
# redirect(url_for('get_all_posts'))

# TODO: delete_post() to remove a blog post from the database
@app.route("/delete/<post_id>")
def delete_blog_post(post_id):
    get_to_delete_post = BlogPost.query.get(post_id)
    if get_to_delete_post:
        db.session.delete(get_to_delete_post)
        db.session.commit()
        return redirect(url_for('get_all_posts'))
    return redirect(url_for('get_all_posts'))
        

# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
