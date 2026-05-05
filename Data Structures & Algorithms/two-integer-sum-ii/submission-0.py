class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        indexes = {}

        for index, num in enumerate(numbers):
            if target - num in indexes:
                return [indexes[target-num], index+1]
            else:
                indexes[num] = index+1

        