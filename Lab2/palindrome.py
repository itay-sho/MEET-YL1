def isPalindrome(word):
	wordLength = len(word)
	for i in xrange(wordLength):
		if word[i] != word[wordLength - i - 1]:
			print "Not a palindrome"
			return False
	print "Palindrome"
	return True
if __name__ == "__main__":
	while True:
		isPalindrome(raw_input("Please enter a word: "))
	
