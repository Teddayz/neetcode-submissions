# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0
        
        def dfs(node: TreeNode, curr_max: int) -> None:
            if not node:
                return 
            if node.val >= curr_max:
                curr_max = node.val
                self.res += 1
            dfs(node.left, curr_max)
            dfs(node.right, curr_max)

        dfs(root, root.val)
        return self.res
            