# -*- encoding: utf-8 -*-
'''
@File    :   144. 二叉树的前序遍历.py
@Time    :   2020/05/03 11:43:30
@Author  :   windmzx 
@Version :   1.0
@Desc    :   For leetcode template
'''

# here put the import lib
from typing import List
from untils.until import TreeNode
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack=[]
        if root:
            stack.append(root)
        res=[]
        while len(stack)!=0:
            node=stack.pop(0)
            res.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)      
        return res      
if __name__ == "__main__":
    x=Solution()
    print()