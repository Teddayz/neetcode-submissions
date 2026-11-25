# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:

        def dfs(node: TreeNode | None, minimum: int, maximum: int) -> bool:
            if not node:
                return True
            if node.val <= minimum or node.val >= maximum:
                return False

            left = dfs(node.left, minimum, min(maximum, node.val))
            right = dfs(node.right, max(minimum, node.val), maximum)
            
            return left and right
        
        return dfs(root, -math.inf, math.inf)
