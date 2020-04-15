from typing import List
class Solution:
    def countBits(self, num: int) -> List[int]:
        dp=[0]*(num+1)
        dp[1]=1
        for i in range(2,num+1):
            if i%2==0:
                dp[i]=dp[i//2]
            else:
                dp[i]=dp[i-1]+1
        return dp
if __name__ == "__main__":
    x=Solution()
    res=x.countBits(10)
    print(res)