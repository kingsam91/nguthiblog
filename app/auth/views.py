from flask import render_template
from . import auth
from .forms import LoginForm


@auth.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()

    title = "Login"
    return render_template('auth/login.html', login_form=login_form, title=title)


@auth.route('/register', methods=["GET", "POST"])
def register():
    form = RegistrationForm()

    title = "New Account"
    return render_template('auth/register.html', registration_form=form, title=title)
