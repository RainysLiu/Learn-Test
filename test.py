

input_str = input('����������M�ͺ�����N(��Ӣ�ġ�,���ֿ�, ���� :2,100):')
input_list = list(map(int, input_str.strip().split(',')))
if not len(input_str) != 2:
    print('��������M�ͺ���������!')
M = input_list[0]
N = input_list[1]
all_list = []
for line in range(1, M + 1):
    line_list = []
    input_str = input('������%s������������ÿ��λ�÷����������Ӣ�ġ�,���ֿ�:' % N)
    input_list = list(map(int, input_str.strip().split(',')))
    if len(input_list) != N:
        print('ÿ��λ�÷��������������')
    for num in input_list:
        line_list.append(num)
    all_list.append(line_list)
print(all_list)
