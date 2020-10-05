import unittest
from test_cart import TestCart
from get_excel_data import get_all_text_input
from HTMLTestRunner import HTMLTestRunner
from myunittest import MyTestCase

ALL_INPUT = get_all_text_input()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    tests = list()
    for para in ALL_INPUT:
        tests.append(MyTestCase.parametrize(TestCart, param=para))
    suite.addTests(tests)
    # 生成测试报告
    with open('测试报告.html', 'w', encoding='utf8') as f:
        runner = HTMLTestRunner(stream=f,
                                title='测试报告',
                                description='测试用例的执行情况',
                                verbosity=2
                                )
        runner.run(suite)
