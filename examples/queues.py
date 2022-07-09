#Queues

#Queues are FIFO
#Nodes are added with enqueue
#Nodes are removed with dequeue

#Data Structures you can use:
#List - for something to be a queue you add on 1 end and remove on 1 end
#end is O(1) and beginning is O(n)

#With a linked list, you want to remove from the head and add from the tail to keep both sides O(1) instead of O(n)


#Queues use terms "first" and "last"

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class Queue:
    def __init__(self, value):
        new_node = Node(value)
        #set first and last values equal to new_node
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        temp = self.first
        #while temp is not empty
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def enqueue(self, value):
        new_node = Node(value)
        #check if list is empty
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
        	#set the last item's next value to new_node
            self.last.next = new_node
            #set last to equal the new_node
            self.last = new_node
        self.length += 1

    def dequeue(self):
        if self.length == 0:
            return None
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None
        self.length -= 1
        return temp

my_queue = Queue(4)

my_queue.print_queue()

###ENQUE SECTION
my_queue = Queue(1)
my_queue.enqueue(2)

my_queue.print_queue()


#DEQUEUE SECTION
 
my_queue = Queue(1)
my_queue.enqueue(2)

# (2) Items - Returns 2 Node
print(my_queue.dequeue())
# (1) Item -  Returns 1 Node
print(my_queue.dequeue())
# (0) Items - Returns None
print(my_queue.dequeue())
