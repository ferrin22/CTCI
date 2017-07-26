#Create a fn that solves Tower of Hanoi using stacks
def towerShift(stk1, stk2, stk3):
	n = len(stk1)
	if n%2 != 0:      #odd
		while stk1 or stk2:

			print stk1, stk2, stk3

			if stk1 and not stk3:
				stk3.append(stk1.pop())
			elif stk3 and not stk1:
				stk1.append(stk3.pop())
			else:
				if stk1[len(stk1) - 1] > stk3[len(stk3) - 1]:
					stk1.append(stk3.pop())
				else:
					stk3.append(stk1.pop())
			if stk1 or stk2:
				if stk1 and not stk2:
					stk2.append(stk1.pop())
				elif stk2 and not stk1:
					stk1.append(stk2.pop())
				else:
					if stk1[len(stk1) - 1] > stk2[len(stk2) - 1]:
						stk1.append(stk2.pop())
					else:
						stk2.append(stk1.pop())
			if stk1 or stk2:
				if stk2 and not stk3:
					stk3.append(stk2.pop())
				elif stk3 and not stk2:
					stk2.append(stk3.pop())
				else:
					if stk2[len(stk2) - 1] > stk3[len(stk3) - 1]:
						stk2.append(stk3.pop())
					else:
						stk3.append(stk2.pop())

		return stk3

A = [7,6,5,4,3,2,1]
B = []
C = []

print towerShift(A, B, C)