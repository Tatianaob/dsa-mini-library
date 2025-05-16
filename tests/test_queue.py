from data_structures.queue import Queue

def test_queue_methods():
    q = Queue()
    assert q.is_empty()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)

    assert q.size() == 3
    assert q.peek() == 10
    assert q.dequeue() == 10
    assert q.peek() == 20
    assert q.dequeue() == 20
    assert q.dequeue() == 30
    assert q.is_empty()
    