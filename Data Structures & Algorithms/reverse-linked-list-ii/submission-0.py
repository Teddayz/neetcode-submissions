# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        def reverseLinkedList(node, n) -> ListNode | None:
            if not node:
                return None
            prev = None
            first_node = node
            while n >= 0:
                temp = node.next
                node.next = prev
                prev = node
                node = temp
                n -= 1
            first_node.next = node
            return prev
        dummyNode = ListNode(0, head)
        pos = 1
        curr = dummyNode
        while pos < left:
            curr = curr.next
            pos += 1
        reversed = reverseLinkedList(curr.next, right - left)
        curr.next = reversed
        return dummyNode.next


