# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return False
        p1=head
        p2=head.next
        while p1!=p2:
            if p2.next!=None and p2.next.next!=None:
                p1=p1.next
                p2=p2.next.next
        if p1==p2:
            p1=head
            while p1!=p2:
                p1=p1.next
                p2=p2.next
        else:
            return None
