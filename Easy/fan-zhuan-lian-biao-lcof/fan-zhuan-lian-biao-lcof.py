# Definition for singly-linked list.
from copy import deepcopy


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def __str__(self):
        return str(self.val)
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head==None:
            return None
        cur=head.next
        head.next=None
        while cur:
            temp=cur.next
            cur.next=head
            head = cur
            cur=temp
        return head

l=ListNode(2)
l.next=ListNode(3)
l.next.next=ListNode(4)
Solution().reverseList(l)

