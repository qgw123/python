__author__ = 'qgw'

import paramiko
#指定地址和端口
transport = paramiko.Transport(('192.168.189.130', 22))
#连接的用户和密码
transport.connect(username='root', password='q')

sftp = paramiko.SFTPClient.from_transport(transport)
# 将location.py 上传至服务器 /tmp/test.py
sftp.put('ssh.py', '/root/ss.py')
# 将remove_path 下载到本地 local_path
sftp.get('/root/.ssh/id_rsa', 'C:/Users/Administrator/Desktop/py1/day09/id_rsa130.txt')

transport.close()