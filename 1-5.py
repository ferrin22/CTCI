#Peform basic string compression using the counts of repeated characters
#Solution: Loop O(n)
def compressor(string):
	counter = 1
	compressed = []
	current = string[0]
	compressed.append(current)
	for i in range(1, len(string)):
		if string[i] == current:
			counter += 1
		else:
			compressed.append(counter)
			counter = 1
			current = string[i]
			compressed.append(current)
	compressed.append(counter)
	if len(compressed) > len(string):
		return string
	return compressed


print compressor("aabcccccaaa")
print compressor("abcde")
print compressor("aaAAaaAAAaaa")
print compressor("abcdeffffffffffffffffffffgh")
