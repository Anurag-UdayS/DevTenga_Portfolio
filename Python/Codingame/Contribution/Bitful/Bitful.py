import random

def newSet():
	a = random.randint(0, 2**15)
	b = random.randint(0, 2**15)
	c = random.randint(0, 2**15)
	print(a & b)
	print(a | b)
	print(a ^ b ^ c)
	return ( (a & b, a | b, a ^ b ^ c), (a, b, c) )

def solveSet():
	results = newSet()
	a = results[0][0]
	o = results[0][1]
	x = results[0][2]

	print("Result: " + str((o & ~a) ^ x) )
	print("Expected: " + str(results[1][2]))

if __name__ == '__main__':
	solveSet()