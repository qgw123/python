import getpass

_name = 'lol'
_pass = '123'

username = input('username: ')
password = getpass.getpass('passwoed: ')

if username == _name and _pass == password:
    print('登陆成功')
else:
    print('用户名或密码不正确')
print(username, password)