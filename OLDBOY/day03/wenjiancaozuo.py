
# data = open('yesterday', encoding='utf-8').read()
# data1 = open('yesterday1',encoding='utf-8')
# print(data)
# f = open('yesterday',encoding='utf-8' )
# f1 = open('yesterday1',encoding='utf-8')

with open('yesterday', 'rb' ) as f:
    data = f.read()
with open('yesterday2', 'wb') as fboj:
    data1 = fboj.write(data)
f.close()
fboj.close()
print(data1)

f = open('yesterday2', 'a', encoding='utf-8')
f.write('我爱你，我的家\n')
f.write('我的家啊\n我的天堂')
f.write('真的好吗')
print(f.tell())