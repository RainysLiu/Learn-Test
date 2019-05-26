def Singleton(cls):
    ins = {}

    def singleton(*args, **kargs):
        if cls not in ins:
            ins[cls] = cls(*args, **kargs)
        return ins[cls]

    return singleton


@Singleton
class A(object):
    a = 1

    def __init__(self, x=0):
        self.x = x


a1 = A(3)
a2 = A(2)

print(a1)
print(a2)
