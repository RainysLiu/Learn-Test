# 使用next()生成斐波那契数列
def Fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return '亲！没有数据了...'
# 调用方法，生成出10个数来
f=Fib(10)
print(f)

l=[]

while True:
    try:
        l.append(next(f))
    except:
        print('没有了')
        break
print(l)



for fi in f:
    print(fi)
