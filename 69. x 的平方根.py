# -*- encoding: utf-8 -*-
'''
@File    :   69. x 的平方根.py
@Time    :   2020/04/22 09:48:50
@Author  :   windmzx 
@Version :   1.0
@Desc    :   For leetcode template
'''

# here put the import lib
from typing import List
import math
class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0 or x==1:
            return x
        left=1
        right=x//2
        while left<right:
            mid=math.ceil((left+right)/2)
            if mid*mid<=x:
                left=mid
            else:
                right=mid-1
        return left
if __name__ == "__main__":
    x=Solution()
    print(x.mySqrt(14))