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
        dummyNode = Node(0, head)
        curr = head
        while curr:
            duplicated_node = Node(curr.val, None, None)
            hashMap[curr] = duplicated_node
            curr = curr.next
        curr = head
        duplicated_curr = hashMap[curr]
        dummyNode.next = duplicated_curr
        while curr != None:
            if not curr.next:
                duplicated_curr.next = None
            else:
                duplicated_curr.next = hashMap[curr.next]
            if not curr.random:
                duplicated_curr.random = None
            else:
                duplicated_curr.random = hashMap[curr.random]
            curr = curr.next
            duplicated_curr = duplicated_curr.next
        return dummyNode.next
        
