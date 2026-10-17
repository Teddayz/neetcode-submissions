# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        
        def dfs(node: TreeNode, prevMax: int) -> None:
            if not node:
                return
            
            if node.val >= prevMax:
                self.count += 1
                prevMax = node.val

            left = dfs(node.left, prevMax)
            right = dfs(node.right, prevMax)
        dfs(root, -math.inf)
        return self.count
        

        