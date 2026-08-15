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
        hashMap = {}
        dummy = Node(0, head)

        # Create the copied nodes and put into hashMap
        while head != None:
            duplicatedNode = Node(head.val, head.next)
            hashMap[head] = duplicatedNode
            duplicatedNode = duplicatedNode.next
            head = head.next

        curr = dummy.next
        output = Node(0, curr)
        output_curr = hashMap.get(curr)
        while curr != None:
            duplicatedNode = hashMap.get(curr)
            duplicatedNode.next = hashMap.get(curr.next)
            duplicatedNode.random = hashMap.get(curr.random)
            output_curr = duplicatedNode
            curr = curr.next
            output_curr = output_curr.next

        return hashMap[output.next] if hashMap else None