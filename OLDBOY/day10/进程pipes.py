__author__ = 'qgw'
from multiprocessing import Pipe,Process

def run(conn):
    conn.send([42, None, 'hello'])
    conn.send([40, None, "qgw"])
    print('from parent :',conn.recv())
    conn.close()

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p = Process(target=run,args=(child_conn,))
    p.start()
    print(parent_conn.recv())
    print(parent_conn.recv())
    parent_conn.send("Are you ok")
    p.join()