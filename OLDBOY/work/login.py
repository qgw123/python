__author__ = 'qgw'

'''
模拟用户登陆
'''
import getpass
userdb = {'qgw': '123456'}

def register():
    username = input("Username: ")
    if username not  in userdb:
        password = input('Password: ')
        userdb[username] = password
    else:
        print('\033[32;1m该%s用户已注册\033[0m' % username)

def login():
    username = input('Username: ')
    password = getpass.getpass('Password: ')
    if userdb.get(username) == password:
        print('\033[32;1m登陆成功\033[0m')
    else:
        print('\033[31;1m无效的用户名和密码\033[0m')

def show():
    cmds = {'0': register, '1': login}
    prompt = '''（0）注册
（1）登陆
（2）退出
请做出你的选择>>>>: '''

    while True:
        choice = input(prompt).strip()
        if choice not in ['0','1','2']:
            print('无效的选择，请重新选择')
        elif choice == '2':
            break

        cmds[choice]()

if __name__ == '__main__':
    show()

