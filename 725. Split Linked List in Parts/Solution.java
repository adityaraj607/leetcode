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
    public ListNode[] splitListToParts(ListNode head, int k) {
        ListNode[] r=new ListNode[k];
        int count=0;
        ListNode temp=head;
        while(temp!=null){
            temp=temp.next;
            count+=1;
        }
        int parts=count/k;
        int f=count%k;
        temp = head;
        for (int i=0;i<k && temp!=null;i++) {
            r[i]=temp;
            int c=parts+(i<f?1:0);
            for (int j=0;j<(c-1);j++) {
                temp = temp.next;
            }
            ListNode nextPart=temp.next;
            temp.next=null;
            temp=nextPart;
        }
        return r;
    }
}