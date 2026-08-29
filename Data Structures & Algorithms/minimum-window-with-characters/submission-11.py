class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(s)<len(t):
            return ""
        
        if s == t:
            return s
        
        needs, haves = {}, {}

        for ch in t:
            if ch not in needs:
                needs[ch] = 0
            needs[ch] += 1
        
        need, have = len(needs), 0
        l, r = 0, 0
        result, result_length = "", len(s)

        while r<len(s):
            ch = s[r]
            if ch in needs:
                if ch not in haves:
                    haves[ch] = 0
                haves[ch] += 1
                if haves[ch] == needs[ch]:
                    have += 1
                while have >= need:
                    ch_l = s[l]
                    if ch_l in haves:
                        if r-l+1 <= result_length:
                            result_length = r-l+1
                            result = s[l:r+1]
                        haves[ch_l] -= 1
                        if haves[ch_l] < needs[ch_l]:
                            have -= 1
                    l += 1
            r += 1
        
        return result




        