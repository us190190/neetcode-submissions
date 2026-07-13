class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = piles[0]

        for pile in piles:
            r = max(r, pile)

        while l<r:

            k = l + ((r-l)//2)

            time  = 0
            for pile in piles:
                time += (pile//k) + (1 if pile%k else 0)
            
            if time<=h:
                r = k
            else:
                l = k + 1
        
        return r


        