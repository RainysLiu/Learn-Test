# encoding=utf8
import json
import os
import time

import requests
"""
json_str = {
    'mm': {
        'hh': 'ff'

    },
    'ss': [1, 2, 3, {'ll': 'dd'}]
}


class GetValue:
    # 将查询结果以列表展示(可能多个)
    result = []
    @classmethod
    def __fun(self, json_str, keywords):
        if isinstance(json_str, dict):
            if keywords in json_str.keys():
                 self.result.append(json_str[keywords])
            else:
                 for _, value in json_str.items():
                    self.__fun(value, keywords)
        if isinstance(json_str, list):
            for li in json_str:
                self.__fun(li, keywords)

    @classmethod
    def get_value_with_keywords(self, json_str, keywords):
        self.__fun(json_str, keywords)
        return self.result


print([1,2,3,4,5][:100])
import re
str1 = "Python's features"
str2 = re.match( r'(.*)on(.*?) .*', str1, re.M|re.I)
print(str2.group(1))



"""

"""
def test_time(fun):
    def test(*args, **kwargs):
        print("即将测试函数%s运行时间" % fun)
        start_time = time.time()
        fun(*args, **kwargs)
        print("程序%s运行了%s秒" % (fun, time.time() - start_time))
    return test


def fun(s):
    for i in range(s):
        time.sleep(1)
        print('第%s此循环' % i)


test_time(fun)(5)
"""
# path = os.path.dirname(__file__) + '/test.py'
path = os.path.join(os.path.dirname(__file__), 'test.py')
print(os.path.abspath(path))
print(os.path.exists(path))


