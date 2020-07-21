__author__ = 'qgw'
import shelve
import datetime

###############写入文件#################
d = shelve.open('shelve_test')     #打开一个文件
#
# name = ["alex","rain","test"]
# info = {'name': 'qgw', 'age': 22, }
#
# d['name'] = name
# d['info'] = info
# d['date'] = datetime.datetime.now()
#
# d.close()

############读取文件###############

d = shelve.open('shelve_test')

print(d.get('name'))
print(d.get('info'))
print(d.get('date'))