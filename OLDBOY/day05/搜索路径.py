__author__ = 'qgw'
import os
import  sys

path = os.path.abspath(__file__)           #查看文件当前目录
path1 =  os.path.dirname((os.path.abspath(__file__)))
path2 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

print(path)
print(path1)
print(path2)

data = sys.path.append(path2)
sys.path
print(sys.path)