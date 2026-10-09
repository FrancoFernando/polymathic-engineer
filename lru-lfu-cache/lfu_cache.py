"""LFU cache: a hash table plus a min-heap ordered by (counter, timestamp).

Python's heapq has no way to update the priority of an element in place, so
every hit pushes a fresh (counter, timestamp, key) tuple and leaves the old one
in the heap. Eviction pops until it finds a tuple that matches the live entry.
When the heap grows past twice the cache size, it is rebuilt from the table.
"""

import heapq
from itertools import count


class LFUCache:
    def __init__(self, max_size):
        self.max_size = max_size
        self.table = {}  # key -> [value, counter, timestamp]
        self.heap = []  # (counter, timestamp, key), may contain stale tuples
        self.clock = count()  # a tick per access plays the role of the timestamp

    def size(self):
        return len(self.table)

    def get(self, key):
        entry = self.table.get(key)
        if entry is None:
            return None
        self._touch(key, entry)
        return entry[0]

    def set(self, key, value):
        entry = self.table.get(key)
        if entry is not None:
            entry[0] = value
            self._touch(key, entry)
            return
        if len(self.table) >= self.max_size:
            self._evict()
        entry = [value, 1, next(self.clock)]
        self.table[key] = entry
        heapq.heappush(self.heap, (1, entry[2], key))

    def _touch(self, key, entry):
        entry[1] += 1
        entry[2] = next(self.clock)
        heapq.heappush(self.heap, (entry[1], entry[2], key))
        if len(self.heap) > 2 * self.max_size:
            self._rebuild()

    def _evict(self):
        while True:
            counter, timestamp, key = heapq.heappop(self.heap)
            entry = self.table.get(key)
            if entry is not None and entry[2] == timestamp:  # not stale
                del self.table[key]
                return

    def _rebuild(self):
        self.heap = [(e[1], e[2], k) for k, e in self.table.items()]
        heapq.heapify(self.heap)


if __name__ == "__main__":
    cache = LFUCache(2)
    cache.set("A", 1)
    cache.set("B", 2)
    cache.get("A")
    cache.get("A")  # A has counter 3, B has counter 1
    cache.set("C", 3)  # cache is full: B is evicted
    print(cache.get("B"))  # None
    cache.set("D", 4)  # A (3) vs C (1): C is evicted
    print(cache.get("C"))  # None
    print(cache.get("A"))  # 1
    print(cache.size())  # 2
