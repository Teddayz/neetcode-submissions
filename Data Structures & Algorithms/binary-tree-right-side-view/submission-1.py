# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        if not root:
            return []
        res = []
        frontier = []
        frontier.append((root, 0))
        seen = set()
        while frontier:
            node, level = frontier.pop()
            if level not in seen:
                res.append(node.val)
            seen.add(level)
            if node.left:
                frontier.append((node.left, level + 1))
            if node.right:
                frontier.append((node.right, level + 1))
        return res