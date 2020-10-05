# coding=utf8
"""
实现简单的购物车结算功能
"""
import re
import time


class Cart:
    """
    购物车类
    """
    __goods_type_dic = {
        '电子': ['ipad', 'iphone', '显示器', '笔记本电脑', '键盘'],
        '食品': ['面包', '饼干', '蛋糕', '牛肉', '鱼', '蔬菜'],
        '日用品': ['餐巾纸', '收纳箱', '咖啡杯', '雨伞'],
        '酒类': ['啤酒', '白酒', '伏特加']
    }

    def __init__(self, cart_info):
        """
        初始化参数
        :param cart_info:
        """

        self.cart_info = cart_info
        self.goods_info_list = []
        self.discount_info_dic = {}
        self.discount_coupons_infos = []
        self.pay_date = ''

    def parse_info(self):
        """
        获取输入内容
        :return:
        """
        # 打折商品信息
        discount_info_list = re.findall(
            r'(\d{4}.\d{1,2}.\d{1,2}) \| (0.[1-9]) \| ([\u4e00-\u9fa5]+)', self.cart_info)
        for discount_info in discount_info_list:
            self.discount_info_dic[discount_info[-1]] = [discount_info[0], float(discount_info[1])]
        # 所购买商品信息
        goods_info_list = re.findall(r'(\d+) \* (.*?) : (\d+.\d+)', self.cart_info)
        self.goods_info_list = [[int(goods_info[0]), goods_info[1], float(goods_info[2])]
                                for goods_info in goods_info_list]
        # 支付日期
        self.pay_date = re.findall(r'(\d{4}.\d{1,2}.\d{1,2})\n', self.cart_info)[0]
        # 优惠券信息
        discount_coupons_infos = re.findall(r'(\d{4}.\d{1,2}.\d{1,2}) (\d+) (\d+)',
                                            self.cart_info)
        self.discount_coupons_infos = [
            [discount_coupons[0], int(discount_coupons[1]), int(discount_coupons[2])]
            for discount_coupons in discount_coupons_infos]

    def filter_validity_discount_info(self):
        """
        过滤掉时间失效的优惠券
        :return:
        """
        # 将支付时间转换为秒
        pay_date = time.mktime(time.strptime(self.pay_date, "%Y.%m.%d"))
        # 获取优惠券时间信息
        for discount_info in self.discount_coupons_infos:
            # 将优惠券时间转化为秒
            discount_date = time.mktime(time.strptime(discount_info[0], "%Y.%m.%d"))
            if int(discount_date-pay_date) < 0:
                self.discount_coupons_infos.remove(discount_info)

    def pay_value(self):
        """
        获取最终支付金额
        :return: 打折再优惠后的总价格
        """
        self.parse_info()
        all_goods_pay = 0
        for goods_info in self.goods_info_list:
            pay_value = self.get_goods_pay_value(goods_info)
            all_goods_pay += pay_value
        # 先过滤出有效期内的优惠券
        self.filter_validity_discount_info()
        # 对优惠券价格进行降序排序
        sorted_discount_coupons_info = sorted(self.discount_coupons_infos,
                                              key=lambda d: d[1], reverse=True)
        # 再过滤出符合满减条件的优惠券
        filter_discount_coupons_info = filter(lambda d: all_goods_pay >= d[1],
                                              sorted_discount_coupons_info)
        discount_coupons_value = list(filter_discount_coupons_info)
        # 如果存在符合满减条件的优惠券，则使用最佳的优惠券
        if discount_coupons_value:
            all_goods_pay -= discount_coupons_value[0][2]
        # 指定小数位数为2位
        return round(all_goods_pay, 2)

    def get_goods_pay_value(self, goods_info):
        """
        获取所选商品打折后的总价格
        :param goods_info:单个商品信息
        :return:打折后的总价格
        """
        count, goods, price = goods_info
        # 如果所购买商品在打折商品类型内，并且支付日期在打折日期内，修改当前价格为打折后的价格
        for goods_type, goods_names in self.__goods_type_dic.items():
            if goods in goods_names:
                if (goods_type in self.discount_info_dic.keys()) \
                        and self.discount_info_dic[goods_type][0] == self.pay_date:
                    price = self.discount_info_dic[goods_type][1] * price
                break
        return price * count


def main():
    """
    测试主函数
    :return:
    """
    input_text = """
    2013.11.11 | 0.7 | 电子\n
    \n
    1 * ipad : 2399.00\n
    1 * 显示器 : 1799.00\n
    12 * 啤酒 : 25.0\n
    5 * 面包 : 9.00\n
    \n
    2013.11.11\n
    2014.3.2 1000 200\n
    """
    cart = Cart(input_text)
    cart.parse_info()
    res = cart.pay_value()
    print(res)


if __name__ == '__main__':
    main()
