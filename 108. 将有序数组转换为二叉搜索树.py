# -*- encoding: utf-8 -*-
'''
@File    :   108. 将有序数组转换为二叉搜索树.py
@Time    :   2020/04/27 16:01:28
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
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums)==0:
            return None
        length=len(nums)
        mid=length//2
        root=TreeNode(nums[mid])

        root.left=self.sortedArrayToBST(nums[0:mid])
        root.right=self.sortedArrayToBST(nums[mid+1:])
        return root

if __name__ == "__main__":
    x=Solution()
    res=x.sortedArrayToBST([1,2,3,4,5,6])
    print()