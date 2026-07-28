class Solution:
    def decodeString(self, s: str) -> str:

        length = len(s)
        i = 0
        sub_str = [[1,""]]

        while i<length:
            ch = s[i]

            if ord("0")<=ord(ch)<=ord("9"):
                num = 0
                while i<length and s[i]!="[":
                    num = (num*10)+int(s[i])
                    i += 1
                sub_str.append([num,""])
                i += 1
            elif ch=="]":
                num, st = sub_str.pop()
                while num:
                    sub_str[-1][1] += st
                    num -= 1
                i += 1
            else:
                sub_str[-1][1] += ch
                i += 1
        
        return sub_str[-1][1]

        