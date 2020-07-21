info = {
    '广东': {
        '深圳': {
            '龙岗区': ['双龙','布吉'],
            '罗湖区': ['老街','水贝']
        },
        '广州': {
            '天河区': ['客运站','购物公园'],
            '番禺区': ['长隆', '野生动物园'],
        },
    },
    '上海': {
        '天气': {
            '晴天': ['游玩','逛街'],
            '雨天': ['电影','火锅']
        },
        '地区': {
            '明珠': ['',''],
            '': ['',''],
        }
    },
    '北京':{
        "昌平":{
            "沙河":["oldboy","test"],
            "天通苑":["链家地产","我爱我家"]
        },
        "朝阳":{
            "望京":["奔驰","陌陌"],
            "国贸":{"CICC","HP"},
            "东直门":{"Advent","飞信"},
        },
        "海淀":{},
    },
}

exit_flag = False

while not  exit_flag:
    for i in info:
        print(i)
    choice = input('选择进入>>>: ')
    if choice in info:
        while not exit_flag:
            for i2 in info[choice]:
                print('\t',i2)
            choice2 = input('选择进入>>>2:')
            if choice2 in info[choice]:
                while not exit_flag:
                    for i3 in info[choice][choice2]:
                        print('\t\t',i3)
                    choice3 = input('选择进入>>>3: ')
                    if choice3 in info[choice][choice2]:
                        for i4 in info[choice][choice2][choice3]:
                            print('\t\t\t',i4)
                        choice4 = input("最后一层，按b返回 按q退出>>:")
                        if choice4 == 'b':
                            pass
                        elif choice4 == 'q':
                            exit_flag = True
                    if choice3 == 'b':
                        break
                    elif choice3 == 'q':
                        exit_flag = True
            if choice2 == 'b':
                break
            elif choice2 == 'q':
                exit_flag = True
    # if choice == 'b':
    #     break
    # elif choice == 'q':
    #     exit_flag == True
    # if choice == 'b':
    #     break