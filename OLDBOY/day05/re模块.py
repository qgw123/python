__author__ = 'qgw'
#常用正则表达式符号
'''
'.'     默认匹配除\n之外的任意一个字符，若指定flag DOTALL,则匹配任意字符，包括换行
'^'     匹配字符开头，若指定flags MULTILINE,这种也可以匹配上(r"^a","\nabc\neee",flags=re.MULTILINE)
'$'     匹配字符结尾，或e.search("foo$","bfoo\nsdfsf",flags=re.MULTILINE).group()也可以
'*'     匹配*号前的字符0次或多次，re.findall("ab*","cabb3abcbbac")  结果为['abb', 'ab', 'a']
'+'     匹配前一个字符1次或多次，re.findall("ab+","ab+cd+abb+bba") 结果['ab', 'abb']
'?'     匹配前一个字符1次或0次
'{m}'   匹配前一个字符m次
'{n,m}' 匹配前一个字符n到m次，re.findall("ab{1,3}","abb abc abbcbbb") 结果'abb', 'ab', 'abb']
'|'     匹配|左或|右的字符，re.search("abc|ABC","ABCBabcCD").group() 结果'ABC'
'(...)' 分组匹配，re.search("(abc){2}a(123|456)c", "abcabca456c").group() 结果 abcabca456c
 
 
'\A'    只从字符开头匹配，re.search("\Aabc","alexabc") 是匹配不到的
'\Z'    匹配字符结尾，同$
'\d'    匹配数字0-9         #\d+   匹配多个数字
'\D'    匹配非数字
'\w'    匹配[A-Za-z0-9]
'\W'    匹配非[A-Za-z0-9]
's'     匹配空白字符、\t、\n、\r , re.search("\s+","ab\tc1\n3").group() 结果 '\t'
'''

# re.match            #从头开始匹配
# re.search           #匹配包含
# re.findall          #把所有匹配到的字符放到以列表中的元素返回
# re.splitall         #以匹配到的字符当做列表分隔符
# re.sub              #匹配字符并替换

import re
#'(?P<name>...)' 分组匹配
re.search("(?P<province>[0-9]{4})(?P<city>[0-9]{2})(?P<birthday>[0-9]{4})","371481199306143242").groupdict("city")
#    {'province': '3714', 'city': '81', 'birthday': '1993'}

re.search('(?P<province>[0-9]{6})(?P<birthday>[0-9]{8})(?P<houxu>[0-9]{4})','441481199510043339').groupdict('houxu')
#    {'province': '441481', 'houxu': '0433', 'birthday': '199510'}

##替换
re.sub()
re.sub('[0-9]+', '|', 'abc12de34f5g6h')
#    'abc|de|f|g|h'
re.sub('[0-9]+', "|", 'a1b2c3d4e5f6g7' ,count=2)
#    'a|b|c3d4e5f6g7'

#正则表达式里使用"\"作为转义字符
#正则表达式可以使用r"\\"表示。同样，匹配一个数字的"\\d"可以写成r"\d
'''
re.I(re.IGNORECASE): 忽略大小写（括号内是完整写法，下同）
M(MULTILINE): 多行模式，改变'^'和'$'的行为（参见上图）
S(DOTALL): 点任意匹配模式，改变'.'的行为
'''


