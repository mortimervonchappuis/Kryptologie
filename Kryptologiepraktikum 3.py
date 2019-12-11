from random import randrange
from pickle import dump, load
from os import listdir


def gcd(a, b):
	if b == 0:
		return a
	return gcd(b, a % b)

if gcd(282, 240) == 6:
	print("gcd(282, 240) = 6")
if gcd(9**100+1, 10**100+1) == 401:
	print("gcd(9**100+1, 10**100+1) = 401")

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
		p = randrange(1<<(bit_size>>1))
		q = randrange(1<<(bit_size>>1))
		self.n = p*q
		self.e = (1<<16)+1
		self.d = solve(self.e, 1, (p-1) * (q-1))
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
	rsa = RSA(333)
	dump(rsa, open(file_name, "wb"))


print(rsa)
