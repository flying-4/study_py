/*
 struct ListNode* reverseList(struct ListNode* head) {
    struct ListNode* prev=NULL;
    while(head!=NULL)
    {
        struct ListNode* next=head->next;
        head->next=prev;
        prev=head;
        head=next;
    }
    return prev;
}
 */
