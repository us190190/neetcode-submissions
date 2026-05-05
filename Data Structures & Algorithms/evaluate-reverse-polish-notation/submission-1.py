class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        operators = "+-*/"

        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()
                if token == "+":
                    c = a + b
                elif token == "-":
                    c = a - b
                elif token == "*":
                    c = a * b
                elif token == "/":
                    c = a / b
                stack.append(int(c))
        
        return stack.pop()