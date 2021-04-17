# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> list[int]:
        if not head:
            return []
        vals=[]
        temp=head
        while temp.next:
            vals.append(temp.val)
            temp=temp.next
        vals.append(temp.val)
        return vals[::-1]