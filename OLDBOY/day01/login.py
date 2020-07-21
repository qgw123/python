import getpass

name = 'qqq'
pass1 = '123456'

# username = input('请输入用户名：')
# passwoed = getpass.getpass('请输入密码： ')
n = 0
while n < 3:
    username = input('请输入用户名：')
    passwoed = getpass.getpass('请输入密码： ')
    if username == name  and passwoed == pass1:
        print('欢迎%s用户登陆成功' % username)
        break
    else:
        print('请输入正确的用户名或者密码')
    n += 1

if n == 3:
    print('用户{}已经锁定，因为已经输错三次' .format(username))

