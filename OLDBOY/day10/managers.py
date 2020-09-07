__author__ = 'qgw'
from multiprocessing import Process,Manager
import  os

def run(d, l):
    d[os.getpid()] = os.getpid()
    # d[1] = '1'
    # d['2'] = 2

    l.append(os.getpid())
    print(l)

if __name__ == '__main__':
    with Manager() as managers:
        d = managers.dict()
        l = managers.list(range(5))
        p_list = []
        for i in range(10):
            p = Process(target=run, args=(d, l,))
            p.start()
            p_list.append(p)

        for res in p_list:
            res.join()

        print(d)
        print(l)
