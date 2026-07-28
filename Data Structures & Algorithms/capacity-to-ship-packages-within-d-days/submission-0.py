class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)

        while l<r:
            max_capacity = l + ((r-l)//2)
            days_taken, s_w = 1, 0
            for weight in weights:
                s_w += weight
                if s_w>max_capacity:
                    days_taken += 1
                    s_w = weight
            if days_taken<=days:
                r = max_capacity
            else:
                l = max_capacity+1
        
        return r






        
        