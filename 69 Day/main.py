from datetime import date
from flask import Flask, abort, render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from flask_gravatar import Gravatar
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user, login_required
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import  DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash

from flask_debugtoolbar import DebugToolbarExtension

# Import your forms from the forms.py
from forms import CreatePostForm, RegisterForm, LoginForm, CommentForm
from flask_login import LoginManager
login_manager = LoginManager()

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
ckeditor = CKEditor(app)
Bootstrap5(app)

gravatar = Gravatar(app,
                    size=100,
                    rating='g',
                    default='retro',
                    force_default=False,
                    force_lower=False,
                    use_ssl=False,
                    base_url=None)

# CREATE DATABASE
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)
login_manager.init_app(app)
toolbar = DebugToolbarExtension(app)

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from typing import List
# CONFIGURE TABLES
"""
Database schemas need to be defined early during the development process. 
Once an application has launched and accumulated lots of data, you will need to preserve this data by migrating to the new database.
"""

# Primary Key: Unique column which is not nullable
# Foreign Key: Usually references to the Primary Key, so we can have a relationship between the entries of the tables.


# TODO: Create a User table for all your registered users.
# # PARENT  
class User(db.Model, UserMixin):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String, unique=True)
    password: Mapped[str] = mapped_column(String)
    name: Mapped[str] = mapped_column(String, unique=True)

    posts: Mapped[List["BlogPost"]] = relationship(back_populates="author")

    # Child 1
    # One
    comments: Mapped[List["Comment"]] = relationship(back_populates="comment_author")


# # CHILD
class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

    # Parent
    # One Author -> Many Posts
    # 
    # Purpose of ForeignKey:  The author_id is the same as the users.id, because its an foreign key! (It represents the Primary Key)
    author_id: Mapped[int] = mapped_column(Integer, db.ForeignKey("users.id"))
    author: Mapped["User"] = relationship(back_populates="posts")
    # author = relationship("User", back_populates="posts")

    # Child, relationship to parent with attribute parent_post
    comments: Mapped[List["Comment"]] = relationship(back_populates="parent_post", passive_deletes=True)






class Comment(db.Model):
    __tablename__ = "comments"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    text: Mapped[str] = mapped_column(Text, nullable=False)

    # Parent 1
    # Many Comments --> To One user
    ### Many to one places a foreign key in the parent table referencing the child
    author_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))

    # comment_author: Mapped[List["User"]] = relationship(back_populates="comments")
    comment_author = relationship("User", back_populates="comments")

    # Parent 2
    # Many Comments --> To One BlogPost
    post_id: Mapped[str] = mapped_column(Integer, ForeignKey("blog_posts.id",  ondelete="CASCADE"))
    
    # parent_post: Mapped[List["BlogPost"]] = relationship(back_populates="comments")
    parent_post = relationship("BlogPost", back_populates="comments", passive_deletes=True)



with app.app_context():
    db.create_all()





@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)



# TODO: Use Werkzeug to hash the user's password when creating a new user.
@app.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm()
    # print(form.validate_on_submit())
    if form.validate_on_submit():
        check_user = User.query.filter_by(email=form.email.data).scalar()
        print(check_user)
        print()
        if check_user == None:
            hashed_pw = generate_password_hash(form.password.data, method="scrypt", salt_length=16)
            new_user = User(
                name = form.name.data,
                email = form.email.data,
                password = hashed_pw
            )
            db.session.add(new_user)
            db.session.commit()

            login_user(new_user)
            flash('Registration was sucessfull')


            return redirect(url_for('get_all_posts'))
        else:
            flash("You already signed in with that email, log in instead!")
            return redirect(url_for('login'))

    return render_template("register.html", form=form)


