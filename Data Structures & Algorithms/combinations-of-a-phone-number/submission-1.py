class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        self.result = []
        REF = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

        def dfs(i, comb):
            if i==len(digits):
                if comb:
                    self.result.append(comb)
                return
            
            for ch in REF[int(digits[i])]:
                dfs(i+1, comb+ch)
        
        dfs(0,"")
        return self.result
            

        