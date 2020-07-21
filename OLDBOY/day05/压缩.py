__author__ = 'qgw'
import shutil
import zipfile
import tarfile
'''
shutil.make_archive(base_name, format,root_dir...)

创建压缩包并返回文件路径，例如：zip、tar

    base_name： 压缩包的文件名，也可以是压缩包的路径。只是文件名时，则保存至当前目录，否则保存至指定路径，
    如：www                        =>保存至当前路径
    如：/Users/wupeiqi/www =>保存至/Users/wupeiqi/
    format：	压缩包种类，“zip”, “tar”, “bztar”，“gztar”
    root_dir：	要压缩的文件夹路径（默认当前目录）
    owner：	用户，默认当前用户
    group：	组，默认当前组
    logger：	用于记录日志，通常是logging.Logger对象
'''
shutil.make_archive('os模块', 'zip',  'C:\\Users\Administrator\Desktop\py1\day05') #压缩目录

#shutil 对压缩包的处理是调用 ZipFile 和 TarFile 两个模块来进行的

import zipfile

# 压缩
z = zipfile.ZipFile('laxi.zip', 'w')
z.write('a.log')
z.write('data.data')
z.close()

# 解压
z = zipfile.ZipFile('laxi.zip', 'r')
z.extractall()
z.close()

import tarfile

# 压缩
tar = tarfile.open('your.tar','w')
tar.add('/Users/wupeiqi/PycharmProjects/bbs2.zip', arcname='bbs2.zip')
tar.add('/Users/wupeiqi/PycharmProjects/cmdb.zip', arcname='cmdb.zip')
tar.close()

# 解压
tar = tarfile.open('your.tar','r')
tar.extractall()  # 可设置解压地址
tar.close()
