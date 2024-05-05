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
from flask import render_template, request
from sqlalchemy import func
import random 
import string

from flask_paginate import Pagination
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

from todoforms import ToDoAdd

app = Flask(__name__,
            static_folder="./static",
            template_folder="./templates")
API_KEY_MOVIES = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI3NDRlNjMyMTc1ZDJhNzVmYjdiYzMxMmVmMDJkMGMwYiIsInN1YiI6IjY1ZTk5MjFjNmJlYWVhMDE4NjdhMDU1NSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.8J2FCQc-HS3sOVf0WMcyDn9v9ITAHjB5U2ipzQlNJdk"

app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# CREATE DB
class Base(DeclarativeBase):
    pass

engine = create_engine("sqlite:///todo.db")
if not database_exists(engine.url):
    create_database(engine.url)
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


class ToDo(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    description: Mapped[str] = mapped_column(String(2000), nullable=False)
    finished: Mapped[bool] = mapped_column(Boolean, nullable=False)


    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

# Creates Table with corresponding Table
with app.app_context():
    db.create_all()


@app.route("/delete/<int:id>")
def delete_todo(id):
    obj = ToDo.query.filter_by(id=id).one()
    db.session.delete(obj)
    db.session.commit()
    return redirect(url_for('home'))

@app.route("/finished/<int:id>")
def finished_todo(id):
    # print(id)
    obj = ToDo.query.filter_by(id=id).one()
    obj.finished = True
    db.session.commit()
    return redirect(url_for('home'))

@app.route("/", methods=["GET", "POST"])
def home():
    form = ToDoAdd()
    if form.validate():
        new_task = ToDo(
            name = form.name.data,
            description = form.description.data,
            finished = False
        )
        db.session.add(new_task)
        db.session.commit()

        return redirect(url_for('home'))

    per_page = 6
    page = request.args.get('page', 1, type=int)
    total_todo = ToDo.query.count()
    todo_list = ToDo.query.order_by(ToDo.id).paginate(page=page, per_page=per_page, error_out=False)
    # print(todo_list)

    # Testing autofills the form
    testing = True
    if testing == True:
        form.name.data = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        form.description.data = "Example description"



    return render_template("index.html", todo_list=todo_list, total_todo=total_todo, form = form, testing=testing)

@app.route("/add", methods=["GET","POST"])
def add_todo():
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)