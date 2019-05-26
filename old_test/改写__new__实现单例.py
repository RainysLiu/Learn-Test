
class Earth(object):
    ins = None
    def __new__(cls):
        if cls.ins==None:
            cls.ins==object.__new__
        else:
            return cls.ins
        


a = Earth()
print(id(a))
b = Earth()
print(id(b))
