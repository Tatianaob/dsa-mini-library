from data_structures.singly_linked_list import SinglyLinkedList

def test_insert_at_end():
    ll = SinglyLinkedList()
    ll.insert_at_end(1)
    ll.insert_at_end(2)
    ll.insert_at_end(3)

    assert ll.head.value == 1
    assert ll.head.next.value == 2
    assert ll.head.next.next.value == 3
    