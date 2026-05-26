class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l, r, max_len, ref = 0, 0, 0, defaultdict(int)

        def max_freq_in_window():
            max_f = 0

            for v, f in ref.items():
                max_f = max(max_f, f)

            return max_f

        # XYYX
        # l r

        while r<len(s):
            ch = s[r]
            ref[ch] += 1
            w_len = r-l+1
            w_max_f = max_freq_in_window()
            while l<len(s) and (w_len - w_max_f)>k:
                # print(f"compressing window:: w_len:{w_len} w_max_f:{w_max_f}, k:{k}")
                ref[s[l]] -= 1
                l += 1
                w_len = r-l+1
                w_max_f = max_freq_in_window()
            # print(f"l:{l}, r:{r}, w_len:{w_len}, max_len:{max_len}")
            max_len = max(max_len, w_len)
            r += 1
        
        return max_len


        