# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head
        dummy = ListNode()
        dummy.next = head
        prev = dummy

        slow = head
        fast = head
        for i in range(n):
            fast = fast.next
        # Slow is the node to remove
        while fast != None:
            prev = slow
            slow = slow.next
            fast = fast.next
        prev.next = slow.next
        return dummy.next

        