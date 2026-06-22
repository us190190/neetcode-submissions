class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        s = sum(nums) 
        if s%2:
            return False
        
        target, identified = s>>1, set([0])
        for i in range(len(nums)-1, -1, -1):
            num = nums[i]
            prev_sum = identified.copy()
            for prev in prev_sum:
                n_sum = prev+num
                if n_sum>target:
                    continue
                if n_sum==target:
                    return True
                identified.add(n_sum)

        return False