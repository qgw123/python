from random import randint, choice

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def exam():
    cmds = {'+': add, '-': sub}
    nums = [randint(1, 100) for i in range(2)]
    nums.sort(reverse=True)  # 列表降序排列
    op = choice('+-')
    result = cmds[op](*nums)
    prompt = '%s %s %s = ' % (nums[0], op, nums[1])
    tries = 0

    while tries < 3:
        try:
            answer = int(input(prompt))
        except:  # 简单粗暴地捕获所有异常
            continue

        if answer == result:
            print('Very good!')
            break
        else:
            print('Wrong answer.')
            tries += 1
    else:  # 此得是while的else，全算错才给答案，算对了就不用给出答案了
        print('%s%s' % (prompt, result))

if __name__ == '__main__':
    while True:
        exam()
        try:
            yn = input("Continue(y/n)? ").strip()[0]
        except IndexError:
            continue
        except (KeyboardInterrupt, EOFError):
            print()
            yn = 'n'

        if yn in 'nN':
            break