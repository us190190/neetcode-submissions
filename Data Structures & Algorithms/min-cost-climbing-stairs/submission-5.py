class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}

        n = len(cost)
        def get_min_cost(level):
            if level >= n:
                return 0
 
            if level not in memo:
                memo[level] = cost[level] + min(get_min_cost(level + 1), get_min_cost(level + 2))
            return memo[level]
 
 
        return min(get_min_cost(0), get_min_cost(1))

        