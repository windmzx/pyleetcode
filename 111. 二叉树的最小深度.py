# -*- encoding: utf-8 -*-
'''
@File    :   111. 二叉树的最小深度.py
@Time    :   2020/04/27 21:33:35
@Author  :   windmzx 
@Version :   1.0
@Desc    :   For leetcode template
'''

# here put the import lib
from typing import List
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        if not root.left and root.right:
            return 1+self.minDepth(root.right)
        if not root.right and root.left:
            return 1+self.minDepth(root.left)
        return 1+min(self.minDepth(root.left), self.minDepth(root.right))


if __name__ == "__main__":
    x = Solution()
    print()
