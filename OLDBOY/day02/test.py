import copy

person = ['qwe', ['saving', 1000]]
'''
p1 = copy.copy(person)
p2 = person[:]
p3 = list(person)
'''
p1 = person[:]
p2 = person[:]

p1[0] = 'qwe'
p2[0] = 'qizi'

p1[1][1] = 500

print(p1)
print(p2)
