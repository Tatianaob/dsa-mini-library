
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
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self): # helper to print the whole list
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")
