__author__ = 'qgw'
#https://www.cnblogs.com/alex3714/articles/5161349.html


import os       #系统命令
os.getcwd()     #获取当前目录
# os.chdir()      #切换目录
# os.makedirs()   #逐级创建目录
# os.removedirs() #逐级删除目录， 若目录为空，则删除，并递归到上一级目录，如若也为空，则删除，依次类推
# os.mkdir()      #创建目录
# os.rmdir()      #删除单级目录，若目录不为空则无法删除，报错。
# os.remove()     #删除一个文件
# os.rename()     #重命名
# os.stat()       #获取文件/目录信息
# os.listdir()    #列出指定目录下的所有文件
# os.sep          #输出操作系统特定的路径分隔符
# os.linesep      #输出当前平台使用的行终止符
# os.pathsep      #输出用于分隔文件路径的字符串
# os.environ      #获取系统环境变量
# os.name         #输出当前平台
# os.system()     #运行shell命令，直接显示
#
# os.path.exists(path)    #判断目录路径是否存在

print(os.getcwd())