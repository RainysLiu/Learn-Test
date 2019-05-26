
def outer(func):
    def inner(*args, **kwargs):
        #添加修改的功能
        print("&&&&&&&&&&&&&")
        return func(*args, **kwargs)
    return inner



@outer #say = outer(say)
def say(name, age): #函数的参数力理论上是无限制的，但实际上最好不要超过6、7个
    print("my name is %s, I am %d years old" % (name, age))
    return "aaaa"


say("tom", 18)






####另一个装饰器

import time

def decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func()
        time.sleep(0.8)
        end_time = time.time()
        print(end_time - start_time)

    return wrapper

@decorator 
def func():
    print('这是内部函数')
    

func() # 函数调用
