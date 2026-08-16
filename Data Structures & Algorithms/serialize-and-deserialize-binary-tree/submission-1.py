# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        result = []
        frontier = deque()
        prev = -1001
        frontier.append(root)
        while frontier:
            node = frontier.popleft()
            if not node:
                result.append("N;")
                continue
            frontier.append(node.left)
            frontier.append(node.right)

            result.append(str(node.val) + ';')
        return "".join(result)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        
        data = [x for x in data.split(';') if x]
        if data[0] == 'N':
            return None
        root = TreeNode(int(data[0]))
        queue = deque([root])
        i = 1
        while queue:
            node = queue.popleft()
            # next value is left child
            leftChild = data[i]
            i += 1
            rightChild = data[i]
            i += 1
            if leftChild == 'N':
                leftChild = None
            else:
                leftChild = TreeNode(int(leftChild))
                queue.append(leftChild)

            if rightChild == 'N':
                rightChild = None
            else:
                rightChild = TreeNode(int(rightChild))
                queue.append(rightChild)
            node.left = leftChild
            node.right = rightChild

        return root
