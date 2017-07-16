#Design a stack which, in addition to push and pop, also has a return min function - 
#all fn run in O(1)
#Solution keep track of min element at each state
class Stack(object):

	def __init__(self):
		self.values = []
		self.mini = []

	def push(self, n):
		self.values.append(n)
		if not self.mini:
			self.mini.append(n)
		else:
			curMin = self.mini.pop()
			if n <= curMin:
				self.mini.append(curMin)
				self.mini.append(n)
			else:
				self.mini.append(curMin)
				self.mini.append(curMin)

	def pop(self):
		self.mini.pop()
		return self.values.pop()

	def minE(self):
		return self.mini[len(self.mini) - 1]


stk = Stack()
stk.push(5)
print stk.minE()     #5
stk.push(6)
print stk.minE()     #5
stk.push(4)
print stk.minE()     #4
stk.push(2)
print stk.minE()     #2

print stk.pop()      #2
print stk.minE()     #4
print stk.pop()      #4
print stk.minE()     #5
print stk.pop()      #6
print stk.minE()     #5
print stk.pop()      #5
