
class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        """Insert a new value and bubble it up"""
        self.heap.append(val)
        self.bubble_up(len(self.heap) -1)
        