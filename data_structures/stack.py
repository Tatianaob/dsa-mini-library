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
