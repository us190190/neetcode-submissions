class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:

        stk = [[0,""]]
        length = len(s)
        i=0

        while i<length:

            ch = s[i]
            if stk[-1][1]==ch:
                if stk[-1][0]==k-1:
                    stk.pop()
                else:
                    stk[-1][0] += 1
            else:
                stk.append([1,ch])
            i += 1
        
        return "".join(["".join(ch*count) for count,ch in stk])


        