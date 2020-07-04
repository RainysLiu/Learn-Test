
# import random
# print(random.randint(1,10))


# import random
# import string
#
# # 生成全部字母，包括a-z,A-Z
# strs = string.ascii_letters
# # 生成数组，包括0-9
# nums = string.digits
# # 生成字母与数字的组合
# totle_string = strs + nums
#
# def auth_code(num):
#     # random.sample()截取列表的指定长度的随机数
#     print(''.join(random.sample(totle_string, num)))
#
# auth_code(10)

# import os
#
# def getallfiles(file_path):
#     # 判断路径是否为目录
#     if not os.path.isdir(file_path):
#         print(file_path)
#     # 列出文件夹中包含的文件或文件夹的名字（列表）
#     dirlist = os.listdir(file_path)
#     for dir in dirlist:
#         full_name = os.path.join(file_path ,dir)
#         if os.path.isdir(full_name):
#             getallfiles(full_name)
#         else:
#             print(full_name)
#
# getallfiles('E:/Project/')


# def old_num(n):
#     return n % 2 == 1
#
# newlist = filter(old_num, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# print(newlist)
# print(list(newlist))

import os
# dir_count = 0
# file_conut = 0
#
#
# def getallfiles(file_path):
#     # 判断路径是否为目录
#     global dir_count, file_conut
#     # if not os.path.isdir(file_path):
#     #     print(file_path)
#     #     file_conut += 1
#     # # 列出文件夹中包含的文件或文件夹的名字（列表)
#     # else:
#     dirlist = os.listdir(file_path)
#     for dir in dirlist:
#         full_name = os.path.join(file_path, dir)
#         if os.path.isdir(full_name):
#             getallfiles(full_name)
#             dir_count += 1
#         else:
#             print(full_name)
#             file_conut += 1
#
# # getallfiles("E:\Project\Learn-Test")
# # print(dir_count, file_conut)
# # print(os.listdir("E:\Project\Learn-Test\.git\hooks\applypatch-msg.sample"))
#
# array = [9, 8, 3, 6, 5, 4, 7]
# def choice():
#     for i in range(0, len(array) - 1):
#         print(array)
#         for j in range(i+1, len(array)):
#             if array[i] > array[j]:
#                 array[i], array[j] = array[j], array[i]
#     print(array)
# choice()
#
# print("*" * 50)
# array = [9, 8, 3, 6, 5, 4, 7]
# def maopao():
#     for i in range(1, len(array)):
#         print(array)
#         for j in range(0, len(array) - i):
#             if array[j] > array[j + 1]:
#                 array[j + 1], array[j] = array[j], array[j + 1]
#     print(array)
# maopao()
# print("*" * 50)
# array = [9, 8, 3, 6, 5, 4, 7]
# # print(array)
# def maopao_back():
#     for i in range(len(array)):
#         print(array)
#         for j in range(len(array) - 1, i, -1):
#             if array[j - 1] > array[j]:
#                 array[j - 1], array[j] = array[j], array[j - 1]
#     print(array)
# maopao_back()
#
# print(list('sdfdf'))
# print(str([1, 2, 3, 5, 7]))
# strsss = "[1, 2, 3, 5, 7]"
# print(eval(strsss))
# print(list(strsss))


import re
def email_addr(addr_num):
    # 任意邮箱账号正确注册规则，数字或字母开头
    if re.match(r'^[\da-zA-Z][\da-zA-Z_.-]+[\da-zA-Z]@[\da-zA-Z_-]+(.[\da-zA-Z_-]+){0,4}$', addr_num):
        print('邮箱账号正确,账号为：%s' % addr_num)
    else:
        print('请输入正确的邮箱账号!')

email_addr("3330987@qq.com")

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


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __sing(self):
        print("%s"%self.name,"今年""%s"%self.age,"岁，特长唱歌")

    def gg(self):
        self.__sing()

p = Person("红红",8)
p.gg()

