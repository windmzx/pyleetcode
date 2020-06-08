# -*- encoding: utf-8 -*-
'''
@File    :   面试题19. 正则表达式匹配.py
@Time    :   2020/06/07 17:36:11
@Author  :   windmzx 
@Version :   1.0
@Desc    :   For leetcode template
'''

# here put the import lib
from typing import List


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)
        dp = [[False for _ in range(n+1)]for _ in range(m+1)]

        dp[0][0] = True

        for j in range(1,n+1):
            if p[j-1]=='*' and dp[0][j-2]:
                dp[0][j]=True  

        for i in range(1,m+1):
            for j in range(1,n+1):
                if s[i-1] == p[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '.':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    if j > 1:
                        if (s[i-1] == p[j-2] or p[j-2] == '.'):
                            # 1次或者多次
                            dp[i][j] = dp[i-1][j] or dp[i][j-1]
                        # 0次
                        dp[i][j] = dp[i][j]or dp[i][j-2]
        print(dp)
        return dp[m][n]


if __name__ == "__main__":
    x = Solution()
    print(x.isMatch("aab","c*a*b"))
