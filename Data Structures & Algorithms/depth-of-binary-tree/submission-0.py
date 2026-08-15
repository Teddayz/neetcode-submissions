# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node: Optional[TreeNode], depth: int) -> int:
            if node == None:
                return depth
            depth += 1
            return max(dfs(node.left, depth), dfs(node.right, depth))
        
        return dfs(root, 0)