class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        fast, slow = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if fast == slow:
                slow = 0
                while slow!=fast:
                    slow = nums[slow]
                    fast = nums[fast]
                return slow

        