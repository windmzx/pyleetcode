# -*- encoding: utf-8 -*-
'''
@File    :   86. 分隔链表.py
@Time    :   2020/04/22 20:08:32
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
    def partition(self, head: ListNode, x: int) -> ListNode:
        p1=ListNode(0)
        p2=ListNode(0)
        pp1=p1
        pp2=p2
        cur=head
        while cur:
            if cur.val<x:
                pp1.next=cur
                pp1=pp1.next
            else:
                pp2.next=cur
                pp2x=pp2.next
            cur=cur.next
        pp1.next=p2.next
        pp2.next=None
        return p1.next
if __name__ == "__main__":
    x=Solution()
    print()