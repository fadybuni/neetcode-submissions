class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        j = 0
        res = 0
        for i in s:
            while i in seen:
                    seen.remove(s[j])
                    j += 1
            seen.add(i)
            res = max(len(seen),res)
        return res