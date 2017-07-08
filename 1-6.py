#Rotate an NxN matrix by 90 degrees
#Solution: row1 = col1 - double loop O(n^2) time O(n) space
def rotate(matx, n):
	new = [[0 for x in range(n)] for y in range(n)]
	for i in range(0, n):
		for j in range(0, n):
			new[j][n - 1 - i] = matx[i][j]
	return new


#In place O(n^2), no extra space/memory
#Transpose and flip rows is easier but O(2n^2) = O(n^2) time
'''def rotateIP(a, n):
	for x in range(0, n/2):
		for y in range(0, n/2):
			print a
			temp = a[x][y]
			a[x][y] = a[y][n-1-x]
			a[y][n-1-x] = a[n-1-x][n-1-y]
			a[n-1-x][n-1-y] = a[n-1-y][x]
			a[n-1-y][x] = temp
	return a'''




old = [[0 for x in range(2)] for y in range(2)]
old[0][0] = 1
old[0][1] = 2
old[1][0] = 3
old[1][1] = 4
print old
print rotate(old, 2)

four = [[0 for x in range(4)] for y in range(4)]
four[0][0] = 1
four[0][1] = 2
four[0][2] = 3
four[0][3] = 4
four[1][0] = 5
four[1][1] = 6
four[1][2] = 7
four[1][3] = 8
four[2][0] = 9
four[2][1] = 10
four[2][2] = 11
four[2][3] = 12
four[3][0] = 13
four[3][1] = 14
four[3][2] = 15
four[3][3] = 16
print four
print rotate(four, 4)