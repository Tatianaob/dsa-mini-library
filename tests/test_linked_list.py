from data_structures.singly_linked_list import SinglyLinkedList

# def test_insert_at_end():
#     ll = SinglyLinkedList()
#     ll.insert_at_end(1)
#     ll.insert_at_end(2)
#     ll.insert_at_end(3)

#     assert ll.head.value == 1
#     assert ll.head.next.value == 2
#     assert ll.head.next.next.value == 3
    

def test_insert_and_search():
    ll = SinglyLinkedList()
    ll.insert_at_end(10)
    ll.insert_at_beginning(33)
    assert ll.search(10)
    assert ll.search(33)
    assert not ll.search(99)

def test_delete_node():
    ll = SinglyLinkedList()
    ll.insert_at_end(2)
    ll.insert_at_end(4)
    ll.insert_at_end(6)
    ll.delete_node(2)
    assert ll.to_list() == [4, 6]

def test_to_list():
    ll = SinglyLinkedList()
    ll.insert_at_end(25)
    ll.insert_at_end(47)
    ll.insert_at_beginning(200)
    assert ll.to_list() == [200, 25, 47]