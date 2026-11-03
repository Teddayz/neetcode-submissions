# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        # preorder gives you order of root nodes
        # inorder decides which side of the tree it belongs to
        pMap = {value: index for index, value in enumerate(inorder)}
        self.index = 0

        def build(left: int, right: int):

            if left > right:
                return None

            currval = preorder[self.index]
            currNode = TreeNode(currval)
            mid = pMap[currval]
            self.index += 1

            currNode.left = build(left, mid - 1)
            currNode.right = build(mid + 1, right)

            return currNode

        return build(0, len(preorder) - 1)
