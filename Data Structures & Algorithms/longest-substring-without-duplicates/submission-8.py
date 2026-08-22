class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l, r = 0, 0
        length = len(s)
        window = {}
        result = 0

        while r<length:
            ch = s[r]
            if ch in window:
                # compress window
                compress_till_idx = window[ch]

                while l <= compress_till_idx:
                    ch_at_l = s[l]
                    del window[ch_at_l]
                    l += 1
            # expand window
            window[ch] = r
            result = max(result, len(window))
            r += 1
        
        return result
                
        