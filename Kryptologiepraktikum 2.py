from random import randrange


def miller_rabin(n, it=1000):
    return all(witness(n, randrange(1, n)) for _ in range(it))


def witness(n, a, status=False):
    k = n-1
    x = pow(a, k, n) 
    while x == 1 and k % 2 == 0:
        k >>= 1
        x = pow(a, k, n)
        #print(f"n={n} a={a} x={x}, k={k}")
    return x in (1, n-1)


def next_prime(n, it=1000):
    n += (1&n)^1
    while not miller_rabin(n, it):
        n += 2
    return n

test = [(17, 5, 17), (32, 5, 37), (pow(10, 100), 10, pow(10, 100) + 267)]

if all(next_prime(a, b) == c for a, b, c in test):
    print("NextPrime Test Bestanden")

