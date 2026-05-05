class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        frequencies = {}

        freq_buckets = [[] for i in range(len(nums)+1)]

        for num in nums:
            if num not in frequencies:
                frequencies[num] = 0
            frequencies[num] += 1
        
        for num, freq in frequencies.items():
            freq_buckets[freq].append(num)
        
        results = []

        for freq in range(len(freq_buckets)-1, 0, -1):
            for num in freq_buckets[freq]:
                results.append(num)
                k -= 1
                if k==0:
                    return results
        
        return results

        