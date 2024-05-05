from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float, select, update, delete, values, text, insert
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
import json

from project_forms import MovieForm, AddMovieForm

API_KEY_MOVIES = ""

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

##CREATE DB
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


##CREATE TABLE
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String(250), nullable=True)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

with app.app_context():
    db.create_all()




first_movie = Movie(
    title="Phone Booth",
    year=2002,
    description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
    rating=7.3,
    ranking=10,
    review="My favourite character was the caller.",
    img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
)

second_movie = Movie(
    title="Avatar The Way of Water",
    year=2022,
    description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
    rating=7.3,
    ranking=9,
    review="I liked the water.",
    img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
)
def add_movie(new_movie):
    try:
        with app.app_context():
            db.session.add(new_movie)
            db.session.commit()
    except Exception as e:
        print(f"{'*'*10} Could not add the record: {new_movie.title} {'*'*10}")
        # print(f"Could not add the record: {e}")
print()
add_movie(first_movie)
add_movie(second_movie)
print()


def read_movies(app, db, table):
    """
    Read all reecords from table, then returning that dictionary wrapped by a list.
    """
    data_list = []  

    all_movies = select(Movie).order_by(Movie.ranking.desc(), Movie.rating.desc())
    all_movies = db.session.execute(all_movies).scalars()
    db.session.commit()

    for movie in all_movies:
        data_list.append({"id": movie.id, "title": movie.title, "year": movie.year,
                            "description": movie.description, "rating":movie.rating, "ranking":movie.ranking,
                            "review": movie.review, "img_url": movie.img_url})

    # print(data_list)
    return data_list


@app.route("/")
def home():
    movie_data = read_movies(app=app, db=db, table=Movie)
    return render_template("index.html", movie_data=movie_data)


@app.route("/edit/<title>", methods=['GET', 'POST'])
def edit_post(title):
    form = MovieForm()
    if request.method == "POST":
        if form.validate_on_submit():
            movie_to_update = update(Movie).where(Movie.title == title).values(rating=form.rating.data, review=form.review.data)
            db.session.execute(movie_to_update)
            db.session.commit()

            return redirect(url_for('home'))
        else:
            return render_template("edit.html", title=title, form=form)

    return render_template("edit.html", title=title, form=form)


@app.route("/delete/<title>", methods=['GET'])
def delete_post(title):
    movie_to_delete = delete(Movie).where(Movie.title == title)
    db.session.execute(movie_to_delete)
    db.session.commit()

    return redirect(url_for('home'))


@app.route('/add', methods=["GET", "POST"])
def add_post():
    form = AddMovieForm()
    print(request.method)
    if form.validate_on_submit():
        url = f"https://api.themoviedb.org/3/search/movie?query={form.title.data}"
        headers = {"accept": "application/json",
                   "Authorization": f"Bearer {API_KEY_MOVIES}"}
        response = requests.get(url, headers=headers)

        response_to_dict = json.loads(response.text)
        print(response_to_dict,"\n\n")
        # print(response_to_dict.keys(),"\n\n")

        response_to_dict_results = response_to_dict["results"]
        # print(len(response_to_dict_results),"\n\n")

        return render_template('select.html', response_movies=response_to_dict_results)

    return render_template('add.html', form=form)

@app.route('/add/<movie_title>')
def add_new_post(movie_title, methods=['GET']):
    print(movie_title)
    url = f"https://api.themoviedb.org/3/search/movie?query={movie_title}"
    headers = {"accept": "application/json",
                "Authorization": f"Bearer {API_KEY_MOVIES}"}
    response = requests.get(url, headers=headers)

    response_to_dict = json.loads(response.text)["results"][0]
    

    newMovie = Movie(
        # id= response_to_dict['id'],
        title = response_to_dict['title'],
        review = f"Original Language: {response_to_dict['original_language']}",
        year = response_to_dict['release_date'],
        description = response_to_dict['overview'],
        rating = response_to_dict['vote_average'],
        ranking = response_to_dict['popularity'],
        img_url=f"https://image.tmdb.org/t/p/w500{response_to_dict['poster_path']}"
    )
    db.session.add(newMovie)
    db.session.commit()


    return redirect(url_for('home'))




if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)   