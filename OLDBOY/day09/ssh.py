__author__ = 'qgw'
import paramiko

# 创建SSH对象
# ssh = paramiko.SSHClient()
# # 允许连接不在know_hosts文件中的主机
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# # 连接服务器
# ssh.connect(hostname='192.168.189.130', port=22, username='root', password='q')
#
# # 执行命令
# stdin, stdout, stderr = ssh.exec_command('ls')
# # 获取命令结果
# result = stdout.read()
# print(result.decode())
#
# # 关闭连接
# ssh.close()
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='192.168.189.130', port=22, username='root' , password='q')
stdin,stdout,stderr = ssh.exec_command('top')
res, err = stdout.read(), stderr.read()
# result = res if res else err
if res:
    result = res
else:
    result = err
print(result.decode())

ssh.close()