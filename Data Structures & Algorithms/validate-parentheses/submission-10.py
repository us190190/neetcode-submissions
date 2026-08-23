class Solution:
    def isValid(self, s: str) -> bool:

        ref = {"}":"{", "]":"[", ")":"("}
        stk = []

        for ch in s:
            if ch not in ref:
                stk.append(ch)
            else:
                if not stk:
                    return False
                top = stk.pop()
                if top != ref[ch]:
                    return False
        
        return True if not stk else False
                
        