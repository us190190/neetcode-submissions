class MinStack:

    def __init__(self):
        self.main_stk = []
        self.min_stk = []

    def push(self, val: int) -> None:
        self.main_stk.append(val)
        curr_min = val if not len(self.min_stk) else min(self.min_stk[-1], val)
        self.min_stk.append(curr_min)

    def pop(self) -> None:
        if len(self.main_stk):
            self.main_stk.pop()
            self.min_stk.pop()

    def top(self) -> int:
        if len(self.main_stk):
            return self.main_stk[-1]
        return None

    def getMin(self) -> int:
        if len(self.min_stk):
            return self.min_stk[-1]
        return None
        
