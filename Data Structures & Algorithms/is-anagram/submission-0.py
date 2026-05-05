class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        visitedFirst = {}
        for ch in s:
            if ch not in visitedFirst:
                visitedFirst[ch]=0
            visitedFirst[ch]+=1
        
        visitedSecond = {}
        for ch in t:
            if ch not in visitedSecond:
                visitedSecond[ch]=0
            visitedSecond[ch]+=1
        
        if len(visitedFirst) != len(visitedSecond):
            return False
        
        for ch in visitedFirst:
            if ch not in visitedSecond:
                return False
            if visitedFirst[ch] != visitedSecond[ch]:
                return False
        
        return True
        