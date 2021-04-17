# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if head==None:
            return None
        elif head.next==None:#如果只有头结点
            if head.val==val:
                return None
            return head
        tempHead= head
        # 如果删除的是头结点
        if tempHead.val==val:
            head=head.next
            return head
        while tempHead.next:
            if tempHead.next.val==val:
                tempHead.next=tempHead.next.next
                break
            tempHead=tempHead.next
        return head


