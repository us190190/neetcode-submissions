class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l, r = 1, 1

        for num in piles:
            r = max(r, num)

        while l<r:
            mid = l + ((r-l)//2)

            # check can eat all bananas in less than or equal to h time
            total_time = 0
            for num in piles:
                total_time += num//mid + (1 if num%mid else 0)

            # print(f"total_time:{total_time}, l:{l}, r:{r}, mid:{mid}")
            
            if total_time<=h:
                r = mid
            else:
                l = mid+1
        
        return r
            

        