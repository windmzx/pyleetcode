# -*- encoding: utf-8 -*-
'''
@File    :   83. 删除排序链表中的重复元素.py
@Time    :   2020/04/22 19:46:05
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
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        tail=head
        cur=head.next
        while cur:
            if cur.val!=tail.val:
                tail.next=cur
                tail=tail.next
                cur=cur.next
        tail.next=None
        return head
if __name__ == "__main__":
    x=Solution()
    print()