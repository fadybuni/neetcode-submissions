class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = {}
        for word in strs:
            curr = "".join(sorted(word))
            if curr in words:
                words[curr].append(word)
            else:
                words[curr] = [word]
        return list(words.values())