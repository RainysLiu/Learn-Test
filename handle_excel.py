import xlrd
import xlwt
from xlutils.copy import copy

# 定义一个excel名和sheet名
excel_name = '我的excel.xls'
sheet1 = '我的sheet1'

# 创建工作薄对象
workbook = xlwt.Workbook(encoding = 'ascii')
# 创建sheet
worksheet = workbook.add_sheet(sheet1)
# 往0行写表头入数据
header = ['N0.','姓名', '年龄', '性别']
for clu_num in range(len(header)):
    worksheet.write(0, clu_num, header[clu_num])
# 保存工作簿
workbook.save(excel_name)



# 打开已有表格，创建读对象
rexcel = xlrd.open_workbook(excel_name)
# 获取sheet1
sheet = rexcel.sheet_by_name(sheet1)
# 获取sheet1最大行数
row_num = sheet.nrows

# 将读对象转换成写对象
wexcel = copy(rexcel)
# wexcel中获取第0个sheet
wsheet = wexcel.get_sheet(0)
users = [
    ['张三', '16', '男'],
    ['李四', '16', '女'],
    ['李四', '18', '男'],
    ['赵六', '11', '女'],
    ]
# 双层遍历数据，raw_num待变要写的数据行，clu_num代表列
for data_raw in range(len(users)):
    wsheet.write(row_num, 0, str(data_raw+1))
    for clu_num in range(len(users[data_raw])):
        words = users[data_raw][clu_num]
        print(words)
        wsheet.write(row_num, clu_num+1, words)
    row_num +=1
# 保存添加的行
wexcel.save(excel_name)

