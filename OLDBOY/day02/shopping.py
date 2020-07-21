
salary = input('请输入你的工资： ')

product_list = [('iphone', 5800),
             ('Mac Pro',9800),
             ('Bike',800),
             ('Watch', 10600),
             ('Coffee', 31),
             ('Alex Python', 120)
             ]

shop_list = []
if salary.isdigit():
    salary = int(salary)
    while True:     #enumerate取出下标
        for index, item in enumerate(product_list):
            # print(product_list.index(item), item)
            print(index ,item)
        user_choice = input('请选择需要买的商品>>>：')

        if user_choice.isdigit():
            user_choice = int(user_choice)

            if user_choice < len(product_list) and user_choice >= 0:
                p_item = product_list[user_choice]

                if p_item[1] <= salary: #买的起
                    shop_list.append(p_item)
                    salary -= p_item[1]
                    print('Added %s into shop cart ,your current balance is \033[31;1m%s\033[0m' % (p_item, salary))
                else:
                    print('\033[41;1m你的余额只剩[%s]啦，还买个毛线\033[0m' % salary)
            else:
                print("product code  [%s] is not exist!" % user_choice)

        elif user_choice == 'q':
            print("--------shopping list------")
            for p in shop_list:
                print(p)
            print("Your current balance:",salary)
            exit()
    else:
        print("invalid option")



