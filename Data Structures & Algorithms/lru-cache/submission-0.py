
class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.caches = {}
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left
    
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
    
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next, nxt.prev = node, node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.caches:
            node = self.caches[key]
            self.remove(node)
            self.insert(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.caches:
            self.remove(self.caches[key])
        node = Node(key,value)
        self.insert(node)
        self.caches[key] = node

        if len(self.caches)>self.capacity:
            lru = self.left.next
            del self.caches[lru.key]
            self.remove(lru)
        
