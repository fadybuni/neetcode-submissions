class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        i = 0

        def dfs(start, path, remaining):
            if remaining == 0:
                res.append(path[:])
            for i in range(start, len(nums)):
                if remaining < 0:
                    break
                path.append(nums[i])
                dfs(i,path, remaining - nums[i])
                path.pop()

        dfs(0,[],target)
        return res