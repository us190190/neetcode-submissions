class Trie:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class WordDictionary:

    def __init__(self):
        self.root = Trie()

    def addWord(self, word: str) -> None:
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = Trie()
            cur = cur.children[ch]
        cur.end_of_word = True

    def search(self, word: str) -> bool:

        q = deque([self.root])

        for ch in word:
            next_q = deque()
            while q:
                cur = q.popleft()
                if ch == ".":
                    for child in cur.children.values():
                        next_q.append(child)
                elif ch in cur.children:
                    next_q.append(cur.children[ch])
            q = next_q
            if not q:
                return False
        
        return any(node.end_of_word for node in q)
