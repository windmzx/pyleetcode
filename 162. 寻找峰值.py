# -*- encoding: utf-8 -*-
'''
@File    :   162. 寻找峰值.py
@Time    :   2020/05/05 14:45:54
@Author  :   windmzx 
@Version :   1.0
@Desc    :   For leetcode template
'''

# here put the import lib
from typing import List
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        left=0
        right=len(nums)-1
        while left<right:
            mid=(left+right)//2
            if nums[mid]<nums[mid+1]:
                left=mid+1
            else:
                right=mid
        return left
if __name__ == "__main__":
    x=Solution()
    print(x.findPeakElement([1,2,3,1]))