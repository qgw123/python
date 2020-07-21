#计算1-100的偶数之和

re = 0
co = 0

while co <= 100:
    co += 1
    # if co % 2 == 1
    if co % 2 : #co除以2的值只有0或1 ：1是true，0是false
        continue

    re += co


print(re)