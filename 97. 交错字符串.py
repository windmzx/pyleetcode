# -*- encoding: utf-8 -*-
'''
@File    :   97. 交错字符串.py
@Time    :   2020/04/25 09:29:10
@Author  :   windmzx 
@Version :   1.0
@Desc    :   For leetcode template
'''

# here put the import lib
from typing import List


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        m = len(s1)
        n = len(s2)
        if m+n != len(s3):
            return False
        if m == 0:
            return s2 == s3
        if n == 0:
            return s1 == s3
        dp = [[False for _ in range(n+1)]for _ in range(m+1)]
        dp[0][0] = True
        for i in range(1, m+1):
            dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
        for i in range(1, n+1):
            dp[0][i] = dp[0][i-1] and s2[i-1] == s3[i-1]
        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[j+i-1]
                            ) or(dp[i][j-1] and s2[j-1] == s3[i+j-1])
        return dp[-1][-1]


if __name__ == "__main__":
    x = Solution()
    print(x.isInterleave("a", "", "a"))
