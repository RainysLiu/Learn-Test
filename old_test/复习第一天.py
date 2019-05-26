
#print(ord('s'))


import random

# 生成 length长度的验证码
def verify_code(length):
    codes = []
    for _ in range(length):
        # 确认从哪个范围生成随机字符
        # 0代表数字范围， 1代表小写字母范围, 2大写字母范围
        rn = random.randint(0, 2)
        # 三元操作符
        rank = ('0', '9') if rn == 0 else ('a', 'z') if rn == 1 else ('A', 'Z')

        codes.append(random_char(*rank))  # 提取元组的内容

    return ''.join(codes)


print(var_char('a','b'))

print(random.randint(1,10))

print(int('ab',16))

s = ()
print(type(s))

print(bool(''))
print(bool(None))



#any与all之用法
print(any(('',1,0)))

print(all(('',1,0)))




#sort与sorted之区别
list_1 = [('b',1),('c',7),('a',3)]

list_1.sort()

print(list_1)

list_2 = sorted(list_1,key=lambda tup:tup[1],reverse = True)

print(list_1)

print(list_2)



#字典操作

p = {'id':23,'name':'liu','age':20,'address':'xian'}

print({value:key for key,value in p.items()})

#del p['id']

#p.pop('age')

p.setdefault('address','beijing')

p.update({'age':23,'address':'nanjing','nation':'han'})
print(p)





#使用pymysql连接数据库



import pymysql


def connect(**kwargs):
    global db  # 提升为全局变量
    db = pymysql.Connect(**kwargs)
    print('连接数据库成功!')


def save(id, name, age):
    pass


def create_table(table_name, *args):
    cursor = db.cursor()  # 打开数据库的游标
    columns = ('%s,' * len(args))[:-1]
    args = (table_name, *args)
    sql = "create table %s(" + columns + ")"
    cursor.execute(sql % args)
    print('%s 创建成功' % table_name)


def query(**kwargs):
    # 可以依据： id, name
    pass


db_config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': 'root',
    'db': 'xa_py3',
    'charset': 'utf8'
}
connect(**db_config)  # 提取字典的数据，转成key=value
create_table('t_qx', 'id int', 'title varchar(20)')







#函数之对象
def fx(a):
    fx.a +=a   #fx.a为函数fx的对象
    print(fx.a)

fx.a = 200
fx(100)
fx(200)



#函数之装饰器

import time
def decorate(mysum):
    def wapper(*args,**kwargs):
        stime = time.time()
        mysum(*args,**kwargs)
        endtime = time.time()
        print(endtime-stime)
    return wapper


@decorate
def mysum(fun,*args):
    if fun=='add':
        print(sum(args))
    else:
        re = 1
        for s in args:
            re *= s
        print(re)

mysum('add',1,22,36634,466,533)
mysum('乘',1,22,36634,466,533)



#权限相关
# 有参数的装饰函数
rights = {'QX_ADD': 1,
          'QX_EDIT': 2,
          'QX_DEL': 4}

user_qx = 6  # 当前用户的权限

def check_qx(qx_name):
    print('--A--')

    def wrapper1(fun):
        print('--B--')

        def wrapper2(*args, **kwargs):
            print('---C--')
            # 判断当前用户的权限是否具有qx_name
            qx_right = rights.get(qx_name)
            if all((qx_right, user_qx & qx_right == qx_right)):
                # 有权限
                result = fun(*args, **kwargs)
                return result
            else:
                print('－－无此权限－－')

        return wrapper2

    return wrapper1

@check_qx('QX_ADD')  # 检查当前用户是否拥有add权限
def add(id, title):
    connect(**db_config)
    cursor = db.cursor()
    cursor.execute('insert t_qx(id,title) values(%s,%s)',
                   (id, title))
    db.commit()  # 提交
    print('增加 t_qx 成功!')

add(2, '修改')



#python上下文 context



