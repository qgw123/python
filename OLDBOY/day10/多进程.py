__author__ = 'qgw'
import multiprocessing,threading
import time

def run():
    print(threading.get_ident())

def f(name):
    time.sleep(2)
    print('hello' , name )
    t = threading.Thread(target=run)
    t.start()
    t.join()

if __name__ == '__main__':
    for i in range(5):
        m = multiprocessing.Process(target=f,args=('bob %s' % i ,))
        m.start()
        m.join()

