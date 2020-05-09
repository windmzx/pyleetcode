# -*- encoding: utf-8 -*-
'''
@File    :   面试题25. 合并两个排序的链表.py
@Time    :   2020/05/09 11:31:27
@Author  :   windmzx 
@Version :   1.0
@Desc    :   For leetcode template
'''

# here put the import lib
from typing import List
from untils.until import ListNode
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        tail = head
        while l1 and l2:
            if l1.val > l2.val:
                tail.next = l2
                l2 = l1.next
            else:
                tail.next = l1
                l1 = l1.next
            tail = tail.next
        while l1:
            tail.next=l1
            l1=l1.next
            tail = tail.next
        while l2:
            tail.next=l2
            l2=l2.next
            tail = tail.next
        return head.next
if __name__ == "__main__":
    x = Solution()
    print()
