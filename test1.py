import time


t = 5
for i in range(t):
    print('*' * i)
    time.sleep(1)
print('第%s个称许程序执行完成，用时%s秒' % (t / 5, t))
