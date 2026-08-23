class Node:
    def __init__(self, key: int, val: int):
        self.val = val
        self.key = key
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.store: Dict[int, Node] = {}
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left

    def _remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
    
    def _insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next, nxt.prev = node, node
        node.prev, node.next = prev, nxt

    def get(self, key: int) -> int:
        if key not in self.store:
            return -1
        
        node = self.store[key]
        self._remove(node)
        self._insert(node)
        return node.val

    def put(self, key: int, value: int) -> None:

        if key in self.store:
            node = self.store[key]
            self._remove(node)
        
        node = Node(key, value)
        self._insert(node)
        self.store[key] = node
        if len(self.store)>self.capacity:
            left_node = self.left.next
            del self.store[left_node.key]
            self._remove(left_node)
        
