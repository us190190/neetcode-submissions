class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        ref = set()

        for num in nums:
            if num in ref:
                return True
            ref.add(num)
        
        return False
        