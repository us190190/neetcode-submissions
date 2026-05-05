class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = {}

        for s in strs:
            s_index = ''.join(sorted(s))
            if s_index not in groups:
                groups[s_index] = []
            groups[s_index].append(s)
        
        anagrams = []

        for anagram, values in groups.items():
            anagrams.append(values)

        return anagrams
