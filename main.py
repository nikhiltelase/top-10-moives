from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from sqlalchemy.exc import IntegrityError
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests


class Base(DeclarativeBase):
    pass


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6WlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movie_data.db"
api_key = "9d3c0ced"
bootstrap = Bootstrap5(app)
# CREATE DB
db = SQLAlchemy(model_class=Base)
db.init_app(app)


class Movie(db.Model):
    # CREATE TABLE
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String, unique=True)
    year: Mapped[int] = mapped_column(Integer)
    description: Mapped[str] = mapped_column(String)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String, nullable=True)
    img_url: Mapped[str] = mapped_column(String)


class EditRating(FlaskForm):
    # EDIT FORM
    rating = StringField("Your Rating Out of 10 eg. 7.5 ", validators=[DataRequired()])
    review = StringField("Your Review", validators=[DataRequired()])
    submit = SubmitField("Done")


class AddMovie(FlaskForm):
    # ADD FORM
    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    movies = db.session.execute(db.select(Movie).order_by(Movie.rating)).scalars()
    i = Movie.query.count()
    for movie in movies:
        movie.ranking = i
        db.session.commit()
        i -= 1
    ranking_movies = db.session.execute(db.select(Movie).order_by(Movie.rating)).scalars()
    return render_template("index.html", movies=ranking_movies)


@app.route("/edit", methods=['GET', 'POST'])
def edit():
    movie_id = request.args.get("id")
    movie = db.get_or_404(Movie, movie_id)
    form = EditRating()
    if form.validate_on_submit():
        data = form.data
        try:
            movie.rating = float(data['rating'])
        except ValueError:
            error = "rating would be a number 4, 4.5"
            return render_template("edit.html", movie=movie, form=form, error=error)

        movie.review = data['review']
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", movie=movie, form=form)


@app.route("/delete")
def delete():
    movie_id = request.args.get("id")
    movie = db.get_or_404(Movie, movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))


@app.route("/add", methods=['GET', 'POST'])
def add():
    form = AddMovie()

    if form.validate_on_submit():
        data = form.data
        title = data['title'].strip()
        return redirect(url_for('select', title=title))
    return render_template("add.html", form=form)


@app.route("/select/<title>")
def select(title):
    form = AddMovie()
    try:
        response = requests.get(f"http://www.omdbapi.com/?s={title}&apikey={api_key}")
        search_list = response.json()['Search']
        movie_list = []
        for search in search_list:
            if search['Type'] == "movie":
                movie_list.append(search)
    except KeyError:
        error = "Not found"
        return render_template("add.html", form=form, error=error)
    return render_template("select.html", list=movie_list)


@app.route("/save_movie")
def save_movie():
    movie_id = request.args.get("id")
    response = requests.get(f"http://www.omdbapi.com/?i={movie_id}&apikey={api_key}")
    movie_data = response.json()
    new_movie = Movie(
        title=movie_data['Title'],
        year=movie_data['Year'],
        description=movie_data['Plot'],
        rating=None,
        ranking=None,
        review=None,
        img_url=movie_data['Poster'],
    )
    db.session.add(new_movie)
    try:
        db.session.commit()
    except IntegrityError:
        return redirect(url_for('home'))

    return redirect(url_for('edit', id=new_movie.id))


if __name__ == '__main__':
    app.run(debug=True)
