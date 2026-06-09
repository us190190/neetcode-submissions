class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
    
    def add_word(self, word):
        cur = self
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
        cur.is_end = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        root = TrieNode()
        result, visited = set(), set()
        DIRECTIONS = [[1,0], [0,1], [-1,0], [0,-1]]
        ROWS, COLS = len(board), len(board[0])

        for word in words:
            root.add_word(word)
        
        def dfs(r, c, node, word):
            if r<0 or r>=ROWS or c<0 or c>=COLS or (r,c) in visited or board[r][c] not in node.children:
                return
            cur_ch = board[r][c]
            cur_word = word + cur_ch
            visited.add((r,c))
            node = node.children[cur_ch]
            if node.is_end:
                result.add(cur_word)
            
            for dr,dc in DIRECTIONS:
                dr += r
                dc += c
                dfs(dr, dc, node, cur_word)
            
            visited.remove((r, c))
        
        for row in range(ROWS):
            for col in range(COLS):
                dfs(row, col, root, "")

        return list(result)
        