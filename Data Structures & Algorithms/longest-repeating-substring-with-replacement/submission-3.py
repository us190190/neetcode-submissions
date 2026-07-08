class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        freq = defaultdict(int)
        result = 0
        max_freq = 0
        l,r = 0, 0
        while r<len(s):
            length = r-l+1
            freq[s[r]] += 1
            for ch, f in freq.items():
                max_freq = max(max_freq, f)
            if (length-max_freq) <= k:
                #print(f"sub: {s[l:r+1]}, length: {length}, max_freq: {max_freq}")
                result = max(result, length)
                r += 1
            else:
                freq[s[l]] -= 1
                l += 1
                freq[s[r]] -= 1
        
        return result
        