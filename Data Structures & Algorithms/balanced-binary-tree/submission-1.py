# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.max_difference = 0
        
        def dfs(node: Optional[TreeNode]) -> int:
            if node == None:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            self.max_difference = max(self.max_difference, abs(right - left))

            return 1 + max(left, right)
        dfs(root)
        
        if self.max_difference > 1:
            return False
        return True