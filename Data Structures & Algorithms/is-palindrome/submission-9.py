class Solution:
    def isPalindrome(self, s: str) -> bool:

        length = len(s)
        if length<2:
            return True
        s = s.lower()
        l, r = 0, length-1

        print(s)

        while l<r:
            if not (ord('a')<=ord(s[l])<=ord('z') or ord('0')<=ord(s[l])<=ord('9')):
                l += 1
                continue
            if not (ord('a')<=ord(s[r])<=ord('z') or ord('0')<=ord(s[r])<=ord('9')):
                r -= 1
                continue
            if ord(s[l])==ord(s[r]):
                l += 1
                r -= 1
            else:
                return False
        
        return True
        