class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stk = []
        for token in tokens:
            if token in "+-/*":
                b = stk.pop()
                a = stk.pop()
                if token == "+":
                    val = a+b
                elif token == "-":
                    val = a-b
                elif token == "*":
                    val = a*b
                else:
                    val = int(a/b)
            else:
                val = int(token)
            stk.append(val)
        return stk.pop()

        