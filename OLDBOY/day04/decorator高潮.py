__author__ = 'qgw'

import getpass

user = 'qgw'
passwd = '123456'


def auth(auth_type):
    print("auth func:", auth_type)

    def out_wrapper(func):
        def wrapper(*args, **kwargs):
            if auth_type == 'local':
                username = input('Username: ').strip()
                #  password = getpass.getpass('Password: ')
                password = input('Password: ').strip()
                if username == user and passwd == password:
                    print('\033[32;1m欢迎登陆\033[0m')
                    res = func(*args, **kwargs)
                    print(res)
                else:
                    exit('\033[31;1m无效的用户名或者密码\033[0m')

            elif auth_type == 'ldap':
                print('搞毛线啊，不会。。。。')

        return wrapper

    return out_wrapper


def index():
    print('Welcome index')


@auth(auth_type='local')  # home = wrapper()
def home():
    print('Welcome home')
    return "home is si "


@auth(auth_type='ldap')
def bbs():
    print('Welcome bbs')


index()
home()
bbs()
