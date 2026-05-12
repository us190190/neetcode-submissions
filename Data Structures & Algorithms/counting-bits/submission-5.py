class Solution:
    def countBits(self, n: int) -> List[int]:

        result = [0] * (n+1)
        power = 1

        for i in range(1, n+1):
            power = power*2 if i/power==2 else power
            print(power)
            result[i] = 1 + result[i-power]
        
        return result

        