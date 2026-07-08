class Solution:
    def minWindow(self, s: str, t: str) -> str:

        need, have = defaultdict(int), defaultdict(int)

        for ch in t:
            need[ch] += 1
        
        l, r = 0, 0
        result = ''
        min_length = float('inf')
        needs, haves = len(need), 0

        while r<len(s):
            ch = s[r]
            if ch in need:
                have[ch] += 1
                if have[ch] == need[ch]:
                    haves += 1
                # print(f"need: {need}, have: {have}")
                while haves==needs and l<=r:
                    length = r-l+1
                    #print(s[l:r+1])
                    if length<=min_length:
                        min_length = min(min_length, length)
                        result = s[l:r+1]

                    if s[l] in have:
                        have[s[l]] -= 1
                        if have[s[l]]<need[s[l]]:
                            haves -= 1
                        if have[s[l]]==0:
                            del have[s[l]]
                    l += 1

            r += 1
        
        return result
