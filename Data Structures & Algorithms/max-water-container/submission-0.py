class Solution:
    def maxArea(self, heights: List[int]) -> int:
        currmax = 0

        for i in range(len(heights)):
            for j in range(i,len(heights)):
                multi = min(heights[i], heights[j])
                currmax= max(currmax, multi * (j - i))
        return currmax