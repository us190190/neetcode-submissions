class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left, right = 0, len(nums)-1

        while left<=right:
            # (l + r) // 2 can lead to overflow
            # m = l + ((r - l) // 2)
            mid = (left+right)//2

            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1

        