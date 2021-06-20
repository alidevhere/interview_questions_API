from flask import jsonify,request
from models import *
import json as js
topic_schema = TopicsSchema()
topics_schema = TopicsSchema(many=True)#strict=True

mcq_schema = QuestionSchema()
mcqs_schema = QuestionSchema(many=True)#strict=True


# Routes 
@app.route('/add/question/',methods=['POST'])
def add_ques():
    #print('DICT+++++++++++',request.json)
    dic = request.json
    if type(dic) == str:
        print('string...converting to json ...')
        dic = js.loads(dic)
        print(type(dic))
    #print(type(request.json))
    q = dic['question']
    ans = dic['answer']
    t_id = dic['topic']
    print(q,ans,t_id)
    new_ques = Question(q,ans,t_id)
    
    try:
        db.session.add(new_ques)
        db.session.commit()
        return jsonify({'success':True,'msg':'Successfully added Question !!'})
    except:
        return jsonify({'success':False,'msg':'Error in adding Question !!'})


@app.route('/add/topic/',methods=['POST'])
def add_topic():
    #new_topic = Topics(request.json['topic'])
    new_topic = Topics(request.json['topic'])
    try:
        db.session.add(new_topic)
        db.session.commit()
        return jsonify({'success':True,'msg':'Successfully added !!'})
    except:
        return jsonify({'success':False,'msg':'Error in adding Topic !!'})
    
    

@app.route('/topic/<int:t>/count/',methods=['GET'])
def topic_questions_count(t):
    topic = Topics.query.get(t)
    return jsonify({'topic_id':topic.id, 'topic_name':topic.topic,'question_count': topic.total_questions})



@app.route('/all/topics/',methods=['GET'])
def view_all_topics():
    topics = Topics.query.all()
    topics_list=[t.to_json for t in topics]
    for t in topics:
        print(t.id)
        print(t.topic)
    return jsonify({'total_topics':len(topics),'all_topics':topics_list})



#run server
if __name__ == '__main__':
    app.run(debug=True)

