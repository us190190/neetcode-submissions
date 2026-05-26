class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        ref, l, r, max_len = {}, 0, 0, 0

        while r<len(s):
            ch = s[r]
            if ch in ref and ref[ch]!=-1:
                l = ref[ch]+1
                for k, f in ref.items():
                    if f<l:
                        ref[k]=-1
            ref[ch] = r
            max_len = max(max_len, r-l+1)
            r += 1
        
        return max_len
        