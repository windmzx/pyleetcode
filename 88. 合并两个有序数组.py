# -*- encoding: utf-8 -*-
'''
@File    :   88. 合并两个有序数组.py
@Time    :   2020/04/23 09:24:45
@Author  :   windmzx 
@Version :   1.0
@Desc    :   For leetcode template
'''

# here put the import lib
from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        index=m+n-1
        i=m-1
        j=n-1
        while i>=0 and j>=0:
            if nums1[i]>nums2[j]:
                nums1[index]=nums1[i]
                index-=1
                i-=1
            else:
                nums1[index]=nums2[j]
                j-=1
                index-=1
        while i>=0:
                nums1[index]=nums1[i]
                index-=1
                i-=1
        while j>=0:
                nums1[index]=nums2[j]
                j-=1
                index-=1

if __name__ == "__main__":
    x=Solution()
    print()