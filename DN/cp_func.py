import sys

def cp(src_name,drt_name):
    srcf = open(src_name, 'rb')
    detf = open(drt_name, 'wb')
    while True:
        data = srcf.read(4096)
        if not data :
            break
        else:
            detf.write(data)

    srcf.close()
    detf.close()

cp(sys.argv[1],sys.argv[2])

# python cp_func.py /bin/touch  /tmp/touch