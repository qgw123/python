name = 'my name is {name} and {year} 23'

print(name.capitalize())    #将首字母大写
print(name.count('q'))         #统计字符出现的次数
print(name.center(50,'-'))      #字符放在中间，两边以‘—‘补充够50个字符
print(name.endswith('wq'))      #判断以什么结尾是否正确
print(name.expandtabs())        #不常用
print(name[name.find('i'):])     #找到i的下标
print(name.format(name='qgw',year=23))
print(name.format_map({'name':'qgw', 'year': 23}))
print('ab23'.isalnum())            #判断是否是阿拉伯数字
print('abA'.isalpha())
print('a1A'.isidentifier())         #判读是不是一个合法的标识符
print('23'.isdigit())               #判断是否是一个整数
print('33A'.isnumeric())            #是否是空格
print('My Name Is  '.istitle())     #是否是首字母大写
print('My Name Is  '.isprintable()) # tty file ,drive file 是否可以打印
print('My Name Is  '.isupper())     #是否全是大写
print('+'.join(['1', '2', '3']))    #列表中拆入+号，变成字符
print(name.ljust(50, '*'))          #在左边加入*
print(name.rjust(50, '-'))          #在右边加入
print('Alex'.lower())               #转换为小写
print('Alex'.upper())               #全转换为大写
print('\nAlex'.lstrip())            #去掉左边空白符
print('Alex\n'.rstrip())            #去掉右边空白符
print('    Alex\n'.strip())         #去掉所有空白符
p = str.maketrans("abcdefli", '123$@456')   #将前面对应后面的
print("alex li".translate(p))       #将字符转换为p中对应的字符
print('alex li'.replace('l', 'L', 1))   #替换  数字为替换哪一个
print('alex lil'.rfind('l'))        #从右边开始读出返回值的下标
print('1+2+3+4'.split('\n'))        #将字符窜以空格（相当于分隔符）转换为列表
print('1+2\n+3+4'.splitlines())     #以换行符（\n）来分
print('Alex Li'.swapcase())         #将大写转换为小写，将小写转换为大写
print('lex li'.title())             #将首字母大写
print('lex li'.zfill(50))           #字符为50位，不够在前面以0补充

print('---')


