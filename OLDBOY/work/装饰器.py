__author__ = 'qgw'


user = 'qgw'
passwd = 'qgw123'

def auth(auth_type):
    print('auth func: ', auth_type)
    def out_wapper(func):
        def wapper(*args, **kwargs):
            if auth_type == 'local':
                username = input('Username: ')
                password = input('Password: ')
                if username == user and passwd == password:
                    print('\033[32qg;1m登陆成功\033[0m')
                    func(*args, **kwargs)
                else:
                    print('\033[31;1m登陆失败\033[0m')

            elif auth_type == 'ladp':
                print('什么情况的操作')


        return wapper
    return out_wapper


def index():
    print('hello index')

@auth(auth_type='local')
def home():
    print('hello home')

@auth(auth_type='ladp')
def ldap():
    print('hello ldap')

index()
home()
ldap()