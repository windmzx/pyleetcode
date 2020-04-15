# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
            return True
        p1=head
        p2=head
        while p2!=None and p2.next!=None:
            p1=p1.next
            p2=p2.next.next
        p1.next=None

        cur=p2 
        per=p2.next
        while per !=None:
            temp=per.next
            per.next=cur
            cur=per
            per=temp
        p2.next=None

        while per and p1:
            if p1.val!=per.val:
                return False
        return True