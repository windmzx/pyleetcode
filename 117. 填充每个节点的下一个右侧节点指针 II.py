# -*- encoding: utf-8 -*-
'''
@File    :   117. 填充每个节点的下一个右侧节点指针 II.py
@Time    :   2020/04/28 14:36:12
@Author  :   windmzx 
@Version :   1.0
@Desc    :   For leetcode template
'''

# here put the import lib
from typing import List


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root == None:
            return None
        if root.left:
            if root.right:
                root.left.next = root.right
            else:
                # 是父节点的左或者右
                if root.next:
                    root.left.next = self.getNextNode(root.next)
        if root.right:
            root.right.next = self.getNextNode(root.next)
        self.connect(root.right)
        self.connect(root.left)

        return root

    def getNextNode(self, root):
        while root:
            if root.left:
                return root.left
            if root.right:
                return root.right
            root = root.next
        return None


if __name__ == "__main__":
    x = Solution()
    print()
