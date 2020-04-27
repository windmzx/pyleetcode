# -*- encoding: utf-8 -*-
'''
@File    :   103. 二叉树的锯齿形层次遍历.py
@Time    :   2020/04/26 10:33:04
@Author  :   windmzx 
@Version :   1.0
@Desc    :   For leetcode template
'''

# here put the import lib
from typing import List
import queue
import copy
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        stack=[]

        res=[]
        if root==None:
            return []
        stack.append(root)
        line=0
        while stack :
            temp=[]
            size=len(stack)
            while size>0:
                if line%2==0:
                    node=stack.pop(0)
                    if node.left:
                        stack.append(node.left)
                    if node.right:
                        stack.append(node.right)
                    temp.append(node.val)
                    size-=1
                elif line%2==1:
                    node=stack.pop(0)
                    if node.right:stack.append(node.right)
                    if node.left:stack.append(node.left)
                    temp.append(node.val)
                    size-=1
            stack.reverse()
            line+=1
            res.append(copy.deepcopy(temp))
        return res




if __name__ == "__main__":
    x=Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    root.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    print(x.zigzagLevelOrder(root))