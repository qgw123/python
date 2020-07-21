dict = {'qgw': '123456', 'qwe': 'qweqwe'}

username = input('Username: ')

# while True:
#     username = input('Username: ')
#     password = input('Password: ')
#     if dict[username] == password:
#         print('login scuccssful')
#         break
#     else:
#         print('false')
print(dict.get(username))
print(dict[username])