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
        frontier = deque()
        index = 0
        output = []
        frontier.append((root, index))
        while frontier:
            item = frontier.popleft()
            index = item[1]
            if item[0].left != None:
                frontier.append((item[0].left, index + 1))
            if item[0].right != None:
                frontier.append((item[0].right, index + 1))
            if len(output) <= index:
                output.append([])
            output[index].append(item[0].val)


        return output