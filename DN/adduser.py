import subprocess ##调用系统命令
import string
import sys      ##调用位置变量模块

# username = input('请输入想要创建的用户名： ')
from random import choice
# from string import ascii_letters, digits
# f = string.ascii_letters
# d = string.digits
all_chs = string.ascii_letters + string.digits

def randpass(n=8):
    result = ''
    for i in range(n):
        ch = choice(all_chs)
        result += ch

    return result

def adduser(username,password,fname):
    info = '''user info:
username: %s
password: %s
''' % (username .password)
    subprocess.run('useradd %s' % username  ,shell=True)
    subprocess.run(
        'echo %s | passwd --stdin %s' % (password,username),
        shell=True)
    with open(fname, 'a') as fobj:
        fobj.write(info)

if __name__ == '__main__':
    # username = sys.argv[1]
    username = input('请输入创建的用户名：')
    password = randpass()
    fname = '/tmp/user.txt'
    adduser(username,password,fname)
