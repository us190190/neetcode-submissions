class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        self.result = []
        self.n = n

        def dfs(o, c, perm):
            if c==self.n:
                self.result.append(perm)
                return
            if o<self.n:
                dfs(o+1, c, perm+"(")
            if c<o:
                dfs(o, c+1, perm+")")
        
        dfs(0,0,"")
        return list(self.result)
        