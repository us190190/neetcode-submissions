class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        result = [0] * len(temperatures)
        ref_stk = []

        for idx in range(len(temperatures)):
            c_temp = temperatures[idx]
            while len(ref_stk) and ref_stk[-1][1] < c_temp:
                pop_idx, pop_temp = ref_stk.pop()
                result[pop_idx] = idx - pop_idx
            ref_stk.append((idx, c_temp))
        
        return result
        