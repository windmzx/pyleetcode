# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False
        p1=head
        p2=p1.next
        while p2!=p1:
            if p1.next is None or p1.next.next is None:
                return False
            p1=p1.next
            p2=p2.next.next
        return True 