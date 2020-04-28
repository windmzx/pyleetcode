# -*- encoding: utf-8 -*-
'''
@File    :   113. 路径总和 II.py
@Time    :   2020/04/28 09:56:31
@Author  :   windmzx 
@Version :   1.0
@Desc    :   For leetcode template
'''

# here put the import lib
from typing import List
import copy
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:

        res=[]
        def helper(root,nums:List[int],sum:int):
            if root.left==None and root.right==None and root.val==sum:
                res.append(copy.deepcopy(nums+[root.val]))
                return
            if root.left:
                helper(root.left,nums+[root.val],sum-root.val)
            if root.right:
                helper(root.right,nums+[root.val],sum-root.val)
        if root is None:
            return []
        return helper(root,[],0)
if __name__ == "__main__":
    x=Solution()
    print()