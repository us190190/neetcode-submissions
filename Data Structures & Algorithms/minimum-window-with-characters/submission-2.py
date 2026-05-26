class Solution:
    def minWindow(self, s: str, t: str) -> str:

        need, have = 0, 0
        need_ref, have_ref = defaultdict(int), defaultdict(int)

        for ch in t:
            need_ref[ch] += 1
        
        need = len(need_ref)

        l, r, min_len, min_s = 0, 0, len(s), -1

        while r<len(s):
            ch = s[r]
            if ch in need_ref:
                have_ref[ch] += 1
                if have_ref[ch] == need_ref[ch]:
                    have += 1
            # print(f"expand:: have_ref:{have_ref}, need_ref:{need_ref}, have:{have}, need:{need}, l:{l}, r:{r}, str:{s[l:r+1]}")
            while have == need and l<=r:
                # print(f"compress:: have_ref:{have_ref}, need_ref:{need_ref}, have:{have}, need:{need}, l:{l}, r:{r}, str:{s[l:r+1]}")
                if (r-l+1)<=min_len:
                    min_s = l
                    min_len = (r-l+1)
                l_ch = s[l]
                if l_ch in need_ref:
                    have_ref[l_ch] -= 1
                    if have_ref[l_ch] < need_ref[l_ch]:
                        have -= 1
                l += 1

            r += 1
        
        return s[min_s:(min_s+min_len)] if min_len else ""

        