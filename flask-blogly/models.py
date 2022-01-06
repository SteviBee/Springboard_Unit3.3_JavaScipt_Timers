"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class User(db.Model):
    """User Class"""

    __tablename__ = "users"

    id = db.Column(db.Integer,
                    primary_key=True,
                    autoincrement=True)
    first_name = db.Column(db.String(50),
                            nullable=False,
                            unique=True)
    last_name = db.Column(db.String(50),
                            nullable=False,
                            unique=True)
    image_url = db.Column(db.Text,
                            nullable=True,
                            default = "https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png")
   
    posts = db.relationship("Post", backref="user")
    
    def get_full_name(self):
        """"Retrives full user name"""

        return f"{self.last_name}, {self.first_name}"


class Post(db.Model):
    """post class"""
    
    __tablename__ = "posts"

    id = db.Column(db.Integer,
                    primary_key=True,
                    autoincrement=True)

    title = db.Column(db.String(50),
                    nullable=False)

    content = db.Column(db.Text)
    
    created_at = db.Column(db.DateTime, default=datetime.now)
  
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    # user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)


    def __repr__(self):
        p = self
        return f"<Post {p.id} {p.title} {p.content} {p.created_at} {p.user_id}>"

def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)