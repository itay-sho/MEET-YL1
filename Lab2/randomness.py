import random
def TailsOrHeads():
	result = random.randint(0,1)
	if (result == 1):
		return "Tails"
	return "Head"

def TailsOrHeads2():
	howManyTimes = int(raw_input("Please enter how many time do you want to try tails or head."))
	result = 0.0
	for i in xrange(howManyTimes):
		result = result + random.randint(0,1)
	return result / howManyTimes

if __name__ == "__main__":
	while True:
		userInput = raw_input("Enter 'n' if you want to to check heads or tails");
		if userInput == "n":
			print TailsOrHeads()
		if userInput == "nTimes":
			print TailsOrHeads2()
