
class Node:
    def __init__(self, value):
        self.value = value
        self.next =  None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self._size = 0
    
    def enqueue(self, value):
        """Add item to the rear of the queue"""
        new_node = Node(value)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self._size += 1

    def dequeue(self):
        """remove and return item from the front"""
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        value = self.front.value
        self.front = self.front.next
        if not self.front:
            self.rear = None
        self._size -= 1
        return value
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty queue")
        return self.front.value
    
    def is_empty(self):
        return self.front is None
    
    def size(self):
        return self._size
