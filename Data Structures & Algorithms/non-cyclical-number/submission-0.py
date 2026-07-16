class Solution:
    def isHappy(self, n: int) -> bool:

        visited = set()

        while n!=1:
            visited.add(n)
            new_n = 0
            while n:
                digit = n%10
                new_n += (digit*digit)
                n //= 10
            n = new_n
            if n in visited:
                return False
        
        return True
            
                
        