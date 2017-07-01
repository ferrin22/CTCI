#Implement an algorithm to determine if a string has all unique characters
#Soluton: Hash 0(n)
def unique(string):
	table = {}
	for element in string:
		if element in table:
			table[element] += 1
		else:
			table[element] = 1
	for bucket in table:
		if table[bucket] > 1:
			return True
	return False

print("unique")
print unique("test")       #T
print unique("abcdefghi")  #F
print unique("")           #F
print unique("0")          #F
print unique("11")         #T
print unique("abcdefghia") #T

#What if you can't use additional data structures?
#Solution: Sort 0(n log(n))
def unique2(string):
	ordered = sorted(string) #.sort() only works on lists
	for i in range(0,len(string) - 1):
		if ordered[i] == ordered[i+1]:
			return True
	return False

print("unique2")
print unique2("test")       #T
print unique2("abcdefghi")  #F
print unique2("")           #F
print unique2("0")          #F
print unique2("11")         #T
print unique2("abcdefghia") #T