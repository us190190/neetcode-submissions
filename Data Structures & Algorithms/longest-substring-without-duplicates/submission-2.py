class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        length, result, seen, l = len(s), 0, {}, 0

        for r in range(length):
            if s[r] in seen:
                result = max(result, len(seen))
                last_seen_at = seen[s[r]]
                while l<=last_seen_at:
                    seen.pop(s[l])
                    l += 1
            seen[s[r]] = r
        
        return max(result, len(seen))


        