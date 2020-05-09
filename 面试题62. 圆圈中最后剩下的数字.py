# -*- encoding: utf-8 -*-
'''
@File    :   面试题62. 圆圈中最后剩下的数字.py
@Time    :   2020/05/09 09:57:53
@Author  :   windmzx 
@Version :   1.0
@Desc    :   For leetcode template
'''

# here put the import lib
from typing import List


class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        res = 0
        for i in range(2, n+1):
            res = (res+m) % i

        return res
if __name__ == "__main__":
    x = Solution()
    print(x.lastRemaining(5,3))
