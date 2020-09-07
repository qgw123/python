__author__ = 'qgw'
import paramiko

private_key = paramiko.RSAKey.from_private_key_file('C:/Users/Administrator/.ssh/id_rsa')

transport = paramiko.Transport('192.168.189.130', 22)
transport.connect(username='root', pkey=private_key)

sftp = paramiko.SFTPClient.from_transport(transport)
#上传文件
sftp.put('123.txt','/root/456.txt')
#下载文件
sftp.get('/root/ss.py','ss.py')

transport.close()