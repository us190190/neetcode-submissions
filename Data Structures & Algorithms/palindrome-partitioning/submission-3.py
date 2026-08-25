class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        self.result = []

        def _is_palindrome(strng: str) -> bool:
            l, r = 0, len(strng)-1
            while l<r:
                if strng[l]!=strng[r]:
                    return False
                l += 1
                r -= 1
            return True

        def dfs(i: int, partition: List[str]):
            if i == len(s):
                self.result.append(partition.copy())
                return
            
            for idx in range(i, len(s)):
                st = s[i:idx+1]
                if _is_palindrome(st):
                    dfs(idx+1, partition + [st])
                

        
        dfs(0, [])

        return self.result