__author__ = 'qgw'

import json
import pickle

def sayhi(name):
    print('hello2',name)

f =  open('test.txt', 'rb')
# data = pickle.loads(f.read())
data =  pickle.load(f)
print(data["func"]("qgw"))
# print(data['age'])