from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os


# initialize
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'db.sqlite')
app.config['SQLALCHAMEY_TRACK_MODIFICATIONS'] =False

# init DB
db = SQLAlchemy(app)

#init marshmallow
ma = Marshmallow(app)


class Topics(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    topic = db.Column(db.String(100),unique=True)

    def __init__(self,topic):
        self.topic =topic

# MCQ Schema
class TopicsSchema(ma.Schema):
    class Meta:
        #fields = ['id','topic' ]
        model =Topics
        



# MCQ class
class MCQ(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    question = db.Column(db.String(255),unique=True)
    answer = db.Column(db.String(255))
    topic = db.Column(db.Integer,db.ForeignKey('topics.id'))
    
    def __init__(self,question,answer,topic):
        self.question=question
        self.answer=answer
        self.topic=topic


# MCQ Schema
class MCQSchema(ma.Schema):
    class Meta:
        #fields = ['id','question','answer','topic' ]
        model =MCQ


