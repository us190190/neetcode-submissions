class Solution:

    def encode(self, strs: List[str]) -> str:

        res = []
        for s in strs:
            res.append(str(len(s))+"#"+s)
        return "".join(res)
        # 5#Hello5#World

    def decode(self, s: str) -> List[str]:

        res = []
        i = 0
        length = 0

        while i<len(s):
            j = i
            while s[j]!="#":
                j += 1
            length = int(s[i:j])
            res.append(s[(j+1):(j+1+length)])
            i = j+length+1

        return res  
