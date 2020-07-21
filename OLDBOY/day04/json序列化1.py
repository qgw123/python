__author__ = 'qgw'

import pickle
def sayhi(name):
    print('hello,',name)

info = {'name': 'qgw', 'age': 22, 'func':sayhi}

f = open('test.txt', 'wb')

data = f.write(pickle.dumps(info))
pickle.dump(info, f)        #---> f.write(pickle.dumps(info))
print(data)