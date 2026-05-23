class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        ref = {}

        for i in range(len(numbers)):
            if target-numbers[i] in ref:
                return [ref[target-numbers[i]], i+1]
            ref[numbers[i]] = i+1
        

        