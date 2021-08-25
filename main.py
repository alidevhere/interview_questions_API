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
    dic = request.json
    if type(dic) == str:
        print('string...converting to json ...')
        dic = js.loads(dic)
        print(type(dic))
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



@app.route('/add/questions/',methods=['POST'])
def add_bulk_ques():
    questions=request.json['questions_list']
    t_id = request.json['topic_id']
    for q in questions:
       ques= q['question']
       ans = q['answer']
       new_q = Question(ques,ans,t_id)
       db.session.add(new_q)
       db.session.commit()
       print('added..')
    return 'success'


@app.route('/add/topic/',methods=['POST'])
def add_topic():
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


@app.route('/all/questions/<int:id>/',methods=['GET'])
def get_questions(id):
    data = Question.query.filter(Question.topic == id).all()
    data = [d.to_json for d in data]
    return jsonify(data)



@app.route('/help/',methods=['GET'])
def help():
    paths={}
    paths['/all/questions/<int:id>/']='returns all questions of specified topic id'
    paths['/all/topics/']='returns list of all topics'
    paths['/topic/<int:t>/count/']='returns count of questions of specified topic id'
    paths['/add/topic/']='POST request to add a topic into api DB,provide json in format : {"topic":"OOP"} e.g "topic" is key'
    paths['/add/question/']='POST request for adding questions e.g {"question":"Question statement","answer":"Correct answer","topic":"any topic name" }'
    paths['/add/questions/']='''POST request for adding many questions in single request.Provide dictionary in format
{'questions_list':[{'question':'question no 1','answer':'ans no 1'},{'question':'question no 2','answer':'ans no 2'},{'question':'question no 3','answer':'ans no 3'}],
'count':3,
'topic_id':1}'''
    return paths




data = {
'questions_list':[{'question':'What is the need for OOPs?','answer':'There are many reasons why OOPs is mostly preferred, but the most important among them are: OOPs helps users to understand the software easily, although they don’t know the actual implementation.With OOPs, the readability, understandability, and maintainability of the code increase multifold.Even very big software can be easily written and managed easily using OOPs.'},
{'question':'What are some major Object Oriented Programming languages?','answer':'The programming languages that use and follow the Object-Oriented Programming paradigm or OOPs, are known as Object-Oriented Programming languages. Some of the major Object-Oriented Programming languages include: Java,C++,Javascript,Python,PHP'},
{'question':'What are some other programming paradigms other than OOPs?','answer':'Programming paradigms refers to the method of classification of programming languages based on their features. There are mainly two types of Programming Paradigms: Imperative Programming Paradigm,Declarative Programming Paradigm'}],
'count':3,
'topic_id':1
}
#run server
if __name__ == '__main__':
    app.run(debug=True)

