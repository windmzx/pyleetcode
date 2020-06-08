# -*- encoding: utf-8 -*-
'''
@File    :   面试题33. 二叉搜索树的后序遍历序列.py
@Time    :   2020/06/08 14:01:53
@Author  :   windmzx 
@Version :   1.0
@Desc    :   For leetcode template
'''

# here put the import lib
from typing import List


class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:

        def helper(nums):
            if len(nums)<=1:
                return True
            root=nums[-1]
            for i in range(len(nums)):
                if nums[i]>root:
                    break
            for j in range(i,len(nums)-1):
                if nums[j]<root:
                    return False
            return helper(nums[:i]) and helper(nums[i:-1])
        if not postorder:return True
        return helper(postorder)
if __name__ == "__main__":
    x=Solution()
    print(x.verifyPostorder(
        [4, 8, 6, 12, 16, 14, 10]
    ))