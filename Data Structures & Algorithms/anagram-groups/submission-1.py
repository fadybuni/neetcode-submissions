class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = {}
        for i in strs:
            sort = ''.join(sorted(i))
            if sort in dictionary:
                dictionary[sort].append(i)
            else:
                dictionary[sort] = [i]
        return list(dictionary.values())