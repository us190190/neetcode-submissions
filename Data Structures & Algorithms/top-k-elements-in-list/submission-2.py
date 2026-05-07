class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        frequencies, result = {}, []
        buckets = [[] for i in range(len(nums)+1)]

        for num in nums:
            frequencies[num] = 1 if num not in frequencies else frequencies[num]+1
        
        for num, freq in frequencies.items():
            buckets[freq].append(num)
        
        for index in range(len(buckets)-1, 0, -1):
            for val in buckets[index]:
                result.append(val)
                k -= 1
                if not k:
                    return result
        
        return result
        