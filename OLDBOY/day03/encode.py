#
''''''
'''
ascii
gb2312
gbk
unicode
utf-8   
转换编码都需要通过Unicode这个编码，最后会变成一个字节模式 

'''
import sys
print(sys.getdefaultencoding()) #查看默认编码

s = '你好'
# s_to_unicode = s.decode('utf-8')
s_to_gbk = s.encode('gbk')
print(s)
print(s_to_gbk)
print(s.encode('utf-8'))
print(s.encode("utf-8").decode("utf-8").encode("gb2312").decode('gb2312'))
