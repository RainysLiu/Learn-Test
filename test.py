import configparser
import os
import time


cur_path = os.path.dirname(__file__)
file_list=os.listdir(cur_path)

def getConfig(set_section=None, set_option=None):
    for file_name in file_list:
        if 'ini' in file_name:
            # print(file_name)
            path = os.path.join(cur_path, file_name)
            # print(path)
            config = configparser.ConfigParser()
            config.read(path, encoding="utf-8")
            sections = config.sections()
            for section in sections:
                if section == set_section:
                    options = config.options(section)
                    for option in options:
                        if option == set_option:
                            value = config.get(section, option)
                            print(file_name, section, option, value)


if __name__ == '__main__':
    getConfig('s1', 's')
    time.sleep(5)
    print('第一个执行完成!')