from random import randint
from matplotlib import pyplot as plt
import pickle


def miller_rabin(n, it=1000):
    return all(witness(n, randint(1, n-1)) for _ in range(it))


def witness(n, a):
    k = n-1
    x = pow(a, k, n)
    if x != 1: return False
    while x == 1 and k % 2 == 0:
        k >>= 1
        x = pow(a, k, n)
    return x in (1, n-1)


def next_prime(n, it=1000):
    if n == 2: return n
    n += (1&n)^1 # macht n ungerade
    while not miller_rabin(n, it):
        n += 2
    return n


def number_witness(n):
    return sum(not witness(n, a) for a in range(1, n))


def mean_distance(n, anz, it=1000):
    distance = lambda x: next_prime(x, it) - x
    return sum(distance(randint(2, n))  for _ in range(anz))/anz


test_A = [(17, 5, 17), (32, 5, 37), (pow(10, 100), 10, pow(10, 100) + 267)]

if all(next_prime(a, b) == c for a, b, c in test_A):
    print("Next-Prime-Test bestanden")

test_B = [(9, 6), (325, 306)]

if all(number_witness(a) == b for a, b in test_B):
    print("Number-Witness-Test bestanden")

r = range(10, 10**8, 10**4)

A = [mean_distance(n, 10, 10) for n in r]
pickle.dump(A, open("a.file", "wb"))
B = [mean_distance(n, 100, 10) for n in r]
pickle.dump(B, open("b.file", "wb"))
C = [mean_distance(n, 1000, 10) for n in r]
pickle.dump(C, open("c.file", "wb"))


plt.scatter(list(r), A, s=0.5)
print("First Plot")
plt.scatter(list(r), B, s=0.5)
print("Second Plot")
plt.scatter(list(r), C, s=0.5)
print("Third Plot")

plt.xlabel("$N$")
plt.ylabel("$\Delta P_N$")
plt.title("Distances to next prime $\Delta P_N$ size $N$")
plt.show()
