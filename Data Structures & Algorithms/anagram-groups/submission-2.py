class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        ref = {}

        for s in strs:
            key = "".join(sorted(s))
            if key not in ref:
                ref[key] = []
            ref[key].append(s)
        
        return list(ref.values())