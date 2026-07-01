class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        result = {}
        for s in strs:
            idx = "".join(sorted(s))
            if idx not in result:
                result[idx] = []
            result[idx].append(s)
        
        return list(result.values())