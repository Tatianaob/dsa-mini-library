# Stack LIFO: last in - first out
# Core operations: push(x) pop(x) peek(x) is_empty() size()

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
class Stack:
    def __init__(self):
        self.top = None   # Points to the top node
        self._size = 0    # Tracks numbers of elements

    def push_node(self,value):
        """Insert value on top of the stack"""
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self._size += 1

    def pop(self):
        """Remove and return the top value"""
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        value = self.top.value
        self.top = self.top.next
        self._size -= 1
        return value
    
    def peek(self):     
        """Return the top value without removing it"""
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.top.value

    def is_empty(self):
        return self.top is None
    
    def size(self):
        return self._size

