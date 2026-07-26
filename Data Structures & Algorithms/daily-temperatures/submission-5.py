class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stk = []
        length = len(temperatures)
        result = [0]*length
        stk.append([0,temperatures[0]])

        for i in range(1, length):
            while stk and stk[-1][1]<temperatures[i]:
                idx, tmp = stk.pop()
                result[idx] = i-idx
            stk.append([i, temperatures[i]])

        return result

        