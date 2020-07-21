__author__ = 'qgw'

'''
生成器只有在调用时才会生成相应的数据
只记录当前位置
只有一个__next__()方法
'''

#yielb 生成器标识

'''
可以直接作用于for循环的数据类型有一下几种：
1、集合数据类型：如list 、tuple、dict、set、str等；
2、generator，包括生成器和带yield的generator function。
这些可以直接作用于for循环的对象统称为可迭代对象：Iterable。
可以使用isinstance()判断一个对象是否是Iterable对象
'''

'''
迭代器：可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator
'''

# 生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。
# 把list、dict、str等Iterable变成Iterator可以使用iter()函数

# range()本身就是一个迭代器

