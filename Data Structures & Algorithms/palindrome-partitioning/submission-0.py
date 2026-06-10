class Solution:
    def partition(self, s: str) -> List[List[str]]:

        result, part = [], []

        def is_pali(chrs, st, end):
            while st<end:
                if chrs[st]!=chrs[end]:
                    return False
                st, end = (st+1), (end-1)
            return True


        def dfs(i):
            if i==len(s):
                result.append(part.copy())
                return
            
            for j in range(i, len(s)):
                if is_pali(s, i, j):
                    part.append(s[i:j+1])
                    dfs(j+1)
                    part.pop()
        
        dfs(0)
        return result
        