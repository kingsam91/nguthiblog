from flask import render_template,flash,redirect,request, url_for
from . import auth
from ..models import User
from flask_login import login_user, login_required, logout_user
from .forms import LoginForm, RegistrationForm


@auth.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email=login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user, login_form.remember.data)

            return redirect(url_for('home.dashboard'))

        flash('Invalid username or Password')

    title = "Login"
    return render_template('auth/login.html', login_form=login_form, title=title)


@auth.route('/register', methods=["GET", "POST"])
def register():
    form = RegistrationForm()

    title = "New Account"


    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data, password=form.password.data)
        user.save_user()

        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', registration_form=form, title=title)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been successfully logged out')
    return redirect(url_for("home.index"))