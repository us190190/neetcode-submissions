class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        result = [0] * len(temperatures)

        temp_stack = []

        for i, tmp in enumerate(temperatures):
            while temp_stack and temp_stack[-1][1]<tmp:
                prev_tmp = temp_stack.pop()
                result[prev_tmp[0]] = i-prev_tmp[0]
            temp_stack.append((i, tmp))
        
        return result
        