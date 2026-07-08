class MinStack:

    def __init__(self):
        self._stk = []

    def push(self, val: int) -> None:
        length = len(self._stk)
        min_so_far = self._stk[length-1][1] if length else val
        min_so_far = min(min_so_far, val)
        self._stk.append([val, min_so_far])

    def pop(self) -> None:
        self._stk.pop()

    def top(self) -> int:
        length = len(self._stk)
        return self._stk[length-1][0]

    def getMin(self) -> int:
        length = len(self._stk)
        return self._stk[length-1][1]
        
