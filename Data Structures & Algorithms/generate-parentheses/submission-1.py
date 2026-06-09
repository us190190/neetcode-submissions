class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        result, substr = [], []

        def dfs(o, c):
            if o == c and o == n:
                result.append("".join(substr))
                return
            
            if o < n:
                substr.append("(")
                dfs(o+1, c)
                substr.pop()
            if o > c:
                substr.append(")")
                dfs(o, c+1)
                substr.pop()
        
        dfs(0, 0)

        return result
        