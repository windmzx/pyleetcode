# -*- encoding: utf-8 -*-
'''
@File    :   91. 解码方法.py
@Time    :   2020/04/23 13:02:52
@Author  :   windmzx 
@Version :   1.0
@Desc    :   For leetcode template
'''

# here put the import lib
from typing import List


class Solution:
    def numDecodings(self, s: str) -> int:
        if s == None or len(s) == 0 or s[0] == '0':
            return 0
        ll = len(s)
        dp = [0] * (ll+1)
        dp[0]=1
        for i in range(1, ll+1):
            if s[i-1] == '0':
                dp[i] = 0
            else:
                dp[i] = dp[i-1]
            if i > 1 and (s[i-2] == '1' or(s[i-2] == '2' and ord(s[i-1]) <= 54)):
                dp[i] += dp[i-2]
        print(dp[-1])


if __name__ == "__main__":
    x = Solution()
    print(x.numDecodings("105"))
