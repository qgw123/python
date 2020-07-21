from random import randint, choice

def add(x, y):
    return x + y

def sub(x, y):
    return  x - y

def exam():
    cmds = {'+': add, '-': sub}
    nums = [randint(1, 100) for i in range(2)]
    nums.sort(reverse=True) #默认升序，改为降序
    op = choice('+-')
    result = cmds[op](*nums)
    prompt = '%s %s %s = ' % (nums[0], op, nums[1])
    tries = 0

    while tries < 3:
        try:
            answer = int(input(prompt))
        except: #简单粗暴地捕获所有异常
            continue

        if answer == result:
            print('Very Good!')
            break
        else:
            print('Wrong Answer!')
            tries += 1
    else:   #此得是while的else, 全算错才给出答案。算对了就不给出答案
        print('%s%s' % (prompt, result))

# def main():
if __name__ == '__main__':
    while True:
        exam()
        try:
            yn = input('Continue(y/n)? ').strip()[0]
        # if yn in 'nN':
        except IndexError:
            continue
        except (KeyboardInterrupt,EOFError):
            print()
            yn = 'n'
        if yn in 'nN':
            break
#
# if __name__ == '__main__':
#     main()