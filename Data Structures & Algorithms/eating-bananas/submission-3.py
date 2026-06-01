class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l, r = 1, 1

        for p in piles:
            r = max(r,p)
        
        while l<r:
            mid = l + ((r-l)//2)
            t = 0
            for p in piles:
                t += (p//mid) + (1 if (p%mid) else 0)

            if t<=h:
                r = mid
            else:
                l = mid + 1

        return r          



        