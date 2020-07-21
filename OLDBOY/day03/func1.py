import time

def log():
    time_format= '%Y-%m-%d %X'
    time_current = time.strftime(time_format)
    with open('a.txt', 'a+') as f :
        f.write('%s end action\n' %time_current)

def test1() :
    print('In the test1')
    log()

def test2() :
    print('In the test2')
    log()

def test3() :
    print('In the test3')
    log()

test1()
test2()
test3()
