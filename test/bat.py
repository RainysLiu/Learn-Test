import cmd
import os
import subprocess

import pexpect
import sys
# child = pexpect.spawn('python\n')
# print(child.readline().decode('gbk'))
# child.sendline('1*2*3*4*5')
# print(child.readline().decode('gbk'))
# child.sendline('exit()')
# print(child.readline().decode('gbk'))

'''
p = subprocess.check_output('python')

curline = p.stdout.read.decode('gbk')
print(curline)
# p.communicate(b'exit()\n',timeout=3)
# p.wait()

'''


# obj = subprocess.Popen(bytes("python".encode()), stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# out,err = obj.communicate(input=bytes(r'print(1) \n'.encode()))
# print(out)
#
# print(err)


#run.py
'''
from subprocess import *
import threading
import time

p =Popen('cmd.exe',shell=True,stdin=PIPE,stdout=PIPE)


line = p.stdout.readline()
print(">>>>>>",line.decode("GBK"))


p.stdin.write("echo HELLW_WORLD!\n".encode("GBK"))

p.stdin.flush()

line = p.stdout.readline()
print(">>>>>>",line.decode("GBK"))


time.sleep(1) #延迟是因为等待一下线程就绪
p.stdin.write("exit\r\n".encode("GBK"))
p.stdin.flush()
line = p.stdout.readline()
print(">>>>>>",line.decode("GBK"))


'''
#run.py
'''
from subprocess import *
import threading
import time

p =Popen('cmd.exe',shell=True,stdin=PIPE,stdout=PIPE)

def run():
    global p
    while True:
        line = p.stdout.readline()
        if not line:  #空则跳出
            break
        print(">>>>>>",line.decode("GBK"))

    print("look up!!! EXIT ===")   #跳出


w =threading.Thread(target=run)

p.stdin.write("echo HELLW_WORLD!\r\n".encode("GBK"))
p.stdin.flush()
time.sleep(1) #延迟是因为等待一下线程就绪
p.stdin.write("exit\r\n".encode("GBK"))
p.stdin.flush()

w.start()



'''






