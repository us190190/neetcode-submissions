class Node:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.store = {}
        self.left = Node()
        self.right = Node()
        self.left.next, self.right.prev = self.right, self.left
        
    def _insert(self, node):
        # [L*].   [M].  [N]  [R*].
        prev, nxt = self.right.prev, self.right.next
        prev.next, self.right.prev = node, node
        node.next, node.prev = self.right, prev
    
    def _remove(self, node):
        # [P].  [C] [N].
        nxt, prev = node.next, node.prev
        del node
        prev.next, nxt.prev = nxt, prev

    def get(self, key: int) -> int:

        if key not in self.store:
            return -1
        
        node = self.store[key]
        new_node = Node(node.key, node.val)
        self._remove(node)
        self._insert(new_node)
        self.store[key] = new_node
        return new_node.val
        

    def put(self, key: int, value: int) -> None:

        if key in self.store:
            self._remove(self.store[key])
            del self.store[key]
        
        node = Node(key, value)
        self.store[key] = node
        self._insert(node)
        
        if len(self.store) > self.capacity:
            extra_node = self.left.next
            if extra_node:
                del self.store[extra_node.key]
                self._remove(extra_node)

        
