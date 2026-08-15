# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if not root:
            return result
        frontier = deque()
        frontier.append(root)
        while frontier:
            level = []
            for i in range(len(frontier)):
                node = frontier.popleft()
                if node.left:
                    frontier.append(node.left)
                if node.right:
                    frontier.append(node.right)
                level.append(node)
            result.append(level[-1].val)
        return result
            

