__author__ = 'qgw'
import paramiko

#指定私钥文件
private_key = paramiko.RSAKey.from_private_key_file('C:/Users/Administrator/.ssh/id_rsa')
#创建ssh对象
ssh = paramiko.SSHClient()
# 允许连接不在know_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#连接到ssh服务器
ssh.connect(hostname='192.168.189.130', port=22, username='root', pkey=private_key)
#执行命令
stdin, stdout, stderr = ssh.exec_command('ifconfig')
#获取命令结果
result =  stdout.read()
#打印命令结果
print(result.decode())

#关闭连接
ssh.close()