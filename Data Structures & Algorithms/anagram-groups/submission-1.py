class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        ref, res = {}, []

        for s in strs:
            index = ''.join(sorted(s))

            if index not in ref:
                ref[index] = []
            
            ref[index].append(s)
        
        for index, anagrams in ref.items():
            res.append(anagrams)
        
        return res

        