"""
Queues in Python

Its common for stacks and queues to be implemented with an array or linked list.

Stacks follow FIFO

To implement a stack, you need 2 operations:
	push - adds an element to the top of the stack
	pop - removes the element at the top of the stack

Queue follows FIFO

To implement a queue, you need 2 operations:
	enqueue - adds an element to the end of the queue
	dequeue - removes the element at the beginning of the queue

Python's built-in list data structure comes with methods to simulate both stack and queue operations

Considering a stack of letters:
"""
letters = []

# Let's push some letters into our list
letters.append('c')
letters.append('a')
letters.append('t')
letters.append('g')

# Now let's pop letters, we should get 'g'
last_item = letters.pop()
print(last_item)

# If we pop again we'll get 't'
last_item = letters.pop()
print(last_item)

# 'c' and 'a' remain
print(letters) #

"""
Why use a queue?

Now imagine that you're a developer working on a new fighting game. In your game, every time a button is pressed, an input event is fired. A tester noticed that if buttons are pressed too quickly the game only processes the first one and special moves won't work!

You can fix that with a queue. We can enqueue all input events as they come in. This way it doesn't matter if input events come with little time between them, they'll all be stored and available for processing. When we're processing the moves we can dequeue them. A special move can be worked out like this
"""
input_queue = Queue()

# The player wants to get the upper hand so pressing the right combination of buttons quickly
input_queue.enqueue('DOWN')
input_queue.enqueue('RIGHT')
input_queue.enqueue('B')

# Now we can process each item in the queue by dequeueing them
key_pressed = input_queue.dequeue() # 'DOWN'

# We'll probably change our player position
key_pressed = input_queue.dequeue() # 'RIGHT'

# We'll change the player's position again and keep track of a potential special move to perform
key_pressed = input_queue.dequeue() # 'B'

# This can do the act, but the game's logic will know to do the special move
