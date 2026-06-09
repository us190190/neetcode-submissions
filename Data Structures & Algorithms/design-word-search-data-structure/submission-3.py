class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end = True

    def search(self, word: str) -> bool:
        q = deque([self.root])

        for ch in word:
            next_q = deque()
            while q:
                node = q.popleft()
                if ch == '.':
                    for child in node.children:
                        next_q.append(node.children[child])
                else:
                    if ch in node.children:
                        next_q.append(node.children[ch])
            q = next_q
            if not q:
                return False
        
        return any(node.end for node in q)


