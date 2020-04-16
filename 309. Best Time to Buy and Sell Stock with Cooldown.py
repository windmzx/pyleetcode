from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<2:
            return 0
        dp=[[0,0,0] for _ in range(len(prices))]
        dp[0][1]=-prices[0]
        # 没股票 有股票 昨天卖了
        for i in range(1,len(prices)):
            dp[i][0]=max(dp[i-1][0],dp[i-1][2])

            dp[i][1]=max(dp[i-1][1],dp[i-1][0]-prices[i])

            dp[i][2]=dp[i-1][1]+prices[i]
        print(dp)
        return max(dp[-1][0],dp[-1][2])
if __name__ == "__main__":
    x=Solution()
    res=x.maxProfit([1,2,3,0,2])
    print(res)