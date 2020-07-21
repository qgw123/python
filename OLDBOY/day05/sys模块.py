__author__ = 'qgw'

import sys

sys.argv        #命令行参数list，第一个元素是程序本身路径
sys.exit(n)     #退出程序，正常退出是exit(0)
sys.version     #获取python解释程序的版本信息
sys.maxint      #最大的int数
sys.path        #返回模块的搜索路径，初始化时使用PYTHONPATH环境变量
sys.platform    #返回操作系统平台名称

sys.stdout.flush()  #刷新
sys.stdout.write('please:')
val = sys.stdin.readline()[:-1]
