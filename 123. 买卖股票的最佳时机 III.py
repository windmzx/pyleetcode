# -*- encoding: utf-8 -*-
'''
@File    :   123. 买卖股票的最佳时机 III.py
@Time    :   2020/04/29 08:44:29
@Author  :   windmzx 
@Version :   1.0
@Desc    :   For leetcode template
'''

# here put the import lib
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ll=len(prices)
        dp1=[0 for _ in range(ll)]
        dp2=[0 for _ in range(ll)]
        minv=prices[0]
        maxv=prices[-1]
        res=0
        for i in range(1,ll):
            dp1[i]=max(dp1[i-1],prices[i]-minv)
            minv=min(minv,prices[i])

        for i in range(ll-2,-1,-1):
            dp2[i]=max(dp2[i+1],maxv-prices[i])
            maxv=max(maxv,prices[i])
        for i in range(ll-1):
            res=max(res,dp1[i]+dp2[i])
        return res
if __name__ == "__main__":
    x=Solution()
    print(x.maxProfit([1,2,3,4,5]
))