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
    public void reorderList(ListNode head) {
        if (head == null || head.next == null) {
            return;
        }
        ListNode t1 = head;
        ListNode t2 = head;
        while (t2.next!=null && t2.next.next!=null) {
            t1=t1.next;
            t2=t2.next.next;
        }
        ListNode second = t1.next;
        t1.next =null;
        ListNode prev =null;
        while(second!=null) {
            ListNode next=second.next;
            second.next=prev;
            prev=second;
            second=next;
        }
        ListNode first=head;
        second=prev;
        while(second!=null) {
            ListNode temp1=first.next;
            ListNode temp2=second.next;
            first.next=second;
            second.next=temp1;
            first=temp1;
            second=temp2;
        }
    }
}