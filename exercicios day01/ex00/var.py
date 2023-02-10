a = 42
b = "42"
c = "quarante-deux"
d = 42.0
e = True
f = [42]
g = {42: 42}
h = (42,)
i = set()

def my_var(): 
    print(a, " has a type ", a.__class__)
    print(b, " has a type ", b.__class__)  
    print(c, " has a type ", c.__class__)
    print(d, " has a type ", d.__class__)
    print(e, " has a type ", e.__class__)
    print(f, " has a type ", f.__class__)
    print(g, " has a type ", g.__class__)
    print(h, " has a type ", h.__class__)
    print(i, " has a type ", i.__class__)

if __name__ == '__main__':
    my_var()


