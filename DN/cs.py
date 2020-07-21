
import random
x = random.randint(1, 99)
a = 0
while  True:
    num = int(input('请随机输入一个数：'))
    a += 1
    if x == num:
        print("你猜对了！")
        break
    elif x < num:
        print("猜大了！")
    else:
        print("猜小了！")

# print("你总共才了{}次" .format(a))
print('你总共才了 %s 次' %  a)

if a > 8:
    print("你的智商已不足，请及时充值")

# import random
#
# answer = random.randint(1, 100)
# count = 0
# while True:
#     count += 1
#     number = int(input("请输入: "))
#     if number < answer:
#         print("大一点")
#     elif number > answer:
#         print("小一点")
#     else:
#         print("猜对了")
#         break
# print("您总共猜了{}次".format(count))
# if count > 7:
#     print("您的智商余额明显不足!!!")