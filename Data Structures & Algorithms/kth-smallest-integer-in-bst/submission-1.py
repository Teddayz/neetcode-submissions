# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        self.count = 0
        self.res = -1

        def dfs(node: TreeNode | None) -> None:
            if not node:
                return
            dfs(node.left)
            self.count += 1
            if self.count == k:
                self.res = node.val
            dfs(node.right)
            
        dfs(root)
        return self.res

