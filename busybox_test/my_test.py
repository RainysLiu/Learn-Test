import pytesseract
import requests
import os
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from PIL import Image, ImageEnhance


class FileDownloadAndUpload(object):
    """
    特殊场景下，文件下载/上传类
    """
    def __init__(self, server_ip, server_port, authorization, server_file_name, is_visible,paste_bin_account,
                 paste_bin_pwd, paste_code_format, paste_code_expire, paste_code_private, paste_code_name):
        """
        初始化
        :param server_ip: busybox搭建的服务器ip
        :param server_port: busybox的端口
        :param authorization: busybox的用户认证加密串(需要提前手动测试获取)
        :param server_file_name: 要从busybox下载的文件名
        :param is_visible: 是否需要浏览器界面可见
        :param paste_bin_account: pastebin.com的账户
        :param paste_bin_pwd: pastebin.com的密码
        :param paste_code_format: 要上传至pastebin.com的文件标识格式
        :param paste_code_expire: 要上传文件在pastebin.com的有效期
        :param paste_code_private: 要上传文件在pastebin.com的公开状态
        :param paste_code_name: 要上传至pastebin.com的文件格式名
        """
        # 定义从busybox下载所需相关的参数
        self.authorization = authorization
        self.server_file_name = server_file_name
        self.server_ip = server_ip
        self.server_port = server_port
        # 定义上传pastebin网站所需的参数
        self.paste_bin_account = paste_bin_account
        self.paste_bin_pwd = paste_bin_pwd
        self.paste_code_format = paste_code_format
        self.paste_code_expire = paste_code_expire
        self.paste_code_private = paste_code_private
        self.paste_code_name = paste_code_name
        self.is_visible = is_visible
        # 初始化仿真浏览器对象
        self.driver_path = 'chrome_driver.exe'
        self.browser = webdriver.Chrome(executable_path=self.driver_path,
                                        chrome_options=self.chrome_options(is_visible))

    def chrome_options(self, is_visible):
        """
        chrome的可选设置
        :param is_visible: 是否需要浏览器界面可见
        :return:
        """
        if not is_visible:
            chrome_options = Options()
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--disable-gpu')
        else:
            chrome_options = None
        return chrome_options

    def down_load(self):
        """
        下载文件
        :return:
        """
        header = {
            'Authorization': self.authorization,
        }
        host = self.server_ip + ':' + self.server_port
        url = 'http://' + host + '/' + self.server_file_name
        print('正在从busybox服务器[host:%s]下载文件%s...' % (host, self.server_file_name))
        response = requests.get(url=url, headers=header)
        content = response.content.decode('utf-8')
        # print(content)
        with open('msg.txt', 'w') as f:
            f.write(content)
        cur_path = os.path.dirname(__file__)
        print('下载文件%s至目录:%s成功!' % (self.server_file_name, cur_path))

    def login_paste_bin(self):
        """
        登录pastebin
        :return:
        """
        print('正在登录pastebin.com...')
        self.browser.get('https://pastebin.com/login')
        # time.sleep(10)
        # 获取验证码并登录
        verify_ok = self.login_with_code(mode='auto')
        if not verify_ok:
            for i in range(5):
                print('即将第%s次重新自动识别验证码...' % (i + 1))
                # 非重新加载验证码的情况下，才需要输入账户密码
                if verify_ok != 'reload code':
                    account_input = self.browser.find_element_by_xpath('//*[@name="user_name"]')
                    account_input.send_keys(self.paste_bin_account)
                    pwd_input = self.browser.find_element_by_xpath('//*[@name="user_password"]')
                    pwd_input.send_keys(self.paste_bin_pwd)
                verify_ok = self.login_with_code(mode='auto')
                if verify_ok:
                    print('用户[%s]登录pastebin.com成功！' % self.paste_bin_account)
                    break
            else:
                for i in range(5):
                    print('正在第%s次重新手动输入验证码...' % (i + 1))
                    code_ok = self.login_with_code(mode='manual')
                    if code_ok:
                        print('用户[%s]登录pastebin.com成功！' % self.paste_bin_account)
                        break
                else:
                    exit('验证码输入不正确次数太多,程序失败结束！')

    def manual_verify_code(self):
        self.save_picture()
        img = Image.open('captcha.png')
        img.show()
        code = input('请手动输入验证码:')
        return code

    def save_picture(self):
        self.browser.save_screenshot('captcha.png')
        element = self.browser.find_element_by_xpath('//img[@id="captcha"]')  # 找到验证码图片
        # print('验证码位置:' + element.location)  # 打印元素坐标
        # print('验证码大小:' + element.size)  # 打印元素大小
        if self.is_visible:
            left = element.location['x'] + 65
            top = element.location['y'] + 105
            right = left + element.size['width'] + 30
            bottom = top + element.size['height'] + 15
        else:
            left = element.location['x']
            top = element.location['y']
            right = left + element.size['width']
            bottom = top + element.size['height']
        im = Image.open('captcha.png')
        im = im.crop((left, top, right, bottom))
        im.save('captcha.png')
        im = Image.open('captcha.png')
        im = ImageEnhance.Color(im).enhance(3)
        im = ImageEnhance.Contrast(im).enhance(3)
        im.save('captcha.png')

    def login_with_code(self, mode):
        if mode == 'auto':
            code = self.get_verify_code()
        else:
            code = self.manual_verify_code()
        if code.strip() == '':
            print('验证码为空，登录失败!')
            if self.is_visible:
                self.browser.find_element_by_id('reload').click()
                return 'get code is empty'
            else:
                self.browser.get('https://pastebin.com/login')
                return False
        code_input = self.browser.find_element_by_xpath('//*[@name="captcha_solution"]')
        code_input.send_keys(code)
        submit = self.browser.find_element_by_xpath('//*[@name="submit"]')
        submit.click()
        find_txt = self.browser.find_element_by_id('content_frame').text
        if 'The captcha test failed!' in find_txt:
            print('验证码验证失败!')
            return False
        return True

    def get_verify_code(self):
        """
        获取验证码
        :return:
        """
        print('正在自动识别验证码...')
        self.save_picture()
        code = self.get_code('captcha.png')
        print('自动识别验证码结果为:' + code)
        return code

    def get_code(self, image_path):
        """
        识别验证码
        :return:
        """
        img = Image.open(image_path)
        # 转化为灰度图片
        img = img.convert('L')
        # 二值化处理
        threshold = 140
        table = []
        for i in range(256):
            if i < threshold:
                table.append(0)
            else:
                table.append(1)
        img.point(table, '1')

        img = img.convert('RGB')

        return pytesseract.image_to_string(img)

    def upload(self):
        """
        上传文件
        :return:
        """
        print('正在进入上传文件页面...')
        new_paste_button = self.browser.find_element_by_id('header_new_paste')
        new_paste_button.click()
        print('进入上传文件页面成功!')
        print('正在填写文件内容...')
        paste_code_input = self.browser.find_element_by_id('paste_code')
        with open(self.server_file_name, 'r') as f:
            paste_code = f.read()
        paste_code_input.send_keys(paste_code)
        time.sleep(1)
        # paste_format_span = self.browser.find_elements_by_class_name("select2-selection__rendered")[0].click()
        # self.browser.find_element_by_name('C#').click()
        print('正在设置文件属性信息...')
        Select(self.browser.find_element_by_name("paste_format")).select_by_visible_text(self.paste_code_format)
        Select(self.browser.find_element_by_name("paste_expire_date")).select_by_visible_text(self.paste_code_expire)
        Select(self.browser.find_element_by_name("paste_private")).select_by_visible_text(self.paste_code_private)
        paste_name_input = self.browser.find_element_by_name('paste_name')
        paste_name_input.send_keys(self.paste_code_name)
        self.browser.find_element_by_name('submit').click()
        print('文件上传至pastebin.com成功！')
        if self.is_visible:
            print('浏览器即将关闭!')
        self.browser.quit()

    def run(self):
        """
        主方法
        :return:
        """
        try:
            #从busybox下载文件
            self.down_load()
            # 登录pastebin.com
            self.login_paste_bin()
            # 上传代码文件至pastebin.com
            self.upload()
        except Exception as e:
            print('程序发生异常:%s' % e)


if __name__ == '__main__':
    file_handler = FileDownloadAndUpload(server_ip='39.106.2.131', server_port='8080',
                                         authorization='Basic bGl1OjEyMzQ1Ng==', server_file_name='msg.txt',
                                         is_visible=False, paste_bin_account='liu123', paste_bin_pwd='123456',
                                         paste_code_format='Python', paste_code_expire='1 Year',
                                         paste_code_private='Public', paste_code_name='msg.txt'
                                         )
    file_handler.run()
