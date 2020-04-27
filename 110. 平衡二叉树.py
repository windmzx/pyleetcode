# -*- encoding: utf-8 -*-
'''
@File    :   110. 平衡二叉树.py
@Time    :   2020/04/27 21:12:31
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
    def isBalanced(self, root: TreeNode) -> bool:
        if root is None:
            return True

        def helper(root) -> int:
            if root is None:
                return 0
            lefth = helper(root.left)
            righth = helper(root.right)
            if lefth == -1 or righth == -1:
                return -1
            if abs(lefth-righth) > 1:
                return -1
            else:
                return max(lefth, righth)+1

        h = helper(root)
        if h != -1:
            return True
        return False


if __name__ == "__main__":
    x = Solution()
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)

    root.right = TreeNode(6)
    root.right.left = TreeNode(5)
    print(x.isBalanced(root))
