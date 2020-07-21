# -*- coding:utf-8 -*-
def search(website):
    result_list = []  # 存放查询的结果
    search_flag = False  # 定义查询结果标志
    with open('haproxy.conf', 'r', encoding='utf-8') as f:
        for line in f: # if 语句顺序进行，当前条件判断完，进入下一判断
            if 'backend {}'.format(website) == line.strip():  # 找到backend www.oldboy.org 开始截取
                search_flag = True
            if line.strip().startswith('backend') and line.strip() != 'backend {}'.format(website):
# 找到下一个 backend www.xxx.com部分结束，截取其中部分
                search_flag = False
            if search_flag:
                result_list.append(line.strip())
        print(result_list)
        f.close()
    if result_list == []:
        print("对不起，您查询的网址不存在！")
    else:
        return result_list

def add(website):
    arg = eval(website)
    backend_title = 'backend {}'.format(arg['backend'])
    record_title = arg['record']
    context_record = "server {0} {0} weight {1} maxconn {2}". \
        format(record_title['server'], record_title['weight'], record_title['maxconn'])
    add_flag = True
    with open('haproxy.conf', 'r+',encoding='utf-8') as f :
        for i in f:
            if i.strip() == backend_title:
                print('\033[1m41地址已经存在\0330m')
        if add_flag:
            f.write('\n{}'.format(backend_title))
            f.write('\n\t\t{}'.format(context_record))
        f.close()

def delete(website):
    delete_flag = False      #设置删除标志位
    with open('haproxy.conf', 'r') as f, \
        open('haproxy.conf_bak','w') as f1:
        for line in f:
            if 'backend {}'.format(website) == line.strip():
                delete_flag = True
                continue
            if line.strip().startswith('backend') and line.strip() != website:
                delete_flag = False
            if not delete_flag:
                f1.write(line)

        if delete_flag == False:
            print("您删除的网址不存在！")

    with open('haproxy.conf','w')as f,\
            open('haproxy.conf_bak' ,'r') as f1:
        for i  in f1:
            f.write(i)


while True:
    prompt = '''（0）查看
（1）新增
（2）删除
（3）按q退出
请做出你的选择（choice(0/1/2)）: '''
    choice = input(prompt).strip()
    print(choice)
    if choice == '0':
        website = input("请输入要查询的网址："
                        "例如：www.oldboy.org\n")
        search(website)
    elif choice == '1':
        website = input("请输入要新增的网址配置："
                        "例如：{'backend': 'www.baidu.com','record': {'server': '100.1.7.8',"
                        "'weight': 20,'maxconn': 3000}}\n")

        add(website)
    elif choice == '2':
         website = input("请输入要删除的网址配置："
                         "例如：www.baidu.com\n")
         delete(website)
    elif choice == 'q':
        break
    else:
        print("请检查您的输入！")