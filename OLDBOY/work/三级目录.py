__author__ = 'qgw'

list_city = {
    '广东': {
        '深圳': {
            '龙岗': ['布吉', '横岗', '双龙'],
            '罗湖': ['水贝', '老街', '国贸'],
            '南山': ['百度', '腾讯', '阿里']
        },
        '广州': {
            '白云': ['云台山', '云台花园', '浪花'],
            '天河': ['客运站', '天桥', '广州塔'],
            '番禺': ['长隆','动物园', '水上乐园']
        },
        '惠州': {
            '惠阳': ['大亚湾', '亚公顶', '南站' ],
            '惠城': ['水口', '惠州西湖', '北站'],
            '惠东': ['双月湾', '熙和湾', '海边']

        }
    },
    '上海':{
        '嘉定区': ['真新', '南翔镇', '江桥镇'],
        '金山': ['枫泾镇', '朱泾镇', '亭林镇'],
        '崇明': ['堡镇','庙镇','城桥镇']
    },
    '北京': {
        "昌平":{
            "沙河":["oldboy","test"],
            "天通苑":["链家地产","我爱我家"]
        },
        "朝阳":{
            "望京":["奔驰","陌陌"],
            "国贸":{"CICC","HP"},
            "东直门":{"Advent","飞信"},
        },
    }
}

exit_type = False
while not  exit_type:
    for i in list_city:
        print(i)
    choice = input('选择进入>>>: ')
    if choice in list_city:
        while not  exit_type:
            for i2 in list_city[choice]:
                print('\t', i2)
            choice2 = input('选择进入>>>2:')
            if choice2 in list_city[choice]:
                while  not  exit_type:
                    for i3 in list_city[choice][choice2]:
                        print('\t\t', i3)
                    choice3 = input('选择进入>>>3:')
                    if choice3 in list_city[choice][choice2]:
                        # while not  exit_type:
                        for i4 in list_city[choice][choice2][choice3]:
                            print('\t\t\t',i4)
                        choice4 = input('这是最后一层，按“b”返回上一层，按“q”退出')
                        if choice4 == 'b':
                            pass
                        elif choice4 == 'q':
                            exit_type = True
                    if choice3 == 'b':
                        break
                    elif choice3 == 'q':
                        exit_type = True
            if choice2 == 'b':
                break
            elif choice2 == 'q':
                exit_type = True
    if choice   == 'q':
        exit_type = True