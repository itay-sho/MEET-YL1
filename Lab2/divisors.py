def allNumbers():
	n = int(raw_input("Please enter a number"))
	for num in xrange(1,n):
		print num
def divisorsOnly():
	n = int(raw_input("Please enter a number"))
	for num in xrange(1,n):
		if n % num == 0:
			print num
def divisors(n):
	for num in xrange(1,n):
		if n % num == 0:
			print num
if __name__ == "__main__":
	allNumbers()
	divisorsOnly()
	divisors(100)
