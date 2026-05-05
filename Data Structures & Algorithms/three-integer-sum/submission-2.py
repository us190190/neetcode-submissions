class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        results = []

        for i in range(len(nums)-2):
            if nums[i]>0:
                break
            if i>0 and nums[i]==nums[i-1]:
                continue
            j, k = i+1, len(nums)-1
            while j<k:
                c_sum = nums[i] + nums[j] + nums[k]
                if c_sum == 0:
                    results.append((nums[i], nums[j], nums[k]))
                    j+=1
                    k-=1
                    while nums[j]==nums[j-1] and j<k:
                        j+=1
                elif c_sum > 0:
                    k -= 1
                elif c_sum < 0:
                    j += 1
        return results

        