# -*- encoding: utf-8 -*-
'''
@File    :   161. 相隔为 1 的编辑距离.py
@Time    :   2020/05/05 15:07:55
@Author  :   windmzx 
@Version :   1.0
@Desc    :   For leetcode template
'''

# here put the import lib
from typing import List


# class Solution:
#     def isOneEditDistance(self, s: str, t: str) -> bool:
#         len1 = len(s)
#         len2 = len(t)
#         dp = [[1 for _ in range(len2+1)]for _ in range(len1+1)]
#         for i in range(len2+1):
#             dp[0][i]=i
#         for i in range(len1+1):
#             dp[i][0]=i
#         for i in range(1, len1+1):
#             for j in range(1, len2+1):
#                 if s[i-1] == t[j-1]:
#                     dp[i][j] = dp[i-1][j-1]
#                 else:
#                     dp[i][j] = min(dp[i-1][j], min(dp[i-1][j-1], dp[i][j-1]))+1
#         return dp[-1][-1]==1
class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        l1 = len(s)
        l2 = len(t)
        if abs(l1-l2) > 1:
            return False
        if l1 > l2:
            return self.isOneEditDistance(t, s)
        i = 0
        while i < l1:
            if s[i] != t[i]:
                if l1 == l2:
                    return s[i+1:] == t[i+1:]
                else:
                    return s[i:] == t[i+1:]
            else:
                pass
            i += 1
        return True

if __name__ == "__main__":
    x = Solution()
    print(x.isOneEditDistance("adc", "abc"))
