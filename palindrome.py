example = ["mom","dad","abcba","test"]

def isPal(word):
	if len(word) <= 1:
		return True
	else:
		left = 0
		right = len(word) - 1
		while left < right:
			if word[right] == word[left]:
				left += 1
				right -= 1
			else:
				return False
		return True


def isPal1(word):
	return word == "".join(reversed(word))
	



for ex in example:
	print isPal1(ex)
