from flask import jsonify,request
from models import *

topic_schema = TopicsSchema()
topics_schema = TopicsSchema(many=True)#strict=True
#mcq_schema = MCQSchema()
#mcqs_schema = MCQSchema(many=True)#strict=True


# Routes 
@app.route('/add/mcq/',methods=['POST'])
def add_mcq():
    new_mcq = MCQ(request.json['question'],request.json['answer'],request.json['topic'])
    db.session.add(new_mcq)
    db.session.commit()

    return MCQSchema.jsonify(new_mcq)


@app.route('/add/topic/',methods=['POST'])
def add_topic():
    #new_topic = Topics(request.json['topic'])
    new_topic = Topics(request.json['topic'])
    db.session.add(new_topic)
    db.session.commit()
    #return topic_schema.dump(new_topic)
    return jsonify({'success':True,'msg':'Successfully added !!'})



@app.route('/all/topics/',methods=['GET'])
def view_all_topics():
    topics = Topics.query.all()
    return jsonify(topics)


#run server
if __name__ == '__main__':
    app.run(debug=True)

