# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def __str__(self):
        return str(self.val)
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        def dfs(l1,l2):
            if l1==None:
                return l2
            elif l2==None:
                return l1
            mergedHead=ListNode(0)
            if(l1.val<l2.val):
                mergedHead=l1
                mergedHead.next=dfs(l1.next,l2)
            else:
                mergedHead=l2
                mergedHead.next=dfs(l1,l2.next)
            return mergedHead
        return dfs(l1,l2)



l1=ListNode(5)

l2=ListNode(1)
l2.next=ListNode(2)

l2.next.next=ListNode(3)
l2.next.next.next=ListNode(7)
Solution().mergeTwoLists(l1,l2)









