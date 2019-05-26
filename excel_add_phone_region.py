from openpyxl import load_workbook
import phone


def get_phone_region(phone_num):
    """
    获取电话号码的归属地信息
    :param phone_num: 电话号码
    :return: 归属信息
    """
    info = phone.Phone().find(phone_num)
    if info is not None:
        region = info['province'] + ' ' + info['city'] + ' ' + info['phone_type']
    else:
        region = '该号码暂未查询到归属地，请检查号码正确性或手动查询！'
    return region


def add_region_in_excel(excel_path, sheet_name):
    """
    添加归属地和运营商信息到excel文件中
    :param excel_path: excel表格的路径名字
    :param sheet_name: sheet的名字
    :return: 无
    """
    excel = load_workbook(excel_path)   # 读取表格
    if not sheet_name:
        sheet = excel.get_active_sheet()   # 读取当前激活的页签
    else:
        sheet = excel.get_sheet_by_name(sheet_name)   # 读取指定名页签
    phone_col = sheet['C']   # 拿到C列
    for index in range(2, len(phone_col) + 1):   # 从C列第2行开始循环
        phone_data = sheet['C%s' % index]   # 拿到C列当前行单元格对象
        phone_num = phone_data.value.strip()   # 去除号码前后空格，得到号码字符串
        phone_region = get_phone_region(phone_num)   # 获得当前号码归属地
        print('正在向D列第' + str(index) + '行(对应号码为' + phone_num + ')写入归属地信息: ' + phone_region)   # 打印出行数，号码，地区信息
        sheet['D%s' % index] = phone_region   # 将归属地内容写入D列对应行
    excel.save(excel_path)


if __name__ == '__main__':
    try:
        excel_path = input('请输入包含excel文件名的完整路径(按enter确认):')
        sheet_name = input('请输入你要操作的sheet名(如果仅有一个sheet，请直接按enter):')
        if sheet_name.strip() == '':
            sheet_name = None
        add_region_in_excel(excel_path, sheet_name)
    except Exception as e:
        print('[ERROR]发生错误:%s' % e)