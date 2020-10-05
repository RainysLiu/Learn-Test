# coding=utf8


# 1.时间相关
import time
import datetime

# 1.获取指定格式的当前时间字符串

now_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
print(now_time)

# 2.获取英文格式的当前时间字符串

print(time.strftime('%Y-%B-%d ,%A ,%H:%M:%S',time.localtime(time.time())))

# 英文格式时间转换中文

time1='Friday, July 3, 2020'
time_format=datetime.datetime.strptime(time1,'%A, %B %d, %Y')
print(time_format)

# 2.系统路径相关
import os

# 1.获取当前文件的路径
# 绝对路径
print(os.path.abspath(__file__))
# 相对路径
print(os.path.relpath(__file__))

# 2.当前文件所在目录
print(os.path.dirname(__file__))
print(os.getcwd())

# 3.相对路径转绝对路径

# 相对路径
rep = os.path.realpath(__file__)
# 绝对路径
absp = os.path.abspath(__file__)
print(rep,"\n",absp)

# 4.分割路径和文件名

# 将文件名和路径分割开
print(os.path.split(absp))
# 将路径与文件格式分开
print(os.path.splitext(absp))
# 将盘符与路径分开
print(os.path.splitdrive(absp))

# 5.得到文件的后缀名

print(os.path.splitext(absp)[-1])

# 3.递归的思想

# 递归本质上是循环，常用的场景？
# 1.实现阶乘
def fun(n):
    if n ==0 or n ==1:
        return 1
    else:
        return (n*fun(n-1))
print(fun(10))

# 2.写一个函数，进行文件路径扫描

def getallfiles(file_path):
    # 判断路径是否为目录
    if not os.path.isdir(file_path):
        print(file_path)
    # 列出文件夹中包含的文件或文件夹的名字（列表)
    else:
        dirlist = os.listdir(file_path)
        for dir in dirlist:
            full_name = os.path.join(file_path ,dir)
            if os.path.isdir(full_name):
                getallfiles(full_name)
            else:
                print(full_name)

# getallfiles('E:/Project/')


# 4.随机数的应用

# 生成一个每位随机含大小写字母、数字的指定长度的验证码

import random
import string

# 生成全部字母，包括a-z,A-Z
strs = string.ascii_letters
# 生成数组，包括0-9
nums = string.digits
# 生成字母与数字的组合
totle_string = strs + nums
# totle_string = [str(i) for i in range(10)] + [chr(i) for i in range(ord('a'), ord("z") + 1)] +\
#                [chr(i) for i in range(ord('A'), ord("Z") + 1)]
print(totle_string)
def auth_code(num):
    # random.sample()截取列表的指定长度的随机数
    print(''.join(random.sample(totle_string, num)))

auth_code(10)

# 5.内置函数的高阶用法

from functools import reduce

# 1.列表生成器的使用

list1 = [1,2,3,4,5]
iters = iter(list1)
print(next(iters))
print(next(iters))
# for i in iters:
#     print(i)

# 2.以filter、map和reduce为例，各自的原理？




# 3.filter、map和reduce各自举例

# map() 会根据提供的函数对指定序列做映射
a = [1, 2, 3, 4]
b = map(lambda x :x*2, a)
print(list(b))

# filter() 用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表
# 列出列表中所有奇数
def old_num(n):
    return n % 2 == 1

