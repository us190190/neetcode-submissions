class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            encoded_str += str(len(s)) + "#" + s
        return encoded_str

    def decode(self, s: str) -> List[str]:

        # "5#Hello5#World"
        idx, word_len, result = 0, 0, []

        while idx<len(s):
            ch = s[idx]
            if ord('0')<=ord(ch)<=ord('9'):
                word_len = word_len*10 + int(ch)
            elif ch == "#":
                word = s[idx+1: idx+1+word_len]
                result.append(word)
                idx += word_len
                word_len = 0
            idx += 1
        
        return result


