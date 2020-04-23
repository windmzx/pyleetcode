# -*- encoding: utf-8 -*-
'''
@File    :   面试题 08.11. 硬币.py
@Time    :   2020/04/23 09:15:20
@Author  :   windmzx 
@Version :   1.0
@Desc    :   For leetcode template
'''

# here put the import lib
from typing import List
class Solution:
    def waysToChange(self, n: int) -> int:
        dp=[0]*(n+1)
        dp[0]=1
        coins=[25,10,5,1]
        for conin in coins:
            for i in range(conin,n+1):
                dp[i]+=dp[i-conin]
        return dp[-1]
if __name__ == "__main__":
    x=Solution()
    print(x.waysToChange(10))