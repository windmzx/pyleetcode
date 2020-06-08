# -*- encoding: utf-8 -*-
'''
@File    :   面试题26. 树的子结构.py
@Time    :   2020/06/08 11:13:38
@Author  :   windmzx 
@Version :   1.0
@Desc    :   For leetcode template
'''

# here put the import lib
from typing import List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from untils.until import TreeNode,stringToTreeNode
class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        def help(A, B):
            if B is None:
                return True
            if A == None:
                return False
            return A.val==B.val and  help(A.left, B.left) and help(A.right, B.right) 

        if A is None or B is None:
            return False
        return help(A,B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)
        


if __name__ == "__main__":
    x = Solution()
    A=stringToTreeNode("[4,2,3,4,5,6,7,8,9]")
    B=stringToTreeNode("[4,8,9]")
    print(x.isSubStructure(A,B))
