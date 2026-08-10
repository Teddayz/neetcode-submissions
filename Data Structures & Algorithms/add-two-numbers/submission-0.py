# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        output = dummy
        carry = 0
        while l1 or l2 or carry:
            curr = 0
            if l1:
                curr += l1.val
                l1 = l1.next
            if l2:
                curr += l2.val
                l2 = l2.next
            if carry:
                curr += carry
                carry = 0
            if curr >= 10:
                curr -= 10
                carry = 1
            output.next = ListNode(curr)
            output = output.next
        return dummy.next
        
            


        