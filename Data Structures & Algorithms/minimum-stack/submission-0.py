class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        

    def push(self, val: int) -> None:
        prev_min = self.min_stack[-1] if len(self.min_stack) else val
        self.stack.append(val)
        self.min_stack.append(min(prev_min, val))

    def pop(self) -> None:
        if len(self.stack):
            self.stack.pop()
            self.min_stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]
        
