def fab(n):
    if n < 1:
        print('输入有误！')
        return -1
    if n ==1 or n ==2:
        return 1
    else:
        return fab(n-1) + fab(n-2)
n = 30
result = fab(n)
if result != -1:
    print('第%d个月总共有%d对小兔崽子诞生！' % (n,result))
