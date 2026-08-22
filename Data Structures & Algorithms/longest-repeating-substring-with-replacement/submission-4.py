class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l, r = 0, 0
        length = len(s)
        window = defaultdict(int)
        result = 0

        while r<length:
            ch = s[r]
            window[ch] += 1
            max_freq = 0
            for f in window.values():
                max_freq = max(max_freq, f)
            
            if ((r-l+1)-max_freq) <= k:
                result = max(result, r-l+1)
                r += 1
            else:
                window[s[l]] -= 1
                l += 1
                window[s[r]] -= 1
        
        return result
            


