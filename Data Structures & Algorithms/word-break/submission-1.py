class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
    
    def add_word(self, word):
        cur = self

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.is_end = True
    
    def search(self, s, i, j):
        cur = self

        for idx in range(i, j+1):
            ch = s[idx]
            if ch not in cur.children:
                return False
            cur = cur.children[ch]
        return cur.is_end

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        head = TrieNode()
        dp = [False]*len(s)
        dp.append(True)
        max_word_len = 0

        for word in wordDict:
            head.add_word(word)
            max_word_len = max(max_word_len, len(word))

        for i in range(len(s)-1, -1 ,-1):
            end = min(len(s), i+max_word_len)
            for j in range(i, end):
                if head.search(s, i, j):
                    dp[i] = dp[j+1]
                    if dp[i]:
                        break

        return dp[0]
        
        




        