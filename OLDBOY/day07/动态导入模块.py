__author__ = 'qgw'

# modname = 'lia.aa'
mod = __import__('lib.aa')    # #这是解释器自己内部用的
obj = mod.aa.C()
print(obj.name)

###建议用下面这个方法
import importlib
lib = importlib.import_module('lib.aa')
print(lib.C().name)

obj = lib.C()
assert type(obj.name) is str  #断言assert
print('ddddd')