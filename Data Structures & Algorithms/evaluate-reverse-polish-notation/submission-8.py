class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stk: List[int] = []

        for token in tokens:
            if token not in "+-*/":
                stk.append(int(token))
            else:
                b = stk.pop()
                a = stk.pop()
                if token == "+":
                    output = a + b
                elif token == "-":
                    output = a - b
                elif token == "*":
                    output = a * b
                else:
                    output = int(a / b)
                stk.append(output)
        
        return stk[0]

        