# TODO: Retrieve a user from the database based on their email. 
@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        check_user = User.query.filter_by(email=form.email.data).scalar()
        if check_user != None and check_password_hash(check_user.password, form.password.data):
            login_user(check_user)
            return redirect(url_for('get_all_posts'))
        elif check_user == None:
            flash("User does not exist!")
            return render_template('login.html', form=form, is_logged_in = current_user.is_authenticated)
        elif check_password_hash(check_user.password, form.password.data) == False:
            flash("Incorrect password!")
            return render_template('login.html', form=form, is_logged_in = current_user.is_authenticated)

    return render_template("login.html", form=form, is_logged_in = current_user.is_authenticated)

@app.route("/settings")
@login_required
def settings():
    pass

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('get_all_posts'))


from functools import wraps
def admin_only(function):
    @wraps(function)
    # https://stackoverflow.com/questions/308999/what-does-functools-wraps-do
    def wrapper(*args, **kwargs):
        # print("\n\n",kwargs)
        # print(args,"\n\n")
        # output_function = function()
        try:
            current_user_id = current_user.get_id()
            get_current_active_user = User.query.get(current_user_id)

            if get_current_active_user.name == "admin": 
                print(get_current_active_user.name)
                return function(**kwargs)
        except Exception as e:
           print(e)
           return abort(403)


    return wrapper

@app.route('/')
def get_all_posts():
    result = db.session.execute(db.select(BlogPost))
    posts = result.scalars().all()
    # print(dir(current_user))
    check_if_admin = False
    try:
        current_user_id = current_user.get_id()
        get_current_active_user = User.query.get(current_user_id)
        if get_current_active_user.name == "admin": check_if_admin = True
    except Exception as e:
        print(e)
        check_if_admin = False

    print(check_if_admin)
    return render_template("index.html", all_posts=posts, is_logged_in = current_user.is_authenticated, check_if_admin=check_if_admin)


# TODO: Allow logged-in users to comment on posts
@app.route("/post/<int:post_id>", methods=['GET', 'POST'])
def show_post(post_id):
    form = CommentForm()
    requested_post = db.get_or_404(BlogPost, post_id)
    if form.validate_on_submit() and requested_post:
        try:
            # Insert comment
            new_comment = Comment(
                author_id = current_user.get_id(),
                post_id = post_id,
                text = form.comment.data
            )

            db.session.add(new_comment)
            db.session.commit()

            return redirect(url_for('show_post', post_id=post_id))
        except Exception as e:
            print(e)
            return redirect(url_for('login'))

    get_comments_for_post = Comment.query.filter_by(post_id=post_id).all()
    # print(get_comments_to_post)
    # print(get_comments_to_post[0].text)

    return render_template("post.html", post=requested_post, is_logged_in = current_user.is_authenticated, form=form, comment_list=get_comments_for_post)


# TODO: Use a decorator so only an admin user can create a new post
@app.route("/new-post", methods=["GET", "POST"])
@admin_only
def add_new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.img_url.data,
            author=current_user,
            date=date.today().strftime("%B %d, %Y")
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=form, is_logged_in = current_user.is_authenticated)


# TODO: Use a decorator so only an admin user can edit a post
@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
@admin_only
def edit_post(post_id):
    post = db.get_or_404(BlogPost, post_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.author = current_user
        post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))
    return render_template("make-post.html", form=edit_form, is_edit=True, is_logged_in = current_user.is_authenticated)


# TODO: Use a decorator so only an admin user can delete a post
@app.route("/delete/<int:post_id>")
@admin_only
def delete_post(post_id):
    post_to_delete = db.get_or_404(BlogPost, post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    # print("HEREEE")
    return redirect(url_for('get_all_posts'))


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


# Configuration Admin
try:
    with app.app_context():
        hashed_pw = generate_password_hash("AdminPassword", method="scrypt", salt_length=16)
        admin_user = User(
            name = "admin",
            email = "admin@mail.com",
            password = hashed_pw

        )
        db.session.add(admin_user)
        db.session.commit()

        login_user(admin_user)
except Exception as e:
    print(f"This errors comes from autoreload=True.\nThe program tries to insert the row twiche.\n{e}")


if __name__ == "__main__":
    app.run(debug=True, port=5002)

