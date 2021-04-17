
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

        printf("%d->", tempNode->val);
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
        tempNode->next = NULL;
        printf("free .. %d \n", tempNode->val);
        struct ListNode *t = tempNode->next;
        free(t);
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
    struct ListNode *out = initList();
    int var1 = -1, var2 = -1;
    struct ListNode *t1 = l1, *t2 = l2;
    int leng1 = 0, leng2 = 0;
    int i, j;
    while (t1 != NULL)
    {
        t1 = t1->next;
        leng1++;
    }
    while (t2 != NULL)
    {
        t2 = t2->next;
        leng2++;
    }
    if(leng2==0 && leng1==0){
        return NULL;
    }
   // leng2--;
   // leng1--;
    printf("leng1= %d  leng2= %d \n", leng1, leng2);

    int *arr1 = (int *)malloc((leng1 + leng2) * sizeof(int));

    int *arr2 = (int *)malloc(leng2 * sizeof(int));

    t1 = l1;
    t2 = l2;
    for (i = 0; i < leng1, t1!= NULL; i++)
    {
        arr1[i] = t1->val;
        t1 = t1->next;
    }
    for (i = 0; i < leng2, t2 != NULL; i++)
    {
        arr2[i] = t2->val;
        t2 = t2->next;
    }
    int curi = leng1;
    for (i = 0; i < leng2; i++)
    {
        // for (i = 0; i < curi; i++)
        // {
        //     printf("cur arr .. %d \n", arr1[i]);
        // }
        for (j = curi - 1; j >= 0; j--)
        {

            if (arr2[i] < arr1[j])
            {
                arr1[j + 1] = arr1[j];
            }
            else
            {
                // printf("break \n");
                break;
            }
        }
        arr1[j + 1] = arr2[i];
        curi++;
    }
    for (i = 0; i < leng2 + leng1; i++)
    {
        insertNode(out, arr1[i]);
        printf("arr .. %d \n", arr1[i]);
    }
    freeLastOne(out);
    return out;
}
