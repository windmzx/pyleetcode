# -*- encoding: utf-8 -*-
'''
@File    :   450. 删除二叉搜索树中的节点.py
@Time    :   2020/06/05 17:44:11
@Author  :   windmzx 
@Version :   1.0
@Desc    :   For leetcode template
'''

# here put the import lib
from typing import List
from untils.until import TreeNode, stringToTreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root is None:
            return None
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
            return root
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
            return root
        else:
            if root.left == None:
                return root.right
            elif root.right == None:
                return root.left
            newroot = self.moveMinToRoot(root.right)
            newroot.left = root.left
            return newroot

    def moveMinToRoot(self, root: TreeNode):
        if root.left == None:
            return root
        curr = root.left
        pre = root
        while curr.left:
            pre = curr
            curr = curr.left
        pre.left = curr.right
        curr.right = root
        return curr


if __name__ == "__main__":
    x = Solution()
    print()
