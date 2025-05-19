from data_structures.min_heap import MinHeap

def test_min_heap_operations():
    h = MinHeap()
    h.insert(10)
    h.insert(4)
    h.insert(15)
    h.insert(1)

    assert h.peek() == 1
    assert h.extract_min() == 1
    assert h.extract_min() == 4
    assert h.size() == 2
    assert h.extract_min() == 10
    assert h.extract_min() == 15
