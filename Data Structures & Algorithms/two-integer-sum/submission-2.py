class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        compliments = {}

        for index in range(len(nums)):
            current_compliment = target - nums[index]
            if current_compliment in compliments:
                return [compliments[current_compliment], index]
            else:
                compliments[nums[index]] = index

        