"""
Stacks:

An analogy is a Stacks tennis balls. You can't get to the first one 

If you're using a list as a stack, then you want to make sure you are removing from the end and not the beginning. This makes the operation O(1) instead of O(n) if you removed it from the beginning

The terms head and tail from linked lists can be replaced with 'top' and 'bottom' but you really don't end up using tail or bottom



"""
class Node:
	def __init__(self, value):
		self.value = value
		self.next = None


class Stack:
	def __init__(self, value):
		new_node = Node(value)
		self.top = new_node
		self.height = 1

	def print_stack(self):
		temp = self.top
		while temp is not None:
			print(temp.value)
			temp = temp.next

	def push(self, value):
		new_node = Node(value)
		if self.height == 0:
			self.top = new_node
		else:
			#point new_node next to the same that self.top is pointing to (from above)
			new_node.next = self.top
			#moves top up and adds new_node into our stack
			self.top = new_node
		self.height += 1


	def pop(self):
		if self.height == 0:
			return None
		temp = self.top
		self.top = self.top.next
		temp.next = None
		self.height -= 1
		return temp

my_stack = Stack(4)

my_stack.print_stack()



#PUSH SECTION
my_stack = Stack(2)
my_stack.push(1)

my_stack.print_stack()


#POP SECTION
my_stack = Stack(7)
my_stack.push(23)
my_stack.push(3)
my_stack.push(11)

print(my_stack.pop(), '\n')

my_stack.print_stack()
