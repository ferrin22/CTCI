#Replace all spaces in a character array with %20.  Assume sufficient space at the end of
#the array
#Solution: Loop until end of string O(n)
def twenty(charray, n):
	space = 0
	for i in range(0,n):
		if charray[i] == " ":
			space += 1
	newlen = n + (space * 2)
	for j in range(n - 1, 0, -1):
		if charray[j] == " ":
			charray[newlen - 1] = "0"
			charray[newlen - 2] = "2"
			charray[newlen - 3] = "%"
			newlen -= 3
		else:
			charray[newlen - 1] = charray[j]
			newlen -= 1
	return charray



print twenty(["M", "r", " ", "J", "o", "h", "n", " ", "S", "m", "i", "t", "h", " ", " ", " ", " "], 13)