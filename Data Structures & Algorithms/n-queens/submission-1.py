class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        result = []
        cols, posd, negd = set(), set(), set()

        def dfs(r, config):
            if r==n:
                result.append(config.copy())
                return
            
            for c in range(n):
                if c not in cols and (c-r) not in posd and (r+c) not in negd:
                    row = ["."]*n
                    row[c] = "Q"
                    cols.add(c)
                    posd.add(c-r)
                    negd.add(r+c)
                    config.append("".join(row))
                    dfs(r+1, config)
                    config.pop()
                    cols.remove(c)
                    posd.remove(c-r)
                    negd.remove(r+c)
        
        dfs(0, [])
        return result


        