# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        frontier = deque()
        frontier.append((root, -101))
        count = 0
        while frontier:
            node, prev_high = frontier.popleft()
            if node.val >= prev_high:
                count += 1
                prev_high = node.val
            if node.left:
                frontier.append((node.left, prev_high))
            if node.right:
                frontier.append((node.right, prev_high))
            
        return count
            