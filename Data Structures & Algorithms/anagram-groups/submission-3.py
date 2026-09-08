class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for i in strs:
            sort = "".join(sorted(i))
            if sort in seen:
                seen[sort].append(i)
            else:
                seen[sort] = [i]
        return list(seen.values())
            