newlist = filter(old_num, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# print(newlist)
print(list(newlist))

# reduce() 函数会对参数序列中元素进行累积
# def add(a,b):
#     return int(a)*10 + int(b)

add_num = reduce(lambda a, b: int(a)*10 + int(b), [i for i in "12345" ])
print(add_num, type(add_num))

# 6.排序算法
"""
常见的排序：
选择、冒泡、插入，各自代码实现？
"""
array = [9, 8, 3, 6, 5, 4, 7]
# 选择
def choice():
    for i in range(0, len(array) - 1):
        for j in range(i+1, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
# 冒泡
def maopao():
    for i in range(1, len(array)):
        for j in range(0, len(array) - i):
            if array[j] > array[j + 1]:
                array[j + 1], array[j] = array[j], array[j + 1]
    print(array)

def maopao_back():
    for i in range(len(array)):
        for j in range(len(array) - 1, i, -1):
            if array[j - 1] > array[j]:
                array[j - 1], array[j] = array[j], array[j - 1]
    print(array)
maopao_back()


# 7.正则表达式
import re
"""
当正则表达式中包含能接受重复的限定符时，通常的行为是（在使整个表达式能得到匹配的前提下）匹配尽可能多的字符。
以这个表达式为例：a.*b，它将会匹配最长的以a开始，以b结束的字符串。如果用它来搜索aabab的话，它会匹配整个字符串aabab。
这被称为贪婪匹配。
有时，我们更需要懒惰匹配，也就是匹配尽可能少的字符。前面给出的限定符都可以被转化为懒惰匹配模式，只要在它后面加上一个问号?。
这样.*?就意味着匹配任意数量的重复，但是在能使整个匹配成功的前提下使用最少的重复。现在看看懒惰版的例子吧：
a.*?b匹配最短的，以a开始，以b结束的字符串。如果把它应用于aabab的话，它会匹配aab（第一到第三个字符）和ab（第四到第五个字符）
"""

# 1.正则判断一个字符串是否是手机号码，再判断是哪个运营商

import re
def phone(phone_num):
    if re.match(r'1[3|4|5|7|8]\d{9}', phone_num):
        print("您输入的的手机号码为：", phone_num)
        #中国联通号码开头：
        # 130，131，132，155，156，185，186，145，176
        if re.match(r'13[0|1|2]\d{8}', phone_num) or \
            re.match(r"15[5|6]\d{8}", phone_num) or \
            re.match(r"18[5|6]", phone_num) or \
            re.match(r"145\d{8}", phone_num) or \
            re.match(r"176\d{8}", phone_num):
            print("该号码属于：中国联通")
        # 中国移动134, 135 , 136, 137, 138, 139, 147, 150, 151,152,
        # 157, 158, 159, 178, 182, 183, 184, 187, 188
        elif re.match(r"13[4|5|6|7|8|9]\d{8}", phone_num) or \
                re.match(r"147\d{8}|178\d{8}", phone_num) or \
                re.match(r"15[0|1|2|7|8|9]\d{8}", phone_num) or \
                re.match(r"18[2|3|4|7|8]\d{8}", phone_num):
            print("该号码属于：中国移动")
        else:
            # 中国电信 133,153,189
            print("该号码属于：中国电信")
    else:
        print("输入有误，请输入正确的号码")

phone("15802917105")

# 2.写一个正则，匹配指定的电子邮箱(有问题)

def email_addr(addr_num):
    # 任意邮箱账号正确注册规则，数字或字母开头
    if re.match(r'^[0-9a-zA-Z]{0,19}@[0-9a-zA-Z]\.[com, cn, net]{1,3}$',addr_num):
    # if re.match(r'^[0-9a-zA-Z]+(.[0-9a-zA-Z_-]+){0,4}@[0-9a-zA-Z_-]+(.[0-9a-zA-Z_-]+){0,4}$', addr_num):
        print('邮箱账号正确,账号为：%s' %addr_num)
    else:
        print('请输入正确的邮箱账号!')

email_addr("3330987@qq.com")


# 8.面向对象
# 8.1.类属性/类方法与对象属性/对象方法的区别?代码说明:
"""
1.类属性/方法是可以通过类名或cls访问的
2.对象属性/方法是可以通过对象名或self访问的
3.所有的对象共享同一个类属性/方法
"""
# 实例方法（对象方法）
class Person(object):
    def __init__(self, name):
        self.__name = name   # 私有属性

    def get_name(self):
        return self.__name

p = Person("man")
p.get_name()

# 类方法
class Person(object):
    count = 0
    def __init__(self, name):
        self.name = name
        Person.count = Person.count +1

    @classmethod
    def how_many(cls):
        return cls.count

Person.how_many()
p1 = Person('man')
p2 = Person('woman')
print(Person.count)


# 8.2.类中的静态方法、私有属性/方法(访问限制)实现原理？代码说明:
"""
1.静态方法加装饰器@staticmethod，指方法内部不使用类/对象的属性和方法的独立的方法，
  其实和普通函数没啥区别，唯一的区别就是，他定义的位置被放在了类里，做为类或者实例的一个函数。
2.私有属性和方法只要在对应的属性或方法前加__即可实现访问限制,即只能在定义的类内部使用，
  通过类名或者通过类创建的对象名时无法使用的
"""
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # 私有方法
    def __sing(self):
        print("%s" %self.name,"今年""%s"%self.age,"岁，特长唱歌")

    def girl(self):
        self.__sing()

p = Person("红红",8)
p.girl()


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @ staticmethod
    def __sing(name,age):
        print("%s" % name,"今年""%s" % age,"岁，特长唱歌")

    def girl(cls):
        print(cls.__sing)
        print(Person.__sing)

p = Person("红红",8)
p.girl()


# 8.3.类的构造函数和析构函数，分别指什么？代码说明:

"""
1.构造函数是指__init__(self),即创建对象时对对象赋属性的函数，构造一个对象必须的
2.析构函数值程序执行完毕时，或者函数内部对象使用完毕时，自动给调用的一个释放对象的方法__del__(self)
"""

# 8.4.对类的__str__和__repr__重写的作用？区别？代码说明:
"""
1.重写_str__和__repr__后（__repr__只在__str__位被重写时生效），打印对象名时不再是内存地址，
而是重写后的__str__或__repr__函数返回的东西
如果要把一个类的实例变成 str，就需要实现特殊方法__str__()
__repr__和__str__这两个方法都是用于显示的，__str__是面向用户的，而__repr__面向开发者
"""

# 8.5.写出一种实现类的单例模式的原理?代码说明:
"""
重写__new__方法，使其只调用一次基类的__new__（cls）方法实现多次实例化只在第一次创建实例，即可实现单例
"""
class Single(object):
    # 定义一个类属性做判断
    __instance=None
    def __new__(cls):
        if cls.__instance == None:
            #如果__instance为空证明是第一次创建实例
            cls.__instance = object.__new__(cls)
            return cls.__instance
        else:
            #返回上一个对象的引用
            return cls.__instance

# 8.6.创建对象时默认调用哪两个私有方法？哪个是类方法、哪个是对象方法？调用的先后顺序？代码说明:
"""
__new__和__init__，先调用__new__(cls)实现实例的创建，在调用__init__(self)给实例添加实例属性
"""

# 8.7.如何给类/对象动态添加属性和方法，怎么限制属性添加的范围
"""
添加属性:类名/对象名.属性名 = 值
添加方法:from types import MethodType，类名/对象名.方法名 = MethodType（函数名, 对象名/类名）
限制属性：在类里定义__slot__ = 元组， 元组类定义允许外部绑定的属性/方法名.
"""
# 8.8.哪两个装饰器将私有属性分别可直接get和可改变，且可以对属性值改变做参数校验
"""
@property和@属性名.setter两个装饰器修饰的方法（方法名可为属性名),可以将私有属性在外部分别可直接get和可改变（对象名.方法名）
外部可以直接用“对象名.方法名”的方式进行获取和修改
"""
# 8.9多重继承和多层继承:
class Tree:
    def show(self):
        print("一个树")

class ATree(Tree):
    pass
    # def show(self):
    #     print("一个a树")

class BTree(Tree):
    def show(self):
        print("一个b树")

class CTree(Tree):
    def show(self):
        print("一个c树")

class DTree(ATree, BTree, CTree):
    pass
    # def show(self):
    #     print("一个d树")
DTree().show()


# 9.装饰器
"""
装饰器实现原理？常用场景？
代码说明：
"""
# 装饰器实际是闭包函数：
"""
特点:
外部函数内包一个内部函数
外部函数返回内部函数
外部函数形参是一个函数（将要被装饰的函数）
内部函数里定义装饰的逻辑和其中外部函数入参的函数的调用位置
"""


"""
1.写一个数据库工具的类
实现的功能：
执行SQL查询语句并返回查询结果
执行SQL执行语句并返回执行成功与否的结果
执行SQL查询语句并返回把字典封装成对象后的查询结果
"""

"""
2.写一个SSH连接工具的类
实现的功能：
执行linux系统命令并返回执行后的输出结果
下载linux的文件到本地
上传一个本地的文件到linux系统
先下载一个linux上的文件到本地，修改文件的内容，然后在上传上去
"""





