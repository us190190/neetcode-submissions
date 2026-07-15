class Solution:
    def partition(self, s: str) -> List[List[str]]:

        self.result = []

        def is_pali(i,j):
            while i<j:
                if s[i]!=s[j]:
                    return False
                i += 1
                j -= 1
            return True

        def dfs(i, subset_version):
            if i==len(s):
                self.result.append(subset_version.copy())
                return
            
            for j in range(i,len(s)):
                if is_pali(i,j):
                    subset_version.append(s[i:j+1])
                    dfs(j+1, subset_version)
                    subset_version.pop()
        dfs(0, [])

        return self.result
                


        