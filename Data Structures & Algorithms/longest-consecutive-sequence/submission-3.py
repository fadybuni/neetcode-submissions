class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        if not nums:
            return 0
        curr = 1
        greatest = 1

        n = len(nums)

        for i in range(1,n):
            if nums[i] == nums[i-1]:
                continue
            if nums[i] == nums[i-1]+1:
                curr += 1
                greatest = max(greatest,curr)
            else:
                curr = 1
        
        return greatest