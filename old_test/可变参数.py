

def one(name):
    print(name)
one(['李白','李世民'])


def two(*name):
    for n in name:
        print(n)
two(*['李白','李世民'])


def change(**name):
    print(name)
change(**{'a':'李白','b':'李世民'})
