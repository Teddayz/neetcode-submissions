"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Create a hashMap, whereby each node is pointing to its replicated node. Then replace each node with its replicated node
        if not head:
            return None
        hashMap = {}
        curr = head
        while curr:
            duplicated_node = Node(curr.val)
            hashMap[curr] = duplicated_node
            curr = curr.next
        curr = head
        duplicated_curr = hashMap[curr]
        dummyNode = Node(0, duplicated_curr)

        while curr != None:
            duplicated_curr.next = hashMap.get(curr.next)
            duplicated_curr.random = hashMap.get(curr.random)
            curr = curr.next
            duplicated_curr = duplicated_curr.next
        return dummyNode.next
        
