#Create stack that operates as a single stack but is actually multiple stacks
#that overflow once they reach a given capacity
#Solution Keep stacks in dictonary so you can easily add new onew
#without new calls to the constructor or specifying the number in advance
class Stack(object):
	def __init__(self, capacity):
		self.table = {}
		self.table[0] = []
		self.curStk = 0
		self.capacity = capacity - 1



	def push(self, number):
		if len(self.table[self.curStk]) - 1 >= self.capacity:
			self.curStk += 1
			self.table[self.curStk] = []
		self.table[self.curStk].append(number)

	def pop(self):
		if not self.table[self.curStk]:
			del self.table[self.curStk]
			self.curStk -= 1
		return self.table[self.curStk].pop()

	def prnt(self):
		print self.table





mystack = Stack(2)
mystack.prnt()
mystack.push(1)
mystack.prnt()
mystack.push(1)
mystack.prnt()
mystack.push(1)
mystack.prnt()
mystack.push(1)
mystack.prnt()
mystack.push(1)
mystack.prnt()
mystack.push(1)
mystack.prnt()
mystack.push(1)
mystack.prnt()
mystack.pop()
mystack.prnt()
mystack.pop()
mystack.prnt()
mystack.pop()
mystack.prnt()
mystack.pop()
mystack.prnt()
mystack.pop()
mystack.prnt()
mystack.push(2)
mystack.prnt()
mystack.push(2)
mystack.prnt()


