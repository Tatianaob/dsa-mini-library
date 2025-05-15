from data_structures.stack import Stack

def test_stack_methods():
    s = Stack()
    assert s.is_empty()
    s.push_node(10)
    s.push_node(20)
    assert s.size() == 2
    assert s.peek() == 20
    assert s.pop() == 20
    assert s.pop() == 10
    assert s.is_empty()
