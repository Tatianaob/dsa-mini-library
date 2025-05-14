
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None # head = first node of list - list empty at the beggining

    def insert_at_end(self, value):  # method adds new node at the end of the list
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        