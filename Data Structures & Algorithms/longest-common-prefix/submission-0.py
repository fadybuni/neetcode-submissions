class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        curr = ""
        LCP = ""
        for i in range(len(strs[0])):
            curr = strs[0][i]
            for j in strs:
                if i == len(j) or j[i] != curr:
                    return LCP
            LCP += curr
        return LCP
            
