class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        #If we have an empty linked list
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            #set  last item(tail)'s next equal to the new node
            self.tail.next = new_node
            #set the previous arrow on the new node to the same node that tail is pointing to
            new_node.prev = self.tail
            #set tail of self to new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        #If length is 0 there is no need to pop anything
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None 
        else:       
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length/2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev  
        return temp
        

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)

        new_node = Node(value)
        before = self.get(index - 1)
        after = before.next

        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node
        
        self.length += 1   
        return True  


    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()

        temp = self.get(index)
        
        temp.next.prev = temp.prev
        temp.prev.next = temp.next
        temp.next = None
        temp.prev = None

        self.length -= 1
        return temp

my_doubly_linked_list = DoublyLinkedList(7)

my_doubly_linked_list.print_list()



#For comparison, this is the linked list node class syntax
#Note the missing 'self.prev = None' line
#class Node:
    #def __init__(self, value):
        #self.value = value
        #self.next = None

###############
#
# APPEND SECTION
#
###############
my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)

my_doubly_linked_list.print_list()

###############
#
# POP SECTION
#
###############

my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)


# (2) Items - Returns 2 Node
print(my_doubly_linked_list.pop())
# (1) Item -  Returns 1 Node
print(my_doubly_linked_list.pop())
# (0) Items - Returns None
print(my_doubly_linked_list.pop())

###############
#
# PREPEND SECTION
#
###############
my_doubly_linked_list = DoublyLinkedList(2)
my_doubly_linked_list.append(3)

my_doubly_linked_list.prepend(1)

my_doubly_linked_list.print_list()


###############
#
# GET SECTION
#
###############
my_doubly_linked_list = DoublyLinkedList(0)
my_doubly_linked_list.append(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)


print(my_doubly_linked_list.get(1))
print(my_doubly_linked_list.get(2))

###############
#
# SET_VALUE SECTION
#
###############
my_doubly_linked_list = DoublyLinkedList(11)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(23)
my_doubly_linked_list.append(7)

my_doubly_linked_list.set_value(1,4)

my_doubly_linked_list.print_list()

###############
#
# INSERT SECTION
#
###############

my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(3)

my_doubly_linked_list.insert(1,2)

my_doubly_linked_list.print_list()


###############
#
# REMOVE SECTION
#
###############

my_doubly_linked_list = DoublyLinkedList(0)
my_doubly_linked_list.append(1)
my_doubly_linked_list.append(2)

print(my_doubly_linked_list.remove(1), '\n')

my_doubly_linked_list.print_list()
