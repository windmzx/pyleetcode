# -*- encoding: utf-8 -*-
'''
@File    :   106. 从中序与后序遍历序列构造二叉树.py
@Time    :   2020/04/27 14:40:23
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
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:

        def helper(inorder: List[int], postorder: List[int]) -> TreeNode:
            if len(inorder) == 0:
                return None
            curval = postorder[-1]
            root = TreeNode(curval)
            index = inorder.index(curval)
            root.left = helper(inorder[:index], postorder[:index])
            root.right = helper(inorder[index+1:], postorder[index:-1])
            return root
        if inorder is None or postorder is None:
            return None
        return helper(inorder, postorder)



if __name__ == "__main__":
    x = Solution()
    print(x.buildTree(
        [9, 3, 15, 20, 7],
        [9, 15, 7, 20, 3]
    ))
