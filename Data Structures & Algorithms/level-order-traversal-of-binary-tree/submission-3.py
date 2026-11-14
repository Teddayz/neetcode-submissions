# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        frontier = deque()
        frontier.append((root, 0))
        while frontier:
            node, level = frontier.popleft()
            if not res or len(res) <= level:
                res.append([])
            res[level].append(node.val)
            if node.left:
                frontier.append((node.left, level + 1))
            if node.right:
                frontier.append((node.right, level + 1))
        return res