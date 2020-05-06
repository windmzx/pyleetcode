# -*- encoding: utf-8 -*-
'''
@File    :   201. 数字范围按位与.py
@Time    :   2020/05/06 18:52:57
@Author  :   windmzx 
@Version :   1.0
@Desc    :   For leetcode template
'''

# here put the import lib
from typing import List


class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:

        if m == 2147483647:
            return 2147483647
        res = m
        for i in range(m+1, n+1):
            print(res)
            res = res & i
            print(res)
            if res == 0 or i == 2147483647:
                break
        return res


if __name__ == "__main__":
    x = Solution()
    print(x.rangeBitwiseAnd(600000000,2147483645))
