class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        ref = {}

        for num in nums:
            if num not in ref:
                ref[num] = 0
            ref[num] += 1
        
        result = []
        while len(result)<k:
            m, f = float('-inf'), float('-inf')
            for num, freq in ref.items():
                if freq>=f and num not in result:
                    m, f = num, freq
            result.append(m)
        
        return result



        