# coding = utf-8

from myunittest import MyTestCase
from get_excel_data import get_all_text_input
from cart import Cart


ALL_INPUT = get_all_text_input()


class TestCart(MyTestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_cart_pay_value(self):
        """
        测试最终支付金额
        :return:
        """
        self.assertEqual(Cart(self.param[0]).pay_value(), self.param[1])

