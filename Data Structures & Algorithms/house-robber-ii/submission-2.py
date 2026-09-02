class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        dupe = nums[:]
        dupe.append(nums[0])
        dupe.reverse()
        dupe.pop()
        dupe.reverse()
        
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        for i in range(2,len(nums)-1):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        
        
        tp = [0] * len(dupe)
        tp[0] = dupe[0]
        tp[1] = max(dupe[0],dupe[1])
        for i in range(2,len(dupe)-1):
            tp[i] = max(tp[i-2] + dupe[i], tp[i-1])

        return max(tp[-2],dp[-2])
            