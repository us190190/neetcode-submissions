class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        length = len(temperatures)
        result = [0]*length

        for start in range(length):
            for end in range(start+1, length):
                if temperatures[end]>temperatures[start]:
                    result[start] = end-start
                    break

        return result

        