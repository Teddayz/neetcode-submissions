# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0

        def dfs(node: Optional[TreeNode]) -> int:
            if node == None:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            diameter = left + right
            self.max_diameter = max(diameter, self.max_diameter)

            return 1 + max(left, right)
        dfs(root)
        return self.max_diameter