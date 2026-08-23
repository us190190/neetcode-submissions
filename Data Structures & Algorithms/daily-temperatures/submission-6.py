class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stk: List[Tuple[int, int]] = []
        result = [0]*len(temperatures)

        for day, temp in enumerate(temperatures):
            while stk and stk[-1][1]<temp:
                p_day, p_temp = stk.pop()
                result[p_day] = day - p_day
            stk.append((day, temp))
        
        return result
            
        