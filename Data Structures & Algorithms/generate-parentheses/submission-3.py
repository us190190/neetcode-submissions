class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        self.result = []

        def dfs(o: int, c: int, version: str):
            if o == n and c == n:
                self.result.append(version)
                return
            if o>n:
                return

            dfs(o+1, c, version + "(")
            if o>c:
                dfs(o, c+1, version + ")")
                
        dfs(0, 0, "")

        return self.result

        