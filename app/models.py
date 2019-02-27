from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    pitches = db.relationship('Pitch',backref = 'pitch',lazy="dynamic")
    comments = db.relationship('Comment',backref = 'user',lazy = "dynamic")
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))

    
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)


    def __repr__(self):
        return f'User {self.username}'
    
class Pitch(db.Model):
    __tablename__ = 'pitches'

    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(255))
    name = db.Column(db.String(255))
    category = db.Column(db.String(255))
    pitch_content = db.Column(db.String(255))  
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    upvote = db.Column(db.Integer)
    downvote = db.Column(db.Integer)
    published_at = db.Column(db.DateTime, default = datetime.utcnow)
    comments = db.relationship('Comment',backref = 'comment',lazy = "dynamic")


    def __repr__(self):
        return f'User {self.name}'

class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    published_at = db.Column(db.DateTime, default = datetime.utcnow)
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
   

    def __repr__(self):
        return f'User {self.name}'

