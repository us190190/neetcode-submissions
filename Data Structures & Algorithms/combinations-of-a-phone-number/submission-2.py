class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []
        
        KEYMAP = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

        self.result = []

        def dfs(i: int, pattern: str):
            if i==len(digits):
                self.result.append(pattern)
                return
            
            num = int(digits[i])
            for ch in KEYMAP[num]:
                dfs(i+1, pattern+ch)
        
        dfs(0, "")

        return self.result
        