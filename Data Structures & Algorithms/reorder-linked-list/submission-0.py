# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            
        second_half = slow.next
        slow.next = None

        # Reverse from the middle index
        prev = None
        while second_half != None:
            temp = second_half.next
            second_half.next = prev
            prev = second_half
            second_half = temp
        curr1 = head
        curr2 = prev
        
        while curr1 and curr2:
            next1 = curr1.next
            next2 = curr2.next
            curr1.next = curr2
            # If its not None
            if next1:
                curr2.next = next1
            
            curr1 = next1
            curr2 = next2

                
        