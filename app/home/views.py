from flask import render_template,request
from flask_login import login_required
from ..models import Post

from . import home


@home.route('/')
def index():
    return render_template('home/index.html')

@home.route('/add_post', methods=['GET', 'POST'])
def add_post_form():

    if request.method == 'POST':
        title = request.form.get('title')
        image_url = request.form.get('image_url')
        content = request.form.get('content')
        user_id = request.form.get('user_id')

        post = Post(title=title, image_url=image_url, content=content, user_id=user_id)
        post.save_post()

        return render_template("home/add_post.html", title="Add Post", message="Post added")

    return render_template("home/add_post.html")

@home.route('/dashboard')
@login_required
def dashboard():
    """
    Render the dashboard template on the /dashboard route
    """
    return render_template('home/dashboard.html', title="Dashboard")

@home.route('/profile/<int:id>')
def profile(id):    
    """
    Render the dashboard template on the /dashboard route
    """

    return render_template('home/profile.html', title="Profile")

@home.route('/new-post',  methods=['GET', 'POST'])
def new_post():
    """
    Render the dashboard template on the /dashboard route
    """
    if request.method == 'POST':
        title = request.form.get('title')
        image_url = request.form.get('image_url')
        content  = request.form.get('content')
        user_id = request.form.get('user_id')

        post = Post(title=title, image_url=image_url, content=content, user_id=user_id)
        post.save_post()

        return render_template('home/add_post.html', title="New Post", message="Post added.")


    return render_template('home/add_post.html', title="New Post")




    
