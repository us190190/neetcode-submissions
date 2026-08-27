class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}

        n = len(cost)
        def get_min_cost(level, start):
            if level >= n:
                return 0
 
            if (level, start) not in memo:
                memo[(level, start)] = cost[level] + min(get_min_cost(level + 1, start), get_min_cost(level + 2, start))
            return memo[(level, start)]
 
 
        return min(get_min_cost(0, 0), get_min_cost(1, 1))

        