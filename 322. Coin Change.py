from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        dp=[0]*(amount+1)
        dp[0]=0
        for i in range(1,amount+1):
            dp[i]=amount+1
            for j in coins:
                if i>=j:
                    dp[i]=min(dp[i-j]+1,dp[i])
        return dp[-1] if dp[-1]!=amount+1 else -1
if __name__ == "__main__":
    x=Solution()
    res=x.coinChange([1,2,5],11)
    print(res)