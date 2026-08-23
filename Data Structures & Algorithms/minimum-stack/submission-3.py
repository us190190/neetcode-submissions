class MinStack:

    def __init__(self):
        self.stk: List[Tuple(int, int)] = []

    def push(self, val: int) -> None:
        cur_min = val
        if self.stk:
            cur_min = min(cur_min, self.getMin())
        self.stk.append((val, cur_min))

    def pop(self) -> None:
        if self.stk:
            self.stk.pop()

    def top(self) -> int:
        if self.stk:
            return self.stk[-1][0]

    def getMin(self) -> int:
        if self.stk:
            return self.stk[-1][1]
        
