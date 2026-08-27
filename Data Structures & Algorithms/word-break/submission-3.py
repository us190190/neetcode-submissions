class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        # s = "applepenapple", wordDict = ["apple","pen","ape"]

        # applepenapple

        words = set(wordDict)
        min_word = min([len(word) for word in words])
        max_word = max([len(word) for word in words])
        memo = {}

        def is_breakable(idx):
            if idx==-1:
                return True
            if idx<(min_word-1):
                return False
            if idx == min_word-1:
                return s[:idx+1] in words
            
            if idx not in memo:
                status = False
                for i in range(idx, idx-max_word-1, -1):
                    cur_word = s[i:idx+1]
                    if cur_word in words:
                        status = status or is_breakable(i-1)
                memo[idx] = status
            
            return memo[idx]

        return is_breakable(len(s)-1)

        