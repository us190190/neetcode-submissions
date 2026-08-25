class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        self.result = []
        self.occupied_cols = set()
        self.occupied_d1 = set()
        self.occupied_d2 = set()

        def dfs(r: int, solution: List[str]):
            if r == n:
                self.result.append(solution.copy())
                return
            
            for c in range(n):
                if not (c in self.occupied_cols or (r-c) in self.occupied_d1
                    or (r+c) in self.occupied_d2):
                    row = ["."]*n
                    row[c] = "Q"
                    self.occupied_cols.add(c)
                    self.occupied_d1.add(r-c)
                    self.occupied_d2.add(r+c)
                    dfs(r+1, solution + ["".join(row)])
                    self.occupied_cols.remove(c)
                    self.occupied_d1.remove(r-c)
                    self.occupied_d2.remove(r+c)

        dfs(0,[])
        
        return self.result
            




        