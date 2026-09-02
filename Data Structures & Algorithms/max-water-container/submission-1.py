class Solution:
    def maxArea(self, heights: List[int]) -> int:
        currmax = 0
        l = 0
        r = len(heights) - 1
        currmax = 0

        while l < r:
            currmax = max(currmax, (r-l) * min(heights[l], heights[r]))

            if heights[l] < heights[r]:
                l += 1
            else:
                r-= 1
        return currmax