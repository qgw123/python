
school  = 'oldboy'
names = ["Alex", "Jack", "Rain"]
names_tuple = (1, 2, 3, 4)

def change_name():
    names[0] = "金角大王"
    print("inside func", names)

change_name()
print(names)    #列表，字典是可以更改的。字符、数字不可更改

def change_name(name):
    global school   #将局部变量转变成全局变量(声明变量为全局变量)     不建议这样使用
    school = 'Mage Linux'
    print('before change', name, school)
    name = 'qgw qiu'     #这个函数就是这个变量的作用域
    print('after change',name)

name = 'qgw'
change_name(name)
print(name)
print(school)

#global 不要使用

