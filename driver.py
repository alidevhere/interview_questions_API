import requests
import json


def add_tsv_file(file):
    fd = open(file,'r',encoding='utf-8')
    text = fd.readlines()
    for line in text:
        line = line.split('    ')
        line = [l.replace('\n','') for l in line]
        if len(line) != 2:
            print(line)
            break
        q = line[0]
        ans=line[1]
        print('Sending...')
        d= {"question":q,'answer':ans,"topic":1}
        d= json.dumps(d)
        print(d)
        r = requests.post('http://127.0.0.1:5000/add/question/',json=d)
        print(r)
        
#add_tsv_file('file.tsv')


def add_question(ques,ans,topic_id):
    dic = {}
    dic['question']= ques
    dic['answer'] = ans
    dic['topic'] = topic_id
    dic = json.dumps(dic)
    print(dic)
    r = requests.post('http://127.0.0.1:5000/add/question/',json=dic)
    print(r)

'''
data = {
'questions_list':[{'question':'What is the need for OOPs?','answer':'There are many reasons why OOPs is mostly preferred, but the most important among them are: OOPs helps users to understand the software easily, although they don’t know the actual implementation.With OOPs, the readability, understandability, and maintainability of the code increase multifold.Even very big software can be easily written and managed easily using OOPs.'},
{'question':'What are some major Object Oriented Programming languages?','answer':'The programming languages that use and follow the Object-Oriented Programming paradigm or OOPs, are known as Object-Oriented Programming languages. Some of the major Object-Oriented Programming languages include: Java,C++,Javascript,Python,PHP'},
{'question':'What are some other programming paradigms other than OOPs?','answer':'Programming paradigms refers to the method of classification of programming languages based on their features. There are mainly two types of Programming Paradigms: Imperative Programming Paradigm,Declarative Programming Paradigm'}],
'count':3,
'topic_id':1
}
'''

def add_questions(data):
    print(data)
    r = requests.post('http://127.0.0.1:5000/add/questions/',json=data)
    print(r)

#add_questions(data)
#def get_all_mcq(id):
    

