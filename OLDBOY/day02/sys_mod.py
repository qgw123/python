# import sys  #相当于位置变量

# print(sys.path)
# print(sys.argv[1])  #相当于是位置变量
# print(sys.argv[2])

import os       #用系统命令
# cmd = os.system('dir')
cmd = os.popen('dir').read()
# os.mkdir('day02')
# os.rmdir('day02')
# print(cmd)

#将字符转转为bytes用   encode
#将bytes转换为字符用   decode
msg = '我爱我家'
print(msg)
print(msg.encode(encoding='utf-8'))#将字符转换为bytes
print(msg.encode(encoding='utf-8').decode(encoding='utf-8'))#将bytes转换为字符