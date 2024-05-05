from flask import Flask, render_template, redirect, url_for, request
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

from flask_paginate import Pagination

from add_cafe import CafeAdd

app = Flask(__name__,
            static_folder="./static",
            template_folder="./html")
API_KEY_MOVIES = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI3NDRlNjMyMTc1ZDJhNzVmYjdiYzMxMmVmMDJkMGMwYiIsInN1YiI6IjY1ZTk5MjFjNmJlYWVhMDE4NjdhMDU1NSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.8J2FCQc-HS3sOVf0WMcyDn9v9ITAHjB5U2ipzQlNJdk"

app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}





from flask import render_template, request
from sqlalchemy import func

@app.route("/", methods=["GET", "POST"])
def home():
    # Define the number of cafes per page
    per_page = 8
    # Get the current page from the request arguments
    page = request.args.get('page', 1, type=int)
    # Query to count the total number of cafes
    total_cafes = Cafe.query.count()
    # Paginate the cafes query to get the cafes for the current page
    cafes = Cafe.query.order_by(Cafe.id).paginate(page=page, per_page=per_page, error_out=False)

    return render_template("index.html", cafes=cafes)

@app.route("/delete<int:id>")
def delete_cafe(id):
    cafe_object = Cafe.query.filter_by(id=id).one()
    # print(cafe_object)

    db.session.delete(cafe_object)
    db.session.commit()

    return redirect(url_for('home'))

@app.route("/add", methods=["GET","POST"])
def add_cafe():
    import string
    import random

    form = CafeAdd()
    print(request.method)
    # print(form.validate())
    if form.validate() == True:
        print(form.data)
        newCafe = Cafe(name = form.data["name"],
                       map_url = form.data["map_url"],
                       img_url = form.data["img_url"],
                       location = form.data["location"],
                       has_sockets = form.data["has_sockets"], 
                       has_toilet = form.data["has_toilet"],
                       has_wifi = form.data["has_wifi"],
                       can_take_calls = form.data["can_take_calls"],
                       seats = form.data["seats"],
                       coffee_price = form.data["coffee_price"])

        db.session.add(newCafe)
        db.session.commit()

        return redirect(url_for('home'))
    

    random_cafe_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
    return render_template("add_cafe.html", form=form,
                           testing=True, random_cafe_name=random_cafe_name)


if __name__ == "__main__":
    app.run(debug=True)