i = 0
while i<2:
    allcolor = input('请输入')
    revallcolor = allcolor[-1:0:-1]
    color1 = input('请输入')
    color2 = input('请输入')
    if (color1 in allcolor and color2 in allcolor) and (color1 in revallcolor and color2 in revallcolor):
        print('both')
    elif color1 in allcolor and color2 in allcolor:
        print('forward')
    elif color1 in revallcolor and color2 in revallcolor:
        print('backward')
    else:
        print('invalid')
    i += 1