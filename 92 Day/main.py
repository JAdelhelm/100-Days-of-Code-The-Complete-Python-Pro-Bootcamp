from flask import Flask, render_template, redirect, url_for, request, flash
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


import os
from flask import send_from_directory
from uploadForms import *
from werkzeug.utils import secure_filename
UPLOAD_FOLDER = './static'
ALLOWED_EXTENSIONS = { 'png', 'jpg', 'jpeg'}


app = Flask(__name__,
            static_folder="./static",
            template_folder="./templates")
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            send_from_directory(app.config["UPLOAD_FOLDER"], filename)


            return redirect(url_for('process_image', name=filename))
            
    return render_template("index.html")


@app.route('/image/<name>')
def process_image(name):
    from PIL import Image
    import numpy as np
    import scipy.cluster
    import sklearn.cluster

    image = Image.open(f"./static/{name}")
    image_np = np.asarray(image)
    shape = image_np.shape

    image_np = image_np.reshape(np.product(shape[:2]), shape[2]).astype(float)

    kmeans = sklearn.cluster.MiniBatchKMeans(
        n_clusters=10,
        init="k-means++",
        max_iter=5,
        random_state=1000
    ).fit(image_np)

    codes = kmeans.cluster_centers_

    vecs, _dist = scipy.cluster.vq.vq(image_np, codes)         # assign codes
    counts, _bins = np.histogram(vecs, len(codes))    # count occurrences

    colors = []
    for index in np.argsort(counts)[::-1]:
        colors.append(tuple([int(code) for code in codes[index]]))

    print(colors)


    return render_template("index.html", colors=colors, image_colors_available=True)
             


if __name__ == "__main__":
    app.run(debug=True)