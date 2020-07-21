__author__ = 'qgw'
#\高级的 文件、文件夹、压缩包 处理模块
#https://www.cnblogs.com/wupeiqi/articles/4963027.html
import shutil
import os
#
# f1 = open('1.txt', 'rb')
# f2 = open('2.txt', 'wb')

# shutil.copyfileobj(f1,f2)       #拷贝文件
# shutil.copyfile('1.txt', '2.txt')       #拷贝文件   第一个为src # 第二个为dst
# shutil.copymode(src , dst)      #仅拷贝权限。内容、组、用户不变
# shutil.copystat(src, dst)       #拷贝状态的信息，包括：mode bits, atime, mtime, flags
# shutil.copy()                   #拷贝文件和权限
# shutil.copy2()                  #拷贝文件和状态信息
#
# shutil.copytree()               #递归拷贝文件    拷贝目录
# shutil.rmtree()                 #递归删除
# shutil.move(src, dst)           #递归的去移动文件

#压缩，打包
# shutil.make_archive(base_name, format, root_dir...)
'''
#创建压缩包并返回文件路径，例如：zip、tar
    base_name： 压缩包的文件名，也可以是压缩包的路径。时只是文件名，则保存至当前目录，否则保存至指定路径，
    如：www                        =>保存至当前路径
    如：/Users/wupeiqi/www =>保存至/Users/wupeiqi/
    format：	压缩包种类，“zip”, “tar”, “bztar”，“gztar”
    root_dir：	要压缩的文件夹路径（默认当前目录）
    owner：	用户，默认当前用户
    group：	组，默认当前组
    logger：	用于记录日志，通常是logging.Logger对象
'''
# shutil.make_archive('os模块', 'zip',  'C:\\Users\Administrator\Desktop\py1\day05')

import shutil
ret = shutil.make_archive("www", 'gztar', root_dir='/Users/Administrator/Desktop/py1/day05')