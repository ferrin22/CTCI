#Given fn isSubstring, determine whether one word is a rotation 
#of another using one call to isSubstring
#Solution: check for equal lengths, double one string
#Time for isSubstring (probably O(n)) + O(1) = O(n)
def rotation(st1, st2):
	if st1 and st2:
		if len(st1) == len(st2):
			twice = st2 + st2
			if st1 in twice:
				return True
	return False


print rotation("waterbottle", "erbottlewat") #True
print rotation("hello", "llojhe") #False
print rotation("waterbottle", "") #False
print rotation(" ", "erbottlewat") #False
