class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        REF = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

        result, path = [], []

        def dfs(i):
            if i==len(digits):
                if len(path):
                    result.append("".join(path.copy()))
                return
            
            for ch in REF[int(digits[i])]:
                path.append(ch)
                dfs(i+1)
                path.pop()
            
        dfs(0)
        return result
        