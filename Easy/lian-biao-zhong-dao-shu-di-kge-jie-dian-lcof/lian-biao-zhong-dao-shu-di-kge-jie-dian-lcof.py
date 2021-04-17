# Definition for singly-linked list.
from copy import  deepcopy


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        if head==None:
            return None
        temp=deepcopy(head)
        #先走k次
        for i in range(k):
            temp=temp.next
        # 然后大家一起走
        while temp:
            head=head.next
            temp=temp.next
        return head