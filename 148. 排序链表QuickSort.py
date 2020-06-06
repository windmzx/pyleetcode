# -*- encoding: utf-8 -*-
'''
@File    :   148. 排序链表QuickSort.py
@Time    :   2020/06/06 15:17:20
@Author  :   windmzx 
@Version :   1.0
@Desc    :   For leetcode template
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from untils.until import stringToListNode,ListNode

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        
        newhead=ListNode(-1)
        newhead.next=head
        return self.quickSort(newhead,None)

    def quickSort(self,head:ListNode,end:ListNode):
        if head == end or head.next == end or head.next.next == end:
            return head.next
        tmphead=ListNode(-1)
        
        part=head.next
        p=part
        tp=tmphead

        while p.next!=end:
            if p.next.val<part.val:
                tp.next=p.next
                tp=tp.next
                p.next=p.next.next
            else:
                p=p.next
        tp.next=head.next

        head.next=tmphead.next

        self.quickSort(head,part)
        self.quickSort(part,end)

        return head.next
    def listNodeToString(self,node):
        if not node:
            return "[]"

        result = ""
        while node:
            result += str(node.val) + ", "
            node = node.next
        return "[" + result[:-2] + "]"

if __name__ == "__main__":
    x=Solution()
    head=stringToListNode("[5,2,3,4,1]")
    res=x.sortList(head)
    print(x.listNodeToString(res))