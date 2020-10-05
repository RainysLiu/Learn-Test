import sys
import threading
import os
import time

DIR = r'E:\Project\XinJuKe_download_from_linux\XinJuKe\extapps\xadmin'
FILE_LIST = [os.path.join(DIR, name) for name in os.listdir(DIR) if '.py' in name]
iter_path = sys.executable


def exe_py(py_path):
    sem = threading.Semaphore(3)  # 设置可同时执行的最大线程数
    sem.acquire()
    file_name = os.path.split(py_path)[1]
    with open(py_path, 'r', encoding='utf8') as f:
        data = f.read()
    w_path = os.path.join('.', 'test', file_name)
    with open(w_path, 'w', encoding='utf8') as w_file:
        w_file.write(data)
        print('写文件到%s成功' % w_path)
    time.sleep(2)
    sem.release()


num = 100000
lock = threading.Lock()  # 申请一把锁


def cul(n):
    global num
    lock.acquire()
    for i in range(n):
        num += 1
    for i in range(n):
        num -= 1
    lock.release()
    # dfggdg

    print(num)


def multi_work():
    all_threading = []
    for i in range(10000):
        t = threading.Thread(target=cul, args=(10000, ))
        all_threading.append(t)
    for t in all_threading:
        t.start()

    for t in all_threading:
        t.join()


if __name__ == '__main__':
    multi_work()
