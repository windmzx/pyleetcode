# -*- encoding: utf-8 -*-
'''
@File    :   154. 寻找旋转排序数组中的最小值 II.py
@Time    :   2020/05/05 14:34:24
@Author  :   windmzx 
@Version :   1.0
@Desc    :   For leetcode template
'''

# here put the import lib
from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left=0
        right=len(nums)-1
        while left<right:
            mid=(left+right)//2
            if nums[mid]<nums[right]:
                right=mid
            elif nums[mid]>nums[right]:
                left=mid+1
            else:
                right-=1
        return nums[left]


if __name__ == "__main__":
    x=Solution()
    print(x.findMin([6,7,1,1,2,3,4,5]))