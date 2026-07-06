class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        ref = {}
        result = 0

        l, r = 0, 0

        while r<len(s):
            ch = s[r]
            if ch in ref and ref[ch]!=-1:
                # compress till ref[ch]
                till = ref[ch]
                l = till+1
                for key, idx in ref.items():
                    if idx<till:
                        ref[key]=-1
            length = r-l+1
            result = max(result, length)
            ref[ch] = r
            r += 1
        
        return result

        