if __name__ == "__main__":
	users = ["name","age"]
	for i in xrange(3):
		users["name"][i] = raw_input("Please enter your name: ")
		users["age"][i] = int(raw_input("Please enter your age: "))
	print users
