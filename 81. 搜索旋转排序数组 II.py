# -*- encoding: utf-8 -*-
'''
@File    :   81. 搜索旋转排序数组 II.py
@Time    :   2020/04/22 16:16:54
@Author  :   windmzx 
@Version :   1.0
@Desc    :   For leetcode template
'''

# here put the import lib
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left=0
        right=len(nums)-1
        while left<=right:
            # nums[mid]不可能等于target了
            if nums[left]==target or nums[right]==target:
                return True
            while left<right and nums[left]==nums[left+1]:left+=1
            while left<right and nums[right]==nums[right-1]:right-=1
            mid=(left+right)//2
            
            if nums[mid]==target:
                return True
            # 左边是有序的
            if nums[mid]>nums[left]:
                # 目标在左边
                if nums[mid]>target and nums[left]<target:
                    right=mid-1
                else:
                    left=mid+1

            # 右边是有序的
            elif nums[mid]<nums[right]:
                # 目标在右边
                if nums[mid]<target and nums[right]>target:
                    left=mid+1
                else:
                    right=mid-1

            else:
                left+=1
        return False



if __name__ == "__main__":
    x=Solution()
    print(x.search([1,3,1,1,1],3))