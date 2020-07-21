__author__ = 'qgw'

import random
from random import choice
from string import ascii_letters, digits
'''
num = ascii_letters + digits

def randpass(n=4):
    result = ''
    for i in range(n):
        ch = random.choice(num)
        result += ch

    return result

if __name__ == '__main__':
    print(randpass())
'''

'''
##验证码
checknum = ''
for i in range(4):
    current = random.randrange(0,4)
    if current == i:
        ch = chr(random.randint(65, 90))
    else:
        ch = random.randint(0,9)
    checknum += str(ch)

print(checknum)
'''

##猜数
'''
num = random.randint(1,101)
n = 0

while True:
    usernum = int(input('请猜一个数字（1-100）：'))
    n += 1
    if num == usernum:
        print('\033[32:1m你猜对了\033[0m')
        break
    elif usernum > num:
        print("\033[34;1m你猜大了\033[0m")
        continue
    else:
        print("\033[31;1m你猜小了\033[0m")
        continue

print('你一共猜对了：%s' % n)
'''