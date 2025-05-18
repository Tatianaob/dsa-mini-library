
class HashMap:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]  #list of buckets
    
    def _hash(self, key):
        """Hash the key into a bucket index"""
        return hash(key) % self.size

    def put(self, key, value):
        """Insert or put the key value pair"""
        index = self._hash(key)
        bucket = self.table(index)

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i]  = (key, value)  #update
                return
        bucket.append((key, value))  #insert

        
