from data_structures.bst import BinarySearchTree

def test_bst_insert_and_search():
    bst = BinarySearchTree()
    values = [50,30,70,20,40,60,80]
    for v in values:
        bst.insert(v)
    
    assert bst.search(50)
    assert bst.search(20)
    assert not bst.search(999)

def test_bst_inorder():
    bst = BinarySearchTree()
    values = [10,5,20,3,7,15]
    for v in values:
        bst.insert(v)
    assert bst.inorder() == [3,5,7,10,15,20]