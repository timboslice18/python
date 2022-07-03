class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
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
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        #check if list is empty
        if self.length == 0:
            return None
        #create temporary vars temp and pre
        temp = self.head
        pre = self.head
        #same thing as while(temp.next) is not None:
        while(temp.next):
            #set pre to temp
            pre = temp
            #set temp to temp.next; move temp over to the next item
            #exit while loop once temp.next is None (end of linked list)
            temp = temp.next
        #set tail to the 2nd to last node
        self.tail = pre
        #breaks the last item off the linked list
        self.tail.next = None
        #reflects the removal an item from the length
        self.length -= 1
        #If there was only 1 item in the linked list then the length would be 0 and you'd be stuck in a loop
        #we check again if length is equal to 0 and then set head and tail equal to None
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.value

    def prepend(self, value):
        #create node
        new_node = Node(value)
        #if ll is empty 
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            #point new node next to head
            new_node.next = self.head
            #sets head to the new node
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        #check length of ll
        if self.length == 0:
            return None
        #point temp to the head
        temp = self.head
        #move head over to the next item
        self.head = self.head.next
        #remove the first item from the list by setting next equal to None
        temp.next = None
        self.length -= 1
        #Edge case is when we have just 1 item in the ll to start with
        if self.length == 0:

            self.tail = None
        return temp

    def get(self, index):
        #Make sure the index is valid
        #If it is less than 0 or larger than the length of the ll it is invalid
        if index < 0 or index >= self.length:
            return None
        #set temp to the first item
        temp = self.head
        #for loop that runs the number of times that you need for the indexed value
        #the underscore is used if you are not planning to use the value inside the for loop
        for _ in range(index):
            temp = temp.next
        return temp

    #you have to name this set_value because python already has a built in set function
    def set_value(self, index, value):
        #use get to find the indexed value
        temp = self.get(index)
        #same as "if temp is not None"
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        #use the prepend method and exit out with the returned value
        if index == 0:
            return self.prepend(value)
        #use the append method and exit out with the returned value
        if index == self.length:
            return self.append(value)
        #insert new node somwehere in the middle
        new_node = Node(value)
        #assign temp to the item 1 behind the index
        temp = self.get(index - 1)
        #set the next value of the new node to the next item of temp
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1   
        return True  

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        #if index is 0 we can reuse pop_first method
        if index == 0:
            return self.pop_first()
        #If we're looking for the last item we can use pop method
        if index == self.length - 1:
            return self.pop()
        pre = self.get(index - 1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def reverse(self):
        #switch head and tail
        temp = self.head
        self.head = self.tail
        self.tail = temp
        #create after and before vars
        #after is on the right side of temp
        #these will be used to iterate through the LL as we reverse everything
        after = temp.next
        before = None
        #
        for _ in range(self.length):
            after = temp.next
            #this flips and sets next to None
            temp.next = before
            #before and temp are the same value
            before = temp
            #moves temp up to equal after
            temp = after

my_linked_list = LinkedList(1)
my_linked_list.append(2)


###############
#
# POP SECTION
#
###############
# (2) Items - Returns 2 Node
print(my_linked_list.pop())
# (1) Item -  Returns 1 Node
print(my_linked_list.pop())
# (0) Items - Returns None
print(my_linked_list.pop())


###############
#
# PREPEND SECTION
#
###############
my_linked_list = LinkedList(2)
my_linked_list.append(3)

my_linked_list.prepend(1)

my_linked_list.print_list()


###############
#
# POP_FIRST SECTION
#
###############
my_linked_list = LinkedList(2)
my_linked_list.append(1)


# (2) Items - Returns 2 Node
print(my_linked_list.pop_first())
# (1) Item -  Returns 1 Node
print(my_linked_list.pop_first())
# (0) Items - Returns None
print(my_linked_list.pop_first())

###############
#
# GET SECTION
#
###############
my_linked_list = LinkedList(0)
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)

print(my_linked_list.get(2))

###############
#
# SET_VALUE SECTION
#
###############
my_linked_list = LinkedList(11)
my_linked_list.append(3)
my_linked_list.append(23)
my_linked_list.append(7)
#set value of index1 to 4
my_linked_list.set_value(1,4)

my_linked_list.print_list()


###############
#
# INSERT SECTION
#
###############
my_linked_list = LinkedList(0)
my_linked_list.append(2)

my_linked_list.insert(1,1)

my_linked_list.print_list()

###############
#
# REMOVE SECTION
#
###############
my_linked_list = LinkedList(11)
my_linked_list.append(3)
my_linked_list.append(23)
my_linked_list.append(7)

print(my_linked_list.remove(2), '\n')

my_linked_list.print_list()

###############
#
# REVERSE SECTION
#
###############
my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)

my_linked_list.reverse()

my_linked_list.print_list()
