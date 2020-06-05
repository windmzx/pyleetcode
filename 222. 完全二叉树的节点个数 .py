# -*- encoding: utf-8 -*-
'''
@File    :   222. 完全二叉树的节点个数 .py
@Time    :   2020/06/05 14:51:21
@Author  :   windmzx
@Version :   1.0
@Desc    :   For leetcode template
'''
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        lh = self.deep(root.left)
        rh = self.deep(root.right)
        if lh == rh:
            return 1 + (1 << lh)-1+self.countNodes(root.right)
        else:
            return 1 + (1 << rh)-1+self.countNodes(root.left)

    def deep(self, root: TreeNode):
        d = 0
        while root != None:
            root = root.left
            d += 1
        return d


if __name__ == "__main__":
    x = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left=TreeNode(4)
    root.left.right=TreeNode(5)
    root.right.left=TreeNode(6)
    print(x.countNodes(root))
