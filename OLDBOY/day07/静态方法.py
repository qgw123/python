__author__ = 'qgw'

'''
静态方法
    只是名义上归类管理，实际上在静态方法里访问不了类或实例中的任何属性
'''



class Dog(object):
    def __init__(self,name):
        self.name = name

    @staticmethod   #实际上跟类没什么关系来
    def eat(self):
        print('%s is eatting %s' % (self.name, 'dd'))


d = Dog('alex')
d.eat(d)
# Dog.eat(d)
