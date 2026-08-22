class Solution:
    def isPalindrome(self, s: str) -> bool:

        left, right = 0, (len(s)-1)

        while left<right:
            left_ch = s[left]
            right_ch = s[right]
            if ord('A') <= ord(left_ch) <= ord('Z'):
                left_ch = left_ch.lower()
            if not ( ord('a')<=ord(left_ch)<=ord('z') or ord('0')<=ord(left_ch)<=ord('9')):
                left += 1
                continue
            if ord('A') <= ord(right_ch) <= ord('Z'):
                right_ch = right_ch.lower()
            if not ( ord('a')<=ord(right_ch)<=ord('z') or ord('0')<=ord(right_ch)<=ord('9')):
                right -= 1
                continue
            if left_ch != right_ch:
                return False
            left += 1
            right -= 1
        
        return True


        