# -*- encoding: utf-8 -*-
'''
@File    :   112. 路径总和.py
@Time    :   2020/04/28 09:18:35
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
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        
        def helper(root, sum):
            if root.left == None and root.right == None and sum == root.val:
                return True
            b1=False
            b2=False
            if root.left:
                b1 = helper(root.left, sum-root.val)
            if root.right:
                b2 = helper(root.right, sum-root.val)
            return b1 or b2
        if root is None:
            return False
        return helper(root, sum)

if __name__ == "__main__":
    x = Solution()
    root=TreeNode(1)
    root.left=TreeNode(2)
    root.right=TreeNode(3)
    print(x.hasPathSum(root,3))
