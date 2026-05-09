class Solution:
    def isValid(self, s: str) -> bool:

        stk = []

        for ch in s:
            if ch in "{[(":
                stk.append(ch)
            else:
                if not len(stk):
                    return False
                popped = stk.pop()
                if ch == "}" and popped != "{":
                    return False
                elif ch =="]" and popped != "[":
                    return False
                elif ch ==")" and popped != "(":
                    return False
        
        return True if not len(stk) else False

        