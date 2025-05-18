# Goal: build a dict-like structure from scratch usng chaining for collisiion handling.


class HashMap:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]  # initializes a list of buckets
    # each bucket is a list - this lets us store multiple k,v pairs if multiple keys hash to the same bucket
    # table starts with 10 buckets by default

    def _hash(self, key):
        """Hash the key into a bucket index"""
        return hash(key) % self.size
    # takes any key and converts it into an index (from 0 to size - 1)

    def put(self, key, value):  #
        """Insert or put the key value pair"""
        index = self._hash(key)
        bucket = self.table(index)

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i]  = (key, value)  #update
                return
        bucket.append((key, value))  #insert
    
    def get(self, key):     # retrieve the value by key
        index = self._hash(key)
        bucket = self.table[index]

        for (k, v) in bucket:
            if k == key:
                return v
        raise KeyError(f"Key '{key}' not found")
    
    def remove(self, key): #remove the k,v pair
        index = self._hash(key)
        bucket = self.table[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return
        raise KeyError(f"Key '{key}' not found")
    
    def contains(self, key):  #check if the k exists
        index = self._hash(key)
        return any(k == key for k, _ in self.table[index])

    def keys(self):
        """Return all keys."""
        return [k for bucket in self.table for (k, _) in bucket]

