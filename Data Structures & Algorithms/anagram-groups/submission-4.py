class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        words = {}
        n = len(strs)
        for i in range(n):
            sort = ''.join(sorted(strs[i]))
            if sort in words:
                words[sort].append(strs[i])
            else:
                words[sort] = [strs[i]]
        for value in words.values():
            res.append(value)
        return res