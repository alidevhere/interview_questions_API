from flask import Flask,jsonify,request
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


# MCQ class
class MCQ(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    question = db.Column(db.String(255),unique=True)
    answer = db.Column(db.String(255))
    topic = db.Column(db.Integer,db.ForeignKey('topic.id'))
    
    def __init__(self,question,answer,topic):
        self.question=question
        self.answer=answer
        self.topic=topic



class Topics(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    topic = db.Column(db.String(100))

    def __init__(self,topic):
        self.topic =topic





# MCQ Schema
class TopicsSchema(ma.Schema):
    class Meta:
        fields = ['id','topic' ]

topic_schema = TopicsSchema()
topics_schema = TopicsSchema()#many=True,strict=True



# MCQ Schema
class MCQSchema(ma.Schema):
    class Meta:
        fields = ['id','question','answer','topic' ]

mcq_schema = MCQSchema()
mcqs_schema = MCQSchema()#many=True,strict=True


# Routes 
@app.route('/add/mcq/',methods=['POST'])
def add_mcq():
    new_mcq = MCQ(request.json['question'],request.json['answer'],request.json['topic'])
    db.session.add(new_mcq)
    db.session.commit()

    return MCQSchema.jsonify(new_mcq)


@app.route('/add/topic/',methods=['POST'])
def add_topic():
    new_topic = Topics(request.json['topic'])
    db.session.add(new_topic)
    db.session.commit()
    return MCQSchema.jsonify(new_topic)



@app.route('/all/topics/',methods=['GET'])
def view_all_topics():
    topics = Topics.query.all()
    return jsonify(topics)


#run server
if __name__ == '__main__':
    app.run(debug=True)