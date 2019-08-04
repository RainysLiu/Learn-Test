from selenium import webdriver
import time,unittest
from selenium.common.exceptions import NoAlertPresentException


class Test_prompt():
    def test_HandleAlert(self):
        url = r'http://39.106.2.131:8080/msg.txt'
        self.driver = webdriver.Chrome(executable_path='chrome_driver.exe')
        self.driver.get(url)
        button = self.driver.find_element_by_id('button')
        button.click()
        try:
            # 使用driver.switch_to.alert()方法获取alert对象
            alert = self.driver.switch_to.alert()
            time.sleep(2)
            print(alert.text)
            # 往框里输入值
            alert.send_keys('我要搞自动化。。。')  # 没输入但是也没报错
            time.sleep(4)
            alert.accept()  # 模拟点击确定按钮
        except NoAlertPresentException as e:
            print(e)


test1 = Test_prompt()
test1.test_HandleAlert()