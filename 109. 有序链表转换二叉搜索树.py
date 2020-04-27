# -*- encoding: utf-8 -*-
'''
@File    :   109. 有序链表转换二叉搜索树.py
@Time    :   2020/04/27 16:42:29
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

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if head==None:
            return None
        if head.next==None:
            return TreeNode(head.val)
        pre=head
        slow=head.next
        fast=head.next.next
        while fast and fast.next:
            pre=pre.next
            slow=slow.next
            fast=fast.next.next
        pre.next=None
        root=TreeNode(slow.val)
        root.left=self.sortedListToBST(head)
        root.right=self.sortedListToBST(slow.next)
        return root

if __name__ == "__main__":
    x=Solution()
    print()