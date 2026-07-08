class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        result = [0]*len(temperatures)
        stk = [] # monotonic decreasing stk

        for i, tmp in enumerate(temperatures):
            while stk and stk[-1][1]<tmp:
                idx, t = stk.pop()
                result[idx] = i-idx
            stk.append([i, tmp])

        return result 
        