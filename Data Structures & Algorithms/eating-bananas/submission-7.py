class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l, r = 1, max(piles)
        result = l

        while l<=r:
            rate = l + ((r-l)//2)
            time_taken = 0
            for pile in piles:
                time_taken += pile//rate
                time_taken += 1 if pile%rate else 0
            
            if time_taken <= h:
                result = rate
                r = rate - 1
            else:
                l = rate + 1
        
        return result





        