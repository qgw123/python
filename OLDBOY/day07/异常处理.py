__author__ = 'qgw'
'''
异常
    try :
        code
    except (Error1,Erro2) as e:
        print e

    except Exception :抓住所有错误，不建议用
https://www.cnblogs.com/wupeiqi/articles/5017742.html
'''

def bulk(self):
    print('%s is yelling ......' % self.name)

class Cat(object):
    def __init__(self,name):
        self.name = name

    def eat(self):
        print('%s is eatting ....' % self.name)

names = ['alex', 'jack']
dic = {'name':'alex'}
# names[3]
# dic['name']

# try :
#     names[3]
#     dic['name']
# except KeyError as e:
#     print('错误key: ', e)
# except IndexError as e:
#     print('列表错误: ',e)

# try :
#     names[3]
#     dic['name']
# except (IndexError,KeyError) as e:
#     print('错误key： ',e)
try:
    names[3]
    dic['name']

except Exception as e:      #可用在最后面，做未知的错误
    print('出错了',e)

else:                   #无错误执行
    print('正常')

finally:
    print('不管有没有错都执行')