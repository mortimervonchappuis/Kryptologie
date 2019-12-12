from random import randrange, randint
from pickle import dump, load
from os import listdir


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


def next_prime(n, it=100):
    if n == 2: return n
    n += (1&n)^1 # macht n ungerade
    while not miller_rabin(n, it):
        n += 2
    return n


def gcd(a, b):
	if b == 0:
		return a
	return gcd(b, a % b)


def eea(a, b):
	r_0, r_1 = a, b
	x_0, x_1 = 1, 0
	y_0, y_1 = 0, 1
	while r_0 % r_1 != 0:
		r_0, r_1, q = r_1, r_0 % r_1, r_0 // r_1
		x_0, x_1 = x_1, x_0 - x_1 * q
		y_0, y_1 = y_1, y_0 - y_1 * q
	return x_1, y_1


def solve(c, d, m): # c * x = d mod m
	g = gcd(c, m)
	if d % g != 0:
		return -1
	x, y = eea(c, m)
	return (x * d // g)%m


class RSA:
	def __init__(self, bit_size):
		p = next_prime(randrange(1<<(bit_size>>1)))
		q = next_prime(randrange(1<<(bit_size>>1)))
		l = (p-1) * (q-1)
		self.n = p*q
		self.e = (1<<16)+1
		self.d = solve(self.e, 1, l)
		if (self.d*self.e) % l != 1:
			raise Exception("my file is stupid")
		del p, q

	def __str__(self):
		return f"""N = {self.n}
e = {self.e}
d = {self.d}
"""
	
	def __repr__(self):
		return str(self)

	def encryp(self, m):
		if type(m) == int:
			return pow(m, self.e, self.n)
		return self.encryp(self.translate(m))

	def decryp(self, c):
		if type(c) == int:
			return pow(c, self.d, self.n)
		return self.decryp(self.translate(c))

file_name = "RSA.file"	
if file_name in listdir():
	rsa = load(open(file_name, "rb"))
else:
	rsa = RSA(1024)
	dump(rsa, open(file_name, "wb"))


m = 3962244765921027422324033016186664415890198460337848139608060813664838760555578941492735634914129325431171730776269799458129102124351797100583267083593341123177275423550705360315626050218490820716972939618514336576809598864722943090771495140609759992227381039831613713096263671049685860747014367728932617732

print(m == rsa.decryp(rsa.encryp(m)))
print(rsa)

