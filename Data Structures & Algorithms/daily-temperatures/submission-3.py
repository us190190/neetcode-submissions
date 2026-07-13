class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stk = [] # idx, val
        result = [0]*len(temperatures)

        for i, temp in enumerate(temperatures):
            while stk and stk[-1][1]<temp:
                idx, t = stk.pop()
                result[idx] = i-idx
            stk.append([i,temp])
        
        return result
        