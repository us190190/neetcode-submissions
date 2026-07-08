class Solution:
    def isValid(self, s: str) -> bool:

        ref = {"]": "[", "}": "{", ")": "("}
        o_b = []
        for ch in s:
            if ch in "{[(":
                o_b.append(ch)
            else:
                if not len(o_b):
                    return False
                top = o_b.pop()
                if not (ch in ref and top == ref[ch]):
                    return False
        return not len(o_b)



        