class Solution:
    def isValid(self, s: str) -> bool:

        q = deque()
        ref = {')':'(', '}':'{', ']':'['}

        for ch in s:
            if ch in "({[":
                q.append(ch)
            else:
                if not len(q):
                    return False
                top = q.pop()
                if top != ref[ch]:
                    return False
        
        return not len(q)

        