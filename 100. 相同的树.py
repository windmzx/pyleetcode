# -*- encoding: utf-8 -*-
'''
@File    :   100. 相同的树.py
@Time    :   2020/04/26 09:32:18
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
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if q==None :return p==None
        if p==None :return q==None
        
        if p==q:
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        else:
            return False
if __name__ == "__main__":
    x=Solution()
    print()