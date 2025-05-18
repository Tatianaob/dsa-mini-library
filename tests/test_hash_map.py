from data_structures.hash_map import HashMap

def test_hash_map_operations():
    h = HashMap()

    h.put("name", "Alice")
    h.put("age", 30)
    assert h.get("name") == "Alice"
    assert h.get("age") == 30

    h.put("age", 31)
    assert h.get("age") == 31

    assert h.contains("name")
    assert not h.contains("email")

    h.remove("name")
    assert not h.contains("name")

def test_hash_map_keys():
    h = HashMap()
    h.put("a", 1)
    h.put("b", 2)
    h.put("c", 3)

    keys = h.keys()
    assert set(keys) == {"a", "b", "c"}