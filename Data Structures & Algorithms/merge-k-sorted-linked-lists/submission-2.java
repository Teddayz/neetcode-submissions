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
    public ListNode mergeKLists(ListNode[] lists) {
        if (lists.length == 0) {
            return null;
        } else if (lists.length == 1) {
            return lists[0];
        } else {
            int interval = 1;
            while (interval < lists.length) {
                for (int i = 0; i + interval < lists.length; i += interval * 2) {
                    lists[i] = mergeTwoLists(lists[i], lists[i + interval]);
                }
                interval *= 2;
            }
        
            return lists[0];
        }
    }

    private ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode dummy = new ListNode();
        ListNode curr = dummy;
        while (list1 != null && list2 != null) {
            if (list1.val <= list2.val) {
                curr.next = list1;
                list1 = list1.next;
            } else {
                curr.next = list2;
                list2 = list2.next;
            }
            curr = curr.next;
        }
        if (list1 == null && list2 != null) {
            curr.next = list2;
        } else if (list2 == null && list1 != null) {
            curr.next = list1;
        }
        return dummy.next;
    }
}
