
info = { 'stu1101': 'TengLan Wu',
         'stu1102': 'Lao ',
         'stu1103': 'cangjinkong'}

print(info)
info['stu1104'] = 'wutenglan'
print(info.get('stu1101'))
print(info['stu1102'])
print(info['stu1103'])
# del info['stu1101']       #删
# info.pop('stu1101')
# info.popitem()
print(info)
for i in info:
    print(i, info[i])

for key,item in info.items():
    print(key,item)