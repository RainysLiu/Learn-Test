

input_str = input('请输入行数M和和列数N(以英文“,”分开, 例如 :2,100):')
input_list = list(map(int, input_str.strip().split(',')))
if not len(input_str) != 2:
    print('输入行数M和和列数有误!')
M = input_list[0]
N = input_list[1]
all_list = []
for line in range(1, M + 1):
    line_list = []
    input_str = input('请输入%s个整数，代表每个位置方块个数，以英文“,”分开:' % N)
    input_list = list(map(int, input_str.strip().split(',')))
    if len(input_list) != N:
        print('每个位置方块个数输入有误！')
    for num in input_list:
        line_list.append(num)
    all_list.append(line_list)
print(all_list)
