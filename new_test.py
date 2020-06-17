# encoding=utf8
# import sys
# for line in sys.stdin:
#     print(''.join(sorted(line.strip())))
#     import smtplib
import socket

# ipaddr = socket.gethostbyname(socket.gethostname())
# print(ipaddr)


# 单例模式和初始化只执行一次
class Music(object):
    isinstance = None

    def __new__(cls, *args, **kwargs):
        if cls.isinstance is None:
            cls.isinstance = super().__new__(cls)
        return cls.isinstance

    is_init = False

    def __init__(self):
        if not Music.is_init:
            print('初始化')
            Music.is_init = True
        return


# print(Music())
# print(Music())


# 装饰器，写法具有闭包的所有特点,以下功能以登录校验为例
def decorator(need_decorated_fun):
    def wrapper(request,*args, **kwargs):
        if 'session_id' in request.keys():
            need_decorated_fun(request,*args, **kwargs)
        else:
            print('session不存在，即将进入登录页面：')
    return wrapper


# 需要被装饰的函数
def my_info(request):
    print('已进入%s的个人中心页面' % request.get('username'))


"""装饰器的调用原理如下,等同于给需要装饰的函数加“@装饰器名”"""
# 1. 调用装饰器(闭包函数)，传入需要被装饰的函数名(对象)，返回装饰器的内部包装函数
wrapper = decorator(my_info)
# 2. 调用装饰器返回的内部包装函数，传入需要被装饰函数所需的参数，返回被装饰后执行结果
wrapper({'session_id': '', 'username': 'liming'})


# 常用的语法糖需要被装饰的函数进行包装，给需要装饰的函数加“@装饰器名”
@decorator
def my_order(request):
    print('已进入%s的个人订单页面' % request.get('username'))


# 直接调用要被装饰函数即可实现
my_order({})
