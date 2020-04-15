from typing import List
class Solution:
    def maxCoins(self, nums: List[int]) -> int:

        nums=[1]+nums+[1]
        length=len(nums)
        dp=[[0 for _ in range(length)] for _ in range(length)]

        for i in range(length-1,-1,-1):
            for j in range(i+2,length):
                for k in range(i+1,j):
                    dp[i][j]=max(dp[i][j],dp[i][k]+dp[k][j]+nums[k]*nums[i]*nums[j])
            print(dp)
        return dp[0][-1]
if __name__ == "__main__":
    x=Solution()
    res=x.maxCoins([3,1,5,8])
    print(res)