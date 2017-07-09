#If an element in an MxN matrix is zero, its entire column and row get set to zero
#Loop to find 0's in matrix, store them.  For corresponding rows, cols, loop to insert 0's
# O(mn)
def zero(matx, M, N):
	table = []
	for x in range(0, M):
		for y in range(0, N):
			if matx[x][y] == 0:
				table.append((x,y))
	for pair in table:
		for i in range(0, N):
			matx[pair[0]][i] = 0
		for j in range(0, M):
			matx[j][pair[1]] = 0
	return matx


mtx = [[0 for x in range(2)] for y in range(2)]
mtx[0][0] = 1
mtx[0][1] = 0
mtx[1][0] = 3
mtx[1][1] = 4
print mtx
print zero(mtx, 2, 2)

big = [[0 for x in range(3)] for y in range(4)]
big[0][0] = 1
big[0][1] = 2
big[0][2] = 3
big[1][0] = 4
big[1][1] = 5
big[1][2] = 6
big[2][0] = 0
big[2][1] = 8
big[2][2] = 9
big[3][0] = 0
big[3][1] = 10
big[3][2] = 11
print big
print zero(big, 4, 3)