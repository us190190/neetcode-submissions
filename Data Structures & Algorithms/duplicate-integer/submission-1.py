class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        ref = set()

        for n in nums:
            if n in ref:
                return True
            ref.add(n)
        
        return False
        