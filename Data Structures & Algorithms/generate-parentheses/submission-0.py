class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        result = []

        def dfs(o, c, substr):
            if o == c and o == n:
                result.append(substr)
                return
            
            if o < n:
                dfs(o+1, c, substr + '(')
            if o > c:
                dfs(o, c+1, substr + ')')
        
        dfs(0, 0, "")

        return result
        