# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0

        def dfs(node: Optional[TreeNode], height: int) -> int:
            if node == None:
                return 0
            height += 1
            left = dfs(node.left, height)
            right = dfs(node.right, height)
            diameter = left + right
            self.max_diameter = max(diameter, self.max_diameter)

            return 1 + max(left, right)
        dfs(root, 0)
        return self.max_diameter