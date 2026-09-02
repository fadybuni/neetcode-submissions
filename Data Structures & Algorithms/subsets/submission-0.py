class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        

        res = []
        def dfs(curr, path):
            res.append(path[:])
            for i in range(curr, len(nums)):
                path.append(nums[i])
                dfs(i + 1, path)
                path.pop()
            
        
        dfs(0,[])
        return res