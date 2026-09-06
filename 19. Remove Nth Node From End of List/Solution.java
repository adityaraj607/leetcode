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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        int l=0;
        ListNode curr = head;
        while (curr != null) {
            l++;
            curr=curr.next;
        }
        int target=l-n;
        if (target==0) {
            return head.next;
        }
        ListNode ptr=head;
        int currindex=1;
        while (ptr != null) {
            if (currindex == target) {
                ptr.next=ptr.next.next;
                break;
            }
            currindex++;
            ptr=ptr.next;
        }
        return head;
    }
}
