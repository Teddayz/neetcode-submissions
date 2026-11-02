# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummyNode = ListNode()
        dummyNode.next = head
        curr = head
        size = 0
        while curr != None:
            size += 1
            curr = curr.next

        curr = dummyNode
        target_index = size - n
        for _ in range(target_index):
            curr = curr.next
        
        curr.next = curr.next.next

        return dummyNode.next
