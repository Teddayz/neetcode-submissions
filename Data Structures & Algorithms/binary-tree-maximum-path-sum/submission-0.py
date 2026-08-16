# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maximumPathSum = -math.inf
        
        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            left = max(dfs(node.left), 0)   # clamp negative to 0
            right = max(dfs(node.right), 0) # clamp negative to 0
            
            self.maximumPathSum = max(self.maximumPathSum, left + right + node.val)
            return node.val + max(left, right)

        dfs(root)
        return self.maximumPathSum
