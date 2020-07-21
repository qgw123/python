from random import  choice
# import  random
all_chs = '0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
result = ''
for i in range(10):
    ch = choice(all_chs)
    result += ch

print(result)