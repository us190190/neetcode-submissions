class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        # s1 = "abc", s2 = "xyz", s3 = "abxzcy"
        #. ab. c.      x   yz     ab x c yz
        if len(s1) + len(s2) != len(s3):
            return False
        memo = {}

        def compare(s1_idx, s2_idx):
            if (s1_idx + s2_idx) == len(s3):
                return True
            
            if (s1_idx, s2_idx) not in memo:
                s3_idx = s1_idx + s2_idx
                result = False
                if s1_idx<len(s1) and s3_idx<len(s3) and s1[s1_idx] == s3[s3_idx]:
                    result = result or compare(s1_idx + 1, s2_idx)
                if s2_idx<len(s2) and s3_idx<len(s3) and s2[s2_idx] == s3[s3_idx]:
                    result = result or compare(s1_idx, s2_idx + 1)
                memo[(s1_idx, s2_idx)] = result
            
            return memo[(s1_idx, s2_idx)]
        
        return compare(0, 0)


        