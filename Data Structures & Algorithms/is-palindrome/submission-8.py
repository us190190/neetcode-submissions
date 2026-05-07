class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.lower()
        left, right = 0, len(s)-1

        while left<right:
            while left<right and not ord('a')<=ord(s[left])<=ord('z') and not ord('0')<=ord(s[left])<=ord('9'):
                left += 1
            while left<right and not ord('a')<=ord(s[right])<=ord('z') and not ord('0')<=ord(s[right])<=ord('9'):
                right -= 1
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        
        return True
        