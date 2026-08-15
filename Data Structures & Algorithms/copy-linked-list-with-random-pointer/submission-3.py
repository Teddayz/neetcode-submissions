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
        if not head:
            return None
        hashMap = {}
        curr = head
        while curr:
            hashMap[curr] = Node(curr.val)
            curr = curr.next
        curr = head
        while curr:
            hashMap[curr].next = hashMap.get(curr.next)
            hashMap[curr].random = hashMap.get(curr.random)
            curr = curr.next
        return hashMap[head]
