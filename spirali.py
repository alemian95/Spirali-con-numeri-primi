from matplotlib import pyplot as plt
import numpy as np
import cmath as m

class Complex:
    # inizializzazione del numero complesso, qui avviene la conversione da coordinate polari a coordinate cartesiane
    def __init__(self, abs, arg):
        self.x = abs * m.cos(arg)
        self.y = abs * m.sin(arg)


def eratostene(n):
    # creazione dell'array che provvederà ad indicare se il numero è primo o meno, inizialmente tutti i numeri sono considerati primi
    a = []
    # creazione dell'array che conterrà il valore di tutti i numeri primi trovati
    primes = []
    # come precedentemente specificato, si inizializza l'array indicatore a true
    for i in range(n+1):
        a.append(True)
    # crivello di eratostene
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

# data una lista di numeri complessi, restituisce una lista delle parti reali
def getX(complex):
    x = []
    for c in complex:
        x.append(c.x)
    return x

# data una lista di numeri complessi, restituisce una lista delle parti immaginarie
def getY(complex):
    y = []
    for c in complex:
        y.append(c.y)
    return y


# lettura del massimo valore dei numeri primi generati
num = int(input(" > "))

# calcolo dei numeri primi tramite il crivello di eratostene
primes = eratostene(num)

# conversione dei numeri primi in numeri complessi per la conversione da coordinate polari a cartesiane
complex = toComplex(primes)

xpoints = np.array(getX(complex))
ypoints = np.array(getY(complex))

plt.plot(xpoints, ypoints, 'o')
plt.show()
