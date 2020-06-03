# encoding=utf8
import json

import requests

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



