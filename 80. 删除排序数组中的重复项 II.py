# -*- encoding: utf-8 -*-
'''
@File    :   80. 删除排序数组中的重复项 II.py
@Time    :   2020/04/22 12:27:21
@Author  :   windmzx 
@Version :   1.0
@Desc    :   For leetcode template
'''

# here put the import lib
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if nums is None:
            return 0
        ll=len(nums)
        if ll<3:
            return ll
        pernum=nums[0]
        num=1
        j=1
        for i in range(1,ll):
            if nums[i]==nums[i-1]:
                num+=1
                if num<=2:
                    nums[j]=nums[i]
                    j+=1
            else:
                num=1
                pernum=nums[i]
                nums[j]=nums[i]
                j+=1
        # print(nums)
        return j
            
if __name__ == "__main__":
    x=Solution()
    print(x.removeDuplicates([1,1,1,2,2,2,3,3,3,3,5,5]))