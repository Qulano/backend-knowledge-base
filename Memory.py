import copy
import sys
import gc

first = [1, 45, 255]    
second = first
print(id(first), id(second), first is second)
first.append(55)
print(id(first), id(second), first is second)


a = 10
b = a
print(id(a), id(b))
a += 1
print(id(a), id(b))


num_1 = 256
num_2 = int("256")
print(num_1 == num_2, num_1 is num_2)


numb_1 = 1000
numb_2 = int("1000")
print(numb_1 == numb_2, numb_1 is numb_2)


tup = (1, [4, 5, 6])
print(id(tup), id(tup[1]))
try:
    tup[0] = 7
except TypeError as e:
    print(e)
tup[1].append(42)
print(tup, id(tup), id(tup[1]))
try:
    s = {tup}
except TypeError as e:
    print(e)
    
    
ls = [13, 34, 23, 1]
lb = ls
ls += [7]
print(ls, lb, id(ls), id(lb))
ls = ls + [7]
print(ls, lb, id(ls), id(lb))


def f(a=[]):
    a.append(a)
    return a, id(a)
print(f())
print(f())
print(f())
print(f.__defaults__)

def z(item, cart=None):
    if cart is None:
        cart = []
    cart.append(item)
    return cart
    
r1 = z("Булочка")
r2 = z("Револьвер")
r3 = z("Винтовка")
print(z.__defaults__)
print(r1, r2, r3)
print(id(r1), id(r2), id(r3))


ls = [[34, 37, 82], [1, 2, 3], [22, 33, 11]]
ls_copy = ls.copy()
print(id(ls), id(ls_copy), id(ls[0]), id(ls_copy[0]))
ls_copy[0].append(19)
print(ls)

ld = [[1, 3, 7], [14, 17, 2]]
ld_dcop = copy.deepcopy(ld)
print(id(ld), id(ld_dcop), id(ld[0]), id(ld_dcop[0]))
ld_dcop[0].append(6)
print(ld_dcop)

ac = []
for i in range(10):
    ac.append(ac)

a_cop = copy.deepcopy(ac)
print(a, "\n", a_cop, "\n", id(a), id(a_cop))


a = [1, 2]
print(sys.getrefcount(a))
b = a
print(sys.getrefcount(b))
del a
print(sys.getrefcount(b))


class Island:
    def __init__(self, name):
        self.name = name
        self.friend = None
    def __del__(self):
        print(f"Объект {self.name} уничтожен") 

isl_1 = Island("Одиночка")
del isl_1
print("---После del одиночки---")
gc.disable()
a = Island("А")
b = Island("Б")
a.friend = b
print(sys.getrefcount(a))
b.friend = a
del a
del b
print("--- Переменные удалены, ждём gc.collect() ---")
removed = gc.collect()
print(removed)
gc.enable()
print(gc.get_count())




