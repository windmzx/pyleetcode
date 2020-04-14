# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head.next == None:
            return head
        re = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return re

    def reverseList2(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        cur=head
        per=None
        while cur!=None:
            temp=cur.next
            cur.next=per
            per=cur
            cur=temp

        return per


if __name__ == "__main__":
    x = Solution()
    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next=ListNode(1)
    re = x.reverseList2(head)
    print(re)
