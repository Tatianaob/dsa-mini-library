
class Node:
    def __init__(self, value):
        self.value = value
        self.next =  None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self._size = 0
        