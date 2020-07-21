# import sys  #相当于位置变量

# print(sys.path)
# print(sys.argv[1])  #相当于是位置变量
# print(sys.argv[2])

import os       #用系统命令
# cmd = os.system('dir')
cmd = os.popen('dir').read()
# os.mkdir('day02')
os.rmdir('day02')
print(cmd)