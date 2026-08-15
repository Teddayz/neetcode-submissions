# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if p == None and q == None:
                return True
            if not p or not q:
                return False

            if p.val == q.val:
                return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
                
            return False
        
        def dfs(node: Optional[TreeNode]) -> bool:
            if node == None:
                return False
            left = dfs(node.left)
            right = dfs(node.right)

            return isSameTree(node, subRoot) or left or right
        return dfs(root)