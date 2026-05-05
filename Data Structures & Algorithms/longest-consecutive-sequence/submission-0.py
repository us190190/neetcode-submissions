class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        length = len(nums)
        if length < 2:
            return length
        nums.sort()
        print(nums)

        max_len, cur_len, i = 0, 1, 0

        while i<length-1:
            i += 1
            if nums[i] == nums[i-1]+1:
                cur_len += 1
            elif nums[i] == nums[i-1]:
                continue
            else:
                max_len = max(max_len, cur_len)
                print("c:"+str(cur_len)+"m:"+str(max_len))
                cur_len = 1
        
        return max(max_len, cur_len)
