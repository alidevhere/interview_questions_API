import requests
import json
def add_tsv_file():
    fd = open('file.tsv','r',encoding='utf-8')
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
        
#add_tsv_file()
