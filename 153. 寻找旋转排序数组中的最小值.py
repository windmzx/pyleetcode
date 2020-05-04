# -*- encoding: utf-8 -*-
'''
@File    :   153. 寻找旋转排序数组中的最小值.py
@Time    :   2020/05/04 16:09:40
@Author  :   windmzx 
@Version :   1.0
@Desc    :   For leetcode template
'''

# here put the import lib
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        while left < right:

            mid = (left+right)//2
            if nums[mid]<nums[right]:
                right=mid
            else:
                left=mid+1
        return nums[left]



if __name__ == "__main__":
    x = Solution()
    print(x.findMin([3,4,5,1,2]))
