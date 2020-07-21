'''

'''
import  os

def get_fname():
    while True:
        fname = input('请输入需要创建的文件名')
        if not os.path.exists(fname):   ##相当于shell【 -e fname 】
            break
        print('文件名已存在，请再次输入：')

        return fname

def get_content():
    content = []
    print('请输入内容：，输入quit结束')
    while True:
        data = input('> ')
        if data == 'quit':
            break
        content.append(data)

    return content

def wfile(fname,content):
    with open(fname, 'w') as fobj:
        fobj.writelines(content)

if __name__ == '__main__':
    fname = get_fname()     ##获取文件名
    content = get_content()     ##获取文件内容
    content = [ line + '\n' for line in content ]   #将列表中字符串加\n
    wfilt = (fname,content)     ##将文件内容写入文件中
