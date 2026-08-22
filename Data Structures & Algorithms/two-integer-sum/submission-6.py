class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        visited = {}

        for idx, num in enumerate(nums):
            compliment = target-num
            if compliment in visited:
                return [visited[compliment], idx]
            visited[num] = idx
        
        


        