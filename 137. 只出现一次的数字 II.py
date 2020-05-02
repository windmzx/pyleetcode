# -*- encoding: utf-8 -*-
'''
@File    :   137. 只出现一次的数字 II.py
@Time    :   2020/05/02 10:00:35
@Author  :   windmzx 
@Version :   1.0
@Desc    :   For leetcode template
'''

# here put the import lib
from typing import List


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in range(32):
            mask = 1 << i
            temp = 0
            for num in nums:
                if num & mask != 0:
                    temp += 1
            if temp%3!=0:
                res=res|mask
        return res


if __name__ == "__main__":
    x = Solution()
    print(x.singleNumber([-2,-2,1,1,-3,1,-3,-3,-4,-2]
))
