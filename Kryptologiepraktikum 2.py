from random import randrange
from matplotlib import pyplot as plt


def miller_rabin(n, it=1000):
    return all(witness(n, randrange(1, n)) for _ in range(it))


def witness(n, a):
    k = n-1
    x = pow(a, k, n) 
    while x == 1 and k % 2 == 0:
        k >>= 1
        x = pow(a, k, n)
        #print(f"n={n} a={a} x={x}, k={k}")
    return x in (1, n-1)


def next_prime(n, it=1000):
    n += (1&n)^1 # macht n ungerade
    while not miller_rabin(n, it):
        n += 2
    return n


def number_witness(n):
    return sum(not witness(n, a) for a in range(1, n))


def mean_distance(n, anz, it=1000):
    distance = lambda x: next_prime(x, it) - x
    return sum(distance(randrange(n))  for _ in range(anz))/anz


test_A = [(17, 5, 17), (32, 5, 37), (pow(10, 100), 10, pow(10, 100) + 267)]

if all(next_prime(a, b) == c for a, b, c in test_A):
    print("Next-Prime-Test Bestanden")

test_B = [(9, 6), (325, 306)]

if all(number_witness(a) == b for a, b in test_B):
    print("Number-Witness-Test Bestanden")
