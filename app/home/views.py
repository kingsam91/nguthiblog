from flask import render_template

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


        return render_template("home/add_post.html", title="Add Category", mycategories=mylist)
