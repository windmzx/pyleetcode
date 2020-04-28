# -*- encoding: utf-8 -*-
'''
@File    :   118. 杨辉三角.py
@Time    :   2020/04/28 21:34:15
@Author  :   windmzx 
@Version :   1.0
@Desc    :   For leetcode template
'''

# here put the import lib
from typing import List
import copy

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp1 = [1 for _ in range(numRows)]
        dp2 = [1 for _ in range(numRows)]
        for j in range(0, numRows):
            for i in range(1, j):
                dp2[i] = dp1[i]+dp1[i-1]
            dp1,dp2=dp2,dp1
        return dp1


if __name__ == "__main__":
    x = Solution()
    print(x.generate(3))
