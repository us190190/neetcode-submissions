class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        ref = defaultdict(int)

        for ch in s:
            ref[ch] += 1
        
        for ch in t:
            if ch not in ref:
                return False
            ref[ch] -= 1
        
        for ch, freq in ref.items():
            if freq != 0:
                return False
        
        return True
        