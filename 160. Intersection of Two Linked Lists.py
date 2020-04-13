# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA is None or headB is None:
            return None
        long1=1
        long2=1

        p=headA
        while p.next!=None:
            p=p.next
            long1+=1

        p=headB
        while p.next!=None:
            p=p.next
            long2+=1
        p1=headA
        p2=headB

        if long1>long2:
            diff=long1-long2
            while diff>=0:
                p1=p1.next
                diff-=1
        if long2>long1:
            diff=long2-long1
            while diff>=0:
                p2=p2.next
                diff-=1
        while p1.next!=None:
            if p1.val==p2.val:
                return p1
        return None