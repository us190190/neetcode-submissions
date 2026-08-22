class Solution:

    def encode(self, strs: List[str]) -> str:
        enc_data = []
        for s in strs:
            enc_data.append(str(len(s)) + "#" + s)

        "5#Hello4#Test"
        return "".join(enc_data)


    def decode(self, s: str) -> List[str]:

        i = 0
        read_ahead_count = 0
        length = len(s)
        dec_str = []

        while i<length:
            if s[i] == "#":
                dec_str.append(s[i+1:i+read_ahead_count+1])
                i += read_ahead_count+1
                read_ahead_count = 0
            else:
                read_ahead_count = (read_ahead_count*10) + int(s[i])
                i += 1
        
        return dec_str


