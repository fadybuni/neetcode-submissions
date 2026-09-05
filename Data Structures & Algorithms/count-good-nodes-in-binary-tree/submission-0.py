# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        curr = float('-inf')
        def dfs(root, curr):
            nonlocal res
            if root:
                if root.val >= curr:
                    curr = root.val
                    res += 1
                dfs(root.left, curr)
                dfs(root.right, curr)
            return
        dfs(root, curr)
        return res
            

        