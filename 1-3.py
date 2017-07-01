#Given two strings determine if one is a permutation of another
#
#Caution: Do whitespace and caps count?
#
#Elegant Solution: Sort O(n log(n))
def perm(st1, st2):
	one = sorted(st1)
	two = sorted(st2)
	if one == two:
		return True
	return False

print "perm"
print perm("hello", "lloeh")  #T
print perm("hello", "hello")  #T
print perm("hello", "Hello")  #clarify
print perm("hello", "hel lo") #clarity
print perm("hello", "helo")   #F
print perm("hello", "")       #F
print perm("", "")            #T

#Effecent Solution: Hash O(n)
def perm2(st1, st2):
	table1 = {}
	table2 = {}
	
	for item in st1:
		if item in table1:
			table1[item] += 1
		else:
			table1[item] = 1

	for item in st2:
		if item in table2:
			table2[item] += 1
		else:
			table2[item] = 1
	print table1
	print table2		
	if table1 == table2:
		return True
	return False

print "perm2"
print perm2("hello", "lloeh")  #T
print perm2("hello", "hello")  #T
print perm2("hello", "Hello")  #clarify
print perm2("hello", "hel lo") #clarity
print perm2("hello", "helo")   #F
print perm2("hello", "")       #F
print perm2("", "")            #T
