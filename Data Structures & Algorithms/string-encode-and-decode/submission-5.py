class Solution:

    def encode(self, strs: List[str]) -> str:

        enc_str = ""

        for s in strs:
            enc_str += str(len(s)) + "#" + s
        
        return enc_str


    def decode(self, s: str) -> List[str]:

        # "5#Hello5#World"

        i, len_s, res, curr_len = 0, len(s), [], ""

        while i < len_s:

            if s[i] == "#":
                # slice str and append to array
                a_str = s[i+1:i+1+int(curr_len)]
                res.append(a_str)
                i += int(curr_len)
                curr_len = ""
            else:
                curr_len += s[i]
            i += 1
        
        return res
