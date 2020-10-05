# encoding=utf8
import re
import time

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
    def __fun(cls, json_s, keywords):
        if isinstance(json_s, dict):
            if keywords in json_s.keys():
                cls.result.append(json_s[keywords])
            else:
                for _, value in json_s.items():
                    cls.__fun(value, keywords)
        if isinstance(json_s, list):
            for li in json_s:
                cls.__fun(li, keywords)

    @classmethod
    def get_value_with_keywords(cls, my_json, keywords):
        cls.__fun(my_json, keywords)
        return cls.result


print([1, 2, 3, 4, 5][:100])
str1 = "Python's features"
str2 = re.match(r'(.*)on(.*?) .*', str1, re.M | re.I)
print(str2.group(1))


def test_time(f):
    def test(*args, **kwargs):
        print("即将测试函数%s运行时间" % f)
        start_time = time.time()
        fun(*args, **kwargs)
        print("程序%s运行了%s秒" % (f, time.time() - start_time))
    return test


def fun(s):
    for i in range(s):
        time.sleep(1)
        print('第%s此循环' % i)


test_time(fun)(5)
