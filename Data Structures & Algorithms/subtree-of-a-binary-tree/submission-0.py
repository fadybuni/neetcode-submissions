# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def helper(root,subRoot):
            if not subRoot and not root:
                return True
            elif not subRoot or not root:
                return False
            elif subRoot.val != root.val:
                return False
            else:
                return helper(root.left,subRoot.left) and helper(root.right,subRoot.right)



        if not root:
            return False

        if helper(root,subRoot):
            return True
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)

        
            
            
        