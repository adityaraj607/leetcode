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
    public ListNode rotateRight(ListNode head, int k) {
        if(head==null || head.next==null){
            return head;
        }
        int l=1;
        ListNode tail=head;
        while(tail.next!=null){
            tail=tail.next;
            l++;
        }
        if((k%l)==0) return head;
        tail.next=head;
        ListNode ntail=head;
        for (int i=1;i<(l-(k%l));i++){
            ntail=ntail.next;
        }
        ListNode nhead=ntail.next;
        ntail.next=null;
        return nhead;
    }
}