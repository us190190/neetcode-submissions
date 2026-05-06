class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        ref = {}

        for ch in s:
            if ch not in ref:
                ref[ch] = 0
            ref[ch] += 1
        
        for ch in t:
            if ch not in ref:
                return False
            ref[ch] -= 1
        
        for key, val in ref.items():
            if val:
                return False
        
        return True

        