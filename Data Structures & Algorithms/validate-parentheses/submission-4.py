class Solution:
    def isValid(self, s: str) -> bool:

        visited = []
        open_braces = {'{':0, '(':1, '[':2}
        closed_braces = {'}':0, ')':1, ']':2}

        for ch in s:
            if ch in open_braces:
                visited.append(ch)
            elif ch in closed_braces:
                if len(visited)<1:
                    return False
                top = visited.pop()
                if open_braces[top] != closed_braces[ch]:
                    return False
        
        return len(visited)<1
        