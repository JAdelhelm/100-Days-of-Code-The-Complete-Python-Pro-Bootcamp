"""
An eCommerce website with payment processing.
"""

from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash

from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float, Boolean, select, update, delete, values, text, insert
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
import json
import pandas as pd
from flask import render_template, request
from sqlalchemy import func
import random 
import string
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

from flask_paginate import Pagination
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

from login import LoginForm

import stripe
# This is a public sample test API key.
# Don’t submit any personally identifiable information in requests made with this key.
# Sign in to see your own test API key embedded in code samples.
stripe.api_key = 'sk_test_Y17KokhC3SRYCQTLYiU5ZCD2'


login_manager = LoginManager()
API_KEY = ""


app = Flask(__name__,
            static_folder="./static",
            template_folder="./templates")



app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)
# CREATE DB
class Base(DeclarativeBase):
    pass


# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)
login_manager.init_app(app)

class User(db.Model, UserMixin):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(250),  nullable=False)
    permission: Mapped[int] = mapped_column(Integer, unique=True, nullable=True)
    items: Mapped[str] = mapped_column(String(2000), nullable=True, unique=True)




    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

# Creates Table with corresponding Table
with app.app_context():
    db.create_all()
    try:
        add_admin = User(username="admin",
                        password="password",
                        permission=99,
                        items="")
        db.session.add(add_admin)
        db.session.commit()
    except:
        print("Admin already added")

@login_manager.user_loader
def load_user(user_id):
    """
    This callback is used to reload the user object from the user ID stored in the session.
    """
    return db.get_or_404(User, user_id)

@app.route("/add/<int:id>")
def add_shop(id):
    picked_character = requests.get(f"https://rickandmortyapi.com/api/character/{id}").json()
    a_user = db.session.query(User).filter(User.id == current_user.get_id()).one()
    
    if str(id) not in a_user.items:
        add_id = f"{str(id)},"
        a_user.items += add_id
        db.session.commit()

        a_user = db.session.query(User).filter(User.id == current_user.get_id()).one()
        
        nr_items_list = a_user.items.split(",")[:-1]
        nr_items = len(nr_items_list)


        

        return redirect(url_for('home', nr_items = nr_items))
    else:
        a_user = db.session.query(User).filter(User.id == current_user.get_id()).one()

        nr_items_list = a_user.items.split(",")[:-1]
        nr_items = len(nr_items_list)

        return redirect(url_for('home', nr_items = nr_items))

@app.route('/logout')
def logout():
    if current_user.is_authenticated:
        logout_user()
        return redirect(url_for('home'))
    return redirect(url_for('home'))

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    print(form.validate_on_submit())

    if form.validate_on_submit():
        ### No need to create a new hash for entered password ###
        try:
            pw_db = User.query.filter_by(username=form.username.data).scalar().password
        except Exception as e:
            print(e)
            pw_db = ""


        check_user_in_db = User.query.filter_by(username=form.username.data).scalar()
        print(check_user_in_db)
        # print(check_user_in_db)
        if check_user_in_db and pw_db == form.password.data:
            # print(user_to_log_in)
            login_user(check_user_in_db)
            flash('Logged in successfully.')
            print("Logged in successfully!")
            next = request.args.get('next')

            return redirect(url_for(next or 'home'))
        elif check_user_in_db == None:
            flash(message="No account with this username!")
            print("No account with this username!")
            return render_template("login.html", form = form)
        elif pw_db != form.password.data:
            flash(message="Password is incorrect!")
            print("Password is incorrect!")
            return render_template("login.html", form = form)
        
    return render_template("login.html", form = form, logged_in=current_user.is_authenticated)

@app.route("/cart")
def cart():
    if current_user.is_authenticated:
        a_user = db.session.query(User).filter(User.id == current_user.get_id()).one()

        nr_items_list = a_user.items.split(",")[:-1]
        get_chars = requests.get(f"https://rickandmortyapi.com/api/character/{','.join(nr_items_list)}")
        get_chars_json = get_chars.json()
        # print(get_chars_json)

        nr_items = len(nr_items_list)
        return render_template('cart.html', show_characters= True, logged_in=current_user.is_authenticated, nr_items=nr_items, list_of_chars=get_chars_json)
    else:
        return render_template('cart.html', show_characters= True, logged_in=current_user.is_authenticated)    

@app.route('/create-checkout-session/<int:id>', methods=['POST', 'GET'])
def create_checkout_session(id):
    get_chars = requests.get(f"https://rickandmortyapi.com/api/character/{id}")
    get_chars_json = get_chars.json()

    name = get_chars_json["name"]
    img_url = get_chars_json["image"]


    checkout_session = stripe.checkout.Session.create(
        line_items=[{
                "price_data": {
                    "currency": "usd",
                    "product_data": {"name": name,
                                     "images": [img_url]},
                    "unit_amount": int(f"100"),
                },
                'quantity': 1,
            }],
        mode='payment',
        success_url=f"http://127.0.0.1:5000/",
        cancel_url="http://127.0.0.1:5000/",
    )
    return redirect(checkout_session.url, code=303)

@app.route('/', methods=['GET', 'POST'])
def home():

    if request.method == "POST":
        # print("POST REQ")
        return redirect(url_for('home'))
    
    random_20_chars = [str(random.randint(1,183)) for val in range(20)]
    # random_20_chars = [str(val) for val in range(20)]
    random_20_chars_str = ','.join(random_20_chars)
    get_chars = requests.get(f"https://rickandmortyapi.com/api/character/{random_20_chars_str}")
    get_chars_json = get_chars.json()
    if current_user.is_authenticated:
        a_user = db.session.query(User).filter(User.id == current_user.get_id()).one()

        nr_items_list = a_user.items.split(",")[:-1]
        nr_items = len(nr_items_list)
        return render_template('index.html', show_characters= True, list_of_chars=get_chars_json, logged_in=current_user.is_authenticated, nr_items=nr_items)
    else:
        return render_template('index.html', show_characters= True, list_of_chars=get_chars_json, logged_in=current_user.is_authenticated)       




if __name__ == "__main__":
    app.run(debug=True)