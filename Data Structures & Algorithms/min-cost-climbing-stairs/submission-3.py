class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        total_cost = {}
        n = len(cost)
        def dfs(i):
            if i>=n:
                return 0
            
            if i not in total_cost:
                total_cost[i] = cost[i] + min(dfs(i+1), dfs(i+2))
            
            return total_cost[i]
        return min(dfs(0), dfs(1))

            

        