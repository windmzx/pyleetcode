# -*- encoding: utf-8 -*-
'''
@File    :   701. 二叉搜索树中的插入操作.py
@Time    :   2020/06/05 16:44:46
@Author  :   windmzx 
@Version :   1.0
@Desc    :   For leetcode template
'''

# here put the import lib
from typing import List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            return
        if val > root.val :
            if root.right != None:
                self.insertIntoBST(root.right, val)
            else:
                root.right=TreeNode(val)
        if val < root.val:
            if root.left != None:
                self.insertIntoBST(root.left, val)
            else:
                root.left=TreeNode(val)    


if __name__ == "__main__":
    x = Solution()
    print()
