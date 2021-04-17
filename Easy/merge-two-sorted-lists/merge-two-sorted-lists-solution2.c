/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
#include <stdio.h>
#include <stdlib.h>
struct ListNode
{
    int val;
    struct ListNode *next;
    /* val */
} ListNode;
struct ListNode *initList()
{
    struct ListNode *list = (struct ListNode *)malloc(sizeof(struct ListNode));
    list->next = NULL;
    return list;
}
void listPrint(struct ListNode *node)
{
    struct ListNode *tempNode = node;

    while (tempNode != NULL)
    {
        if (tempNode->val >= 0)
            printf("(%d)->", tempNode->val);
        else
        {
            printf("(%d)->", tempNode->val);
        }

        tempNode = tempNode->next;
    }
    printf("\n");
}
void freeLastOne(struct ListNode *node)
{

    struct ListNode *tempNode = node;
    if (tempNode == NULL)
    {
    }
    else
    {
        while (tempNode->next->next != NULL)
        {
            tempNode = tempNode->next;
        }

        printf("free .. %d \n", tempNode->val);
        struct ListNode *t = tempNode->next;
        free(t);
        tempNode->next = NULL;
    }
}
void insertNode(struct ListNode *node, int x)
{
    //直接插到尾巴

    struct ListNode *tempNode = node;
    while (tempNode->next != NULL)
    {
        tempNode = tempNode->next;
    }
    struct ListNode *temp = (struct ListNode *)malloc(sizeof(struct ListNode));

    tempNode->val = x;
    tempNode->next = temp;
    temp->next = NULL;
    temp->val = 0;

    printf("insert .. %d \n", x);
}
struct ListNode *mergeTwoLists(struct ListNode *l1, struct ListNode *l2)
{
    int var1, var2;
    struct ListNode *t1 = l1, *t2 = l2, *head = l1;
    int count = 0;
    if (l1 == NULL && l2 == NULL)
    {
        return NULL;
    }

    if (l1 != NULL && l2 == NULL)
    {
        return t1;
    }
    else if (l2 != NULL && l1 == NULL)
    {
        return t2;
    }
    else
    {
        while (1)
        {

            if (t2 == NULL)
            {
                break;
            }
            listPrint(head);
            printf("t1.val =%d ", t1->val);
            var1 = t1->val;

            printf("t2.val =%d \n", t2->val);
            var2 = t2->val;

            struct ListNode *t = (struct ListNode *)malloc(sizeof(struct ListNode));
            t->next = NULL;
            t->val = var2;

            if (var2 >= var1)
            {
                printf("var2 > var1 \n");
                if (t1->next != NULL)
                {
                    if (t1->next->val > var2)
                    {
                        t->next = t1->next;
                        t1->next = t;
                        t2 = t2->next;
                    }
                }
                else
                {
                    t1->next = t;
                    t2 = t2->next;
                    t1 = head;
                    printf("restart \n");
                    continue;
                }
            }
            else
            {
                printf("var2 < var1 \n");
                if (t1 != NULL)
                {
                    //只有头指针跟t1指针相等才能头插，不然要connect
                    if (t1 == head)
                    {
                        printf("set head \n");
                        t->next = t1;
                        head = t;
                        t1 = head;
                        t2 = t2->next;
                        continue;
                    }
                    else{
                        printf("connect \n");

                    }

                    // printf("two num connect \n");
                    // t->next = t1->next;
                    // t1->next = t;
                }
                else //只有一个结点
                {
              
                }

                t2 = t2->next;
            }
            t1 = t1->next;

        }
    }
    return head;
}

int main()
{

    struct ListNode *head1 = initList();
    // insertNode(head1, 1);
    //     insertNode(head1, 2);
    insertNode(head1, -2);
    insertNode(head1, 5);

    freeLastOne(head1);
    //listPrint(head1);
    struct ListNode *head2 = initList();
    insertNode(head2, -9);
    insertNode(head2, -2);
    insertNode(head2, 5);
    insertNode(head2, -6);
    insertNode(head2, -3);
    insertNode(head2, -1);
    insertNode(head2, 1);
    insertNode(head2, 6);

    insertNode(head2, 5);

    freeLastOne(head2);
    //listPrint(head2);
    struct ListNode *out = mergeTwoLists(head1, head2);
    listPrint(out);

    return 0;
}