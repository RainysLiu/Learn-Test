import time

import paramiko

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(hostname='39.106.2.131', port=22, username='root', password='La1414785769@')

chan=ssh.invoke_shell()#新函数
command = 'python'
chan.send(command+'\n')#\n是执行命令的意思，没有\n不会执行
time.sleep(2)#等待执行，这种方式比较慢
res=chan.recv(1024).decode('utf8')#非必须，接受返回消息
print(res)
if res.find('Type "help", "copyright", "credits" or "license" for more information.') !=1:
    chan.send('1*2**4*5*6*7\n')  # \n是执行命令的意思，没有\n不会执行
    time.sleep(2)  # 等待执行，这种方式比较慢
    chan.send('import django\n')  # \n是执行命令的意思，没有\n不会执行
    time.sleep(2)  # 等待执行，这种方式比较慢
    res = chan.recv(1024).decode('utf8')  # 非必须，接受返回消息
    print(res)
    chan.send('exit()\n')#\n是执行命令的意思，没有\n不会执行
time.sleep(2)#等待执行，这种方式比较慢
res=chan.recv(1024).decode('utf8')#非必须，接受返回消息
print(res)
chan.close()
ssh.close()




