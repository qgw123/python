__author__ = 'qgw'
import random
print(random.randint(1, 99))
print(random.randrange(3))  #不包含3
print(random.choice('qxhsbeviagna'))
print(random.sample('qwert', 2))

item = [1, 2, 3 ,4 ,5, 6]
random.shuffle(item)
print(item)

