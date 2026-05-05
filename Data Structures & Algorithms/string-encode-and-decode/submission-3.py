class Solution:

    def encode(self, strs: List[str]) -> str:

        enc_str = ""

        for s in strs:
            enc_str += str(len(s)) + "#" + s
        
        print(enc_str)
        
        return enc_str

    def decode(self, s: str) -> List[str]:

        result = []

        # "2#ab3#abc"

        i =0

        while i < len(s):
            str_len = ""
            for j in range(i, len(s)):
                if s[j] == "#":
                    slice_length = int(str_len)
                    start_i = j+1
                    end_i = start_i+slice_length
                    result.append(s[start_i:end_i])
                    
                    i = j + slice_length
                    str_len = ""
                    break
                str_len += s[j]
            i+=1
        
        return result
