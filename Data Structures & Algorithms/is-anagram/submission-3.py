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
            if not ref[ch]:
                del ref[ch]

        return not len(ref) 
        