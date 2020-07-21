__author__ = 'qgw'
import json

import pickle

# def sayhi(name):
#     print('hello,',name)

# info = {'name': 'qgw', 'age': 22, 'func':sayhi}
info = {'name': 'qgw', 'age': 22, }

f = open('test.txt', 'w')
# data = pickle.dumps(info)
# data = f.write(pickle.dumps(info))
# data = json.dumps(info )
# data = f.write(json.dumps(info))

print(json.dumps(info))
json.dump(info, f)
# pickle.dump(info, f)  # f.write( pickle.dumps( info) )
# print(data)
f.close()
