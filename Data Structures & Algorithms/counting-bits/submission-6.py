class Solution:
    def countBits(self, n: int) -> List[int]:


        counts = []
        for i in range(n+1):
            count = 0
            num = i
            for _ in range(32):
                count += (num&1)
                num >>= 1
            counts.append(count)
        
        return counts
        