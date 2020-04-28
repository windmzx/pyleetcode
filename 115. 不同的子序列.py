# -*- encoding: utf-8 -*-
'''
@File    :   115. 不同的子序列.py
@Time    :   2020/04/28 10:11:02
@Author  :   windmzx 
@Version :   1.0
@Desc    :   For leetcode template
'''

# here put the import lib
from typing import List


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if s == None or t == None:
            return 0
        if s == "" or t == "":
            return 0
        len1 = len(s)
        len2 = len(t)
        if len1 < len2:
            return 0
        dp = [[0 for _ in range(len1+1)]for _ in range(len2+1)]
        for i in range(len1+1):
            dp[0][i] = 1
        for i in range(1,len2+1):
            for j in range(1,len1+1):
                if s[j-1] == t[i-1]:
                    dp[i][j] = dp[i-1][j-1]+dp[i][j-1]
                else:
                    dp[i][j] = dp[i][j-1]
        print(dp)
        return dp[-1][-1]


if __name__ == "__main__":
    x = Solution()
    print(x.numDistinct("abbc", "abc"))
