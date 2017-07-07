#Replace all spaces in a character array with %20.  Assume sufficient space at the end of
#the array
#Solution: Count spaces, Loop backwards, shifting characters as you go. O(n)
def twenty(charray, n):
	spaces = 0
	for i in range(0, n):
		if charray[i] == " ":
			spaces += 1

	shift = spaces * 2
	for j in range(n - 1, 0, -1):
		if charray[j] == " ":
			charray[j + shift - 2] = "%"
			charray[j  + shift - 1] = "2"
			charray[j + shift] = "0"
			shift = shift - 2
		else:
			charray[j + shift] = charray[j]

	return charray


print twenty(["M", "r", " ", "J", "o", "h", "n", " ", "S", "m", "i", "t", "h", " ", " ", " ", " "], 13)