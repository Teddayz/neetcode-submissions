# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummyNode = ListNode()
        dummyNode.next = head
        slow, fast = head, head
        for _ in range(n):
            fast = fast.next
        prev = dummyNode
        while fast != None:
            prev = prev.next
            slow = slow.next
            fast = fast.next
        prev.next = slow.next
        return dummyNode.next