import random
all = ['石头','剪刀','布']
win_list = [['石头','剪刀'], ['剪刀','布'],['布','石头']]
promot = ''' (0) 石头
(1) 剪刀
(2）布
请做出你的选择0/1/2 '''
pwin = 0
cwin = 0

while pwin < 2 and cwin < 2:
    complete = random.choice(all)
    ind = int(input(promot)) #将用户输入的数字转换成列表的下标
    player = all[ind]        # 从列表中取出字符串
# player = ('请输入石头/剪刀/布' : )
    print('你出了：%s 电脑出了： %s'  % (player,complete))

    if player == complete:
        print('\033[32;1m平局\033[0m')
    elif [player,complete] in win_list:
        pwin += 1
        print('\033[31;1m你赢了\033[0m')
    else:
        cwin += 1
        print('\033[30;1m你输了\033[0m')


# if  complete == '石头':
#     if player == '石头':
#         print('平局')
#     elif player == '剪刀':
#         print('你输了')
#     else:
#         print('你赢了')
# elif complete == '剪刀':
#      if player == '石头':
#          print('你赢了')
#      elif player == '剪刀':
#          print('平局')
#      else:
#          print('你输了')
# else:
#      if player == '石头':
#          print('你输了')
#      elif player =='剪刀':
#          print('你赢了')
#      else:
#          print('平局')

