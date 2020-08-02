from flask import render_template,request
from flask_login import login_required
from ..models import Post

from . import home


@home.route('/')
def index():

    rows = Post.get_posts()

    id = []
    title = []
    content = []
    image_url = []
    created_at = []


    for row in rows:
        id.append(row.id)
        title.append(row.title)
        content.append(row.content)
        image_url.append(row.image_url)
        created_at.append(row.created_at)

    mylist = zip(id, title, content, image_url, created_at)

    print(rows)

    return render_template('home/index.html', myposts=mylist)

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

@home.route('/post/<int:id>')
def single_post(id):
    """
    Render the dashboard template on the /dashboard route
    """

    return render_template('home/single_post.html', title="Post")


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




    
