/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* reverseList(struct ListNode* head) {
    struct ListNode *last=NULL, *curr=head, *next=NULL;

    while (curr!=NULL){
        next=curr->next;
        curr->next=last;
        last=curr;
        curr=next;
    }
    return last;
}