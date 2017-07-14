#Use a single array to represent three stacks
#Solution: Break the array into three even sections
class threeStack(object):
	def __init__(self, n):
		self.values = []
		for i in range(0, n):
			self.values.append(None)

	def push1(self, x):
		for j in range(0, len(self.values)/3 - 1):
			if not self.values[j]:
				self.values[j] = x
				break

	def pop1(self):
		for k in range(0, len(self.values)/3):
			if not self.values[k]:
				temp = self.values[k - 1]
				self.values[k - 1] = None
				return temp
		return None

	def printt(self):
		print self.values


stk = threeStack(9)
stk.printt()
stk.push1(2)
stk.printt()
stk.push1(3)
stk.printt()
print stk.pop1()
stk.printt()
print stk.pop1()
stk.printt()