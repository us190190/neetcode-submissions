class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stk = []

        for token in tokens:
            if token in "+-*/":
                b = stk.pop()
                a = stk.pop()
                if token == "+":
                    c = a + b
                elif token == "-":
                    c = a - b
                elif token == "*":
                    c = a * b
                else:
                    c = int(a/b)
                stk.append(c)
            else:
                stk.append(int(token))
            
            print(stk)
        
        return stk.pop()
        