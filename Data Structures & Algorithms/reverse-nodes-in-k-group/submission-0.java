/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode reverseKGroup(ListNode head, int k) {
        ListNode dummy = new ListNode();
        ListNode curr = head;
        dummy.next = head;
        ListNode prevGroupPointer = dummy;
        int check = 1;
        while (curr != null) {
            // Found 1 group of length k
            ListNode firstNode = curr;
            ListNode nextPointer = curr;
            for (int i = 0; i < k; i++) {
                if (curr == null) {
                    check = 0;
                    break;
                }
                check = 1;
                curr = curr.next;
            }
            // This would reverse k nodes and set the prevGroupPointer to the last node
            // Last node is curr
            if (check == 0) {
                prevGroupPointer.next = firstNode;
                break;
            }
            ListNode next = null;
            ListNode prev = null;
            while (firstNode != curr) {
                next = firstNode.next;
                firstNode.next = prev;
                prev = firstNode;
                firstNode = next;
            }
            prevGroupPointer.next = prev;
            prevGroupPointer = nextPointer;
        }
        return dummy.next;
    }
}
