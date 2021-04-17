/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode *deleteDuplicates(struct ListNode *head)
{
    if (head == NULL)
    {
        return head;
    }
    struct ListNode *pre = head;
    struct ListNode *cur = head;
    cur = cur->next;
    while (cur != NULL)
    {

        
            while (cur!=NULL && cur->val == pre->val)
            {
                printf("cur.val=%d pre.val=%d \n", cur->val, pre->val);
                pre->next = cur->next;

                free(cur);

                cur = pre->next;
            }
        

        if (cur != NULL)
            cur = cur->next;
        pre = pre->next;
    }
    return head;
}