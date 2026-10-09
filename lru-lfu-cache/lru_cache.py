"""LRU cache: a hash table pointing to the nodes of a doubly linked list.

The dict finds a node in O(1). The list keeps the nodes ordered from most
recently used (front) to least recently used (back), so moving a node to the
front and removing the back node both take O(1).
"""


class Node:
    __slots__ = ("key", "value", "prev", "next")

    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, max_size):
        self.max_size = max_size
        self.table = {}  # key -> Node
        # Two sentinel nodes avoid special cases for an empty list
        self.head = Node()  # most recently used side
        self.tail = Node()  # least recently used side
        self.head.next = self.tail
        self.tail.prev = self.head

    def size(self):
        return len(self.table)

    def get(self, key):
        node = self.table.get(key)
        if node is None:
            return None
        self._move_to_front(node)
        return node.value

    def set(self, key, value):
        node = self.table.get(key)
        if node is not None:
            node.value = value
            self._move_to_front(node)
            return
        if len(self.table) >= self.max_size:
            self._evict()
        node = Node(key, value)
        self.table[key] = node
        self._add_to_front(node)

    def _evict(self):
        node = self.tail.prev  # the least recently used entry
        self._unlink(node)
        del self.table[node.key]

    def _move_to_front(self, node):
        self._unlink(node)
        self._add_to_front(node)

    def _add_to_front(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _unlink(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev


if __name__ == "__main__":
    cache = LRUCache(2)
    cache.set("A", 1)
    cache.set("B", 2)
    cache.get("A")  # A becomes the most recently used
    cache.set("C", 3)  # cache is full: B is evicted
    print(cache.get("B"))  # None
    print(cache.get("A"))  # 1
    print(cache.size())  # 2
