from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

# from flask_wtf import FlaskForm
# from wtforms import StringField, EmailField, PasswordField, SubmitField
# from wtforms.validators import DataRequired
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import LoginManager
login_manager = LoginManager()

from forms_project import RegistrationForm, LoginForm
app = Flask(__name__, static_folder='static')
app.config['SECRET_KEY'] = 'secret-key-goes-here'

# CREATE DATABASE
class Base(DeclarativeBase):
    pass
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)
login_manager.init_app(app)

# CREATE TABLE IN DB
class User(db.Model, UserMixin):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))
 
with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated)




@app.route('/register', methods=['GET','POST'])
def register():
    form_register = RegistrationForm()
    if form_register.validate_on_submit():
        with app.app_context():
            # print(form_register.name.data)
            check_if_exists = User.query.filter_by(name=form_register.name.data).scalar()
            # print(check_if_exists)
            if check_if_exists == None:
                new_user = User(
                    email = form_register.email.data,
                    name = form_register.name.data,
                    password = generate_password_hash(password=form_register.password.data, method="pbkdf2:sha256", salt_length=8)
                )
                login_user(new_user)
                flash('Registration was successfully.')

                next = request.args.get('next')

                db.session.add(new_user)
                db.session.commit()
                # print("HERE ", form_register.name.data)
                return render_template('secrets.html', greetings_name=form_register.name.data)
            else:
                flash("Registration was not successfully!")
                return render_template(next or"register.html", form=form_register, already_exists = True)


    return render_template("register.html", form=form_register, logged_in=current_user.is_authenticated)

@login_manager.user_loader
def load_user(user_id):
    """
    This callback is used to reload the user object from the user ID stored in the session.
    """
    return db.get_or_404(User, user_id)

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        ### No need to create a new hash for entered password ###
        # password_as_hash = generate_password_hash(password=form.password.data, method="pbkdf2:sha256", salt_length=8)
        try:
            pw_db = User.query.filter_by(email=form.email.data).scalar().password
        except:
            pw_db = ""
        check_hash = check_password_hash(pwhash=pw_db, password=form.password.data)
        # print(check_hash)
        # print()

        check_user_in_db = User.query.filter_by(email=form.email.data).scalar()
        # print(check_user_in_db)
        if check_user_in_db and check_hash == True:
            # print(user_to_log_in)
            login_user(check_user_in_db)
            flash('Logged in successfully.')
            next = request.args.get('next')

            return redirect(url_for(next or 'home'))
        elif check_user_in_db == None:
            flash(message="No account with this email!")
            return render_template("login.html", form = form)
        elif check_hash == False:
            flash(message="Password is incorrect!")
            return render_template("login.html", form = form)
        
    return render_template("login.html", form = form, logged_in=current_user.is_authenticated)


@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html", logged_in=current_user.is_authenticated)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
@login_required
def download():
        return send_from_directory(
        directory=app.static_folder, path='files/cheat_sheet.pdf', as_attachment=False
    )


if __name__ == "__main__":
    app.run(debug=True)
