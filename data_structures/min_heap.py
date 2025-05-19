# a heap is a special kind of binary tree that satisfiest the heap property:
# Min heap: parent <- children : Dijkstra's alogrith, priority queue
# Max heap: parent >- chuldren: Top-K elements, sorting


class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        """Insert a new value and bubble it up"""
        self.heap.append(val)
        self.bubble_up(len(self.heap) -1)

    def bubble_up(self, index):
        """Move the value at index up to maintain heap property"""
        parent_index = (index - 1) // 2
        while index > 0 and self.heap[index] < self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            index = parent_index
            parent_index = (index - 1) // 2

    def extract_min(self):
        """Remove and return the smallest value (root)."""
        if not self.heap:
            raise IndexError("Heap is empty")
        min_val = self.heap[0]
        last_val = self.heap.pop()
        if self.heap:
            self.heap[0] = last_val
            self._heapify(0)
        return min_val
