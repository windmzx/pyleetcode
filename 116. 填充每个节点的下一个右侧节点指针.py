# -*- encoding: utf-8 -*-
'''
@File    :   116. 填充每个节点的下一个右侧节点指针.py
@Time    :   2020/04/28 12:06:49
@Author  :   windmzx 
@Version :   1.0
@Desc    :   For leetcode template
'''

# here put the import lib
from typing import List

# Definition for a Node.


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None or root.left==None:
            return root
        root.left.next=root.right
        if root.next:
            root.right.next=root.next.left
        self.connect(root.left)
        self.connect(root.right)
            


if __name__ == "__main__":
    x = Solution()
    print()
