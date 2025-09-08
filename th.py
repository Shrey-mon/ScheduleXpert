import threading
from threading import *
import random

l = [i for i in range(0, 200)]


def fun1(l1):
    while l1:
        n = random.choice(l1)
        print("1", n)
        l1.remove(n)


def fun2(l2):
    while l2:
        n = random.choice(l2)
        print("2", n)
        l2.remove(n)

def fun3(l3):
    while l3:
        n = random.choice(l3)
        print("3", n)
        l3.remove(n)

def fun4(l4):
    while l4:
        n = random.choice(l4)
        print("4", n)
        l4.remove(n)

def fun5(l5):
    while l5:
        n = random.choice(l5)
        print("5", n)
        l5.remove(n)

def make_threads(fun, arg):
    return threading.Thread(target=fun, args=[arg])

tl = [fun1, fun2, fun3, fun4, fun5]
# sl = []
# for fun in tl:
#     t=make_threads(fun, l.copy())
#     t.start()

# for i in sl:
#     i.start()

# t1 = threading.Thread(target=fun1, args=[l.copy()])
# t2 = threading.Thread(target=fun2, args=[l.copy()])
#
# t1.start()
# t2.start()


# a=True
#
# while not a:
#     print("hello")

d={
    'a':1,
    'b':5
}
print(sum(d.values()))