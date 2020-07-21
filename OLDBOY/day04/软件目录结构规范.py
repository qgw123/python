__author__ = 'qgw'

'''
'''
import os
import sys
# print(os.path.abspath(__file__))     #查看当前文件的绝对路径
# print(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

print(sys.path)
