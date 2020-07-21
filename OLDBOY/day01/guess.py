import random

num = random.randint(1, 100)
n = 0

while True:
    nums = int(input('请猜一个数： '))
    n += 1
    if num == nums:
        print('你猜对了')
        break
    elif num > nums:
        print('你猜小了')
    else:
        print('你猜大了')

# print('你总共猜对了{}次' .format(n))
print('你总共猜对了%s次' % n)
print('你总共猜对了{_n}次' .format(_n=n))

if n > 8:
    print('你的智商不足，请充值')