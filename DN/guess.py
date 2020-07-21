import random

num = random.randint(1,3)
guess = int(input('请输入一个数字：'))

if num > guess :
    print('猜小了')
elif num < guess:
    print('猜大了')
else:
    print('猜对了')

print('正确的数字：', num)
