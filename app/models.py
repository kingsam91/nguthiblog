from . import db, login_manager
import datetime
from flask import Flask,request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True, index=True)
    password_hash = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    posts = db.relationship('Post', backref='user', lazy="dynamic")


    pass_secure  = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cannnot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def save_user(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'User {self.username}'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    image_url = db.Column(db.String(255))
    title = db.Column(db.String(255))
    content = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow) 
    comments = db.relationship('Comment', backref='post', lazy='dynamic')   

    def save_post(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_posts(cls):
        rows = Post.query.all()
        return rows

    @classmethod
    def get_my_posts(cls, id):
        rows = Post.query.filter_by(user_id=id).all()
        return rows

class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    post_id = db.Column(db.Integer, db.ForeignKey("posts.id"))
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def save_comment(self):
        db.session.add(self)
        db.session.commit()