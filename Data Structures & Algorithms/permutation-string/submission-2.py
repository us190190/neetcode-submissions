class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1)==len(s2)==0:
            return True
        
        s1_ref = {ch: 0 for ch in range(ord('a'), ord('z')+1)}
        s2_ref = {ch: 0 for ch in range(ord('a'), ord('z')+1)}

        for ch in s1:
            s1_ref[ord(ch)] += 1
        
        l, r = 0, 0

        while r<len(s2):
            s2_ref[ord(s2[r])] += 1
            length = r-l+1
            if length==len(s1):
                # compress
                if s2_ref == s1_ref:
                    return True
                s2_ref[ord(s2[l])] -= 1
                l += 1
            r += 1
        
        return False



        