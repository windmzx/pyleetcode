# -*- encoding: utf-8 -*-
'''
@File    :   23. 合并K个排序链表.py
@Time    :   2020/04/26 10:07:33
@Author  :   windmzx 
@Version :   1.0
@Desc    :   For leetcode template
'''

# here put the import lib
from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        def mergeTwoLists(list1,list2):
            p1=list1
            p2=list2
            newhead=ListNode(0)
            tail=newhead
            while p1 and p2:
                if p1.val>p2.val:
                    tail.next=p2
                    tail=tail.next
                    p2=p2.next
                else:
                    tail.next=p1
                    tail=tail.next
                    p1=p1.next
            while p1:
                tail.next=p1
                tail=tail.next
                p1=p1.next
            while p2:
                tail.next=p2
                tail=tail.next
                p2=p2.next
            return newhead.next
        if len(lists)==1:
            return lists[0]
        res=lists[0]
        for list in lists[1:]:
            res=mergeTwoLists(res,list)
        return res

if __name__ == "__main__":
    x=Solution()
    print()