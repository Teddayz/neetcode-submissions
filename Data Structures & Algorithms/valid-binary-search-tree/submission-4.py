# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def dfs(node: Optional[TreeNode], minimum: int, maximum: int) -> bool:
            left, right = True, True
            if node.val >= maximum or node.val <= minimum:
                return False
            if node.left:
                left = dfs(node.left, minimum, min(node.val, maximum))
            if node.right:
                right = dfs(node.right, max(minimum, node.val), maximum)
            
            return left and right
        return dfs(root, -math.inf, math.inf)
