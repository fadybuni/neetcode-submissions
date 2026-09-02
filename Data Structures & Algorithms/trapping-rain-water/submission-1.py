class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        total = 0

        leftmax = height[l]
        rightmax = height[r]
        lowermax = min(leftmax,rightmax)

        while l < r:
            if lowermax == leftmax:
                l+= 1
                total += max(0,(leftmax - height[l]))
                leftmax = max(leftmax, height[l])
                lowermax = min(leftmax,rightmax)
            else:
                r-= 1
                total += max(0,(rightmax - height[r]))
                rightmax = max(rightmax,height[r])
                lowermax = min(leftmax,rightmax)


        return total

