class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        # 1,2,3,_
        # _,_,_,2

        total_cost = [{}, {}]
        n = len(cost)
        def dfs(i, start):
            if i>=n:
                return 0
            
            if i not in total_cost[start]:
                total_cost[start][i] = cost[i] + min(dfs(i+1, start), dfs(i+2, start))
            
            return total_cost[start][i]
        return min(dfs(0,0), dfs(1,1))

            

        