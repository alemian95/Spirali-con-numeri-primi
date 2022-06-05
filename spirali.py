from matplotlib import pyplot as plt
import numpy as np
import cmath as m

class Complex:
    def __init__(self, abs, arg):
        self.x = abs * m.cos(arg)
        self.y = abs * m.sin(arg)


def eratostene(n):
    a = []
    primes = []
    for i in range(n+1):
        a.append(True)
    for i in range (2, n+1):
        if not a[i]:
            continue
        primes.append(i)
        p = i*2
        while p < n+1:
            a[p] = False
            p += i

    return primes

def toComplex(primes):
    cpx = []
    for p in primes:
        cpx.append(Complex(p, p))
    return cpx

def getX(complex):
    x = []
    for c in complex:
        x.append(c.x)
    return x

def getY(complex):
    y = []
    for c in complex:
        y.append(c.y)
    return y

num = int(input(""))
primes = eratostene(num)
complex = toComplex(primes)

xpoints = np.array(getX(complex))
ypoints = np.array(getY(complex))

plt.plot(xpoints, ypoints, 'o')
plt.show()