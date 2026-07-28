class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:

        ref = {}

        for num in nums:
            if num not in ref:
                ref[num] = 0
            ref[num] += 1
        
        freqs = []
        rev_ref = {}
        for num, f in ref.items():
            if f not in rev_ref:
                freqs.append(f)
                rev_ref[f] = []
            rev_ref[f].append(num)
        
        freqs.sort()
        result = []
        for freq in freqs:
            sub_nums = rev_ref[freq]
            sub_nums.sort(reverse=True)
            for num in sub_nums:
                i = freq
                while i:
                    result.append(num)
                    i -= 1
        
        return result


        