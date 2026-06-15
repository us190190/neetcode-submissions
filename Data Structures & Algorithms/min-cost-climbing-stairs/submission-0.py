class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        # cost:     [1,2,1,2,1,1,1]
        # cum_cost: [0,0,0,0,0,0,0]

        memo = [-1]*len(cost)
        
        def dfs(i):
            if i>=len(cost):
                return 0
            if memo[i]!=-1:
                return memo[i]
            memo[i] = cost[i] + min(dfs(i+1), dfs(i+2))
            return memo[i]
        
        return min(dfs(0), dfs(1))
            



        