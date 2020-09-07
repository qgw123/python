__author__ = 'qgw'
import socket
import hashlib

client = socket.socket()
client.connect(('localhost',21))

while True:
    cmd = input('>>: ').strip()
    if len(cmd) ==0:
        continue
    if cmd.startswith("get"):
        client.send(cmd.encode())
        server_response = client.recv(1024)
        print('server response: ' ,server_response.decode())
        client.send(b'ready to recv file ')
        file_total_size = int(server_response.decode())
        recevied_size = 0
        filename = cmd.split()[1]
        f = open(filename + '.new' , 'wb')
        m = hashlib.md5()

        while recevied_size < file_total_size:
            if file_total_size - recevied_size >= 1024: #要收不止一次
               size = 1024
            else:   #最后一次了，剩下多少收多少
                size = file_total_size - recevied_size
                print('last receive: ',size)

            data = client.recv(size)
            recevied_size += len(data)
            m.update(data)
            f.write(data)

        else:
            new_file_md5 = m.hexdigest()
            print('file recv done ', recevied_size,file_total_size)
            f.close()
            server_file_md5 = client.recv(1024)
            print('server file md5: ',server_file_md5)
            print('client file md5: ',new_file_md5)

client.close()