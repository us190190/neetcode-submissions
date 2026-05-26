class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        len_s1, len_s2 = len(s1), len(s2)

        if len_s2<len_s1:
            return False
        
        s1_ref, s2_ref = { ch: 0 for ch in range(ord('a'), ord('z')+1)}, { ch: 0 for ch in range(ord('a'), ord('z')+1)}

        for ch in s1:
            s1_ref[ord(ch)] += 1
        
        l, r = 0, 0

        while r<len_s2:
            ch = s2[r]
            s2_ref[ord(ch)] += 1
            w_len = r-l+1
            if w_len>len_s1:
                # print(f"commpressing window:: l:{l}, r:{r}, w_len:{w_len}")
                s2_ref[ord(s2[l])] -= 1
                l += 1
                w_len = r-l+1
            # print(f"w_len:{w_len}, len_s1:{len_s1}, s2_ref:{s2_ref}, s1_ref:{s1_ref}")
            if w_len == len_s1 and s2_ref == s1_ref:
                return True
            r += 1
        
        return False


        