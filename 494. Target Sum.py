from typing import List
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        if sum(nums)<S:
            return 0
        if (S+sum(nums))%2==1:
            return 0

        S=(S+sum(nums))//2
        dp=[0]*(S+1)
        dp[0]=1
        for num in nums:
            for i in range(S,num-1,-1):
                dp[i]+=dp[i-num]
            print(dp)
        return dp[S]
if __name__ == "__main__":
    x=Solution()
    x.findTargetSumWays([7,9,3,8,0,2,4,8,3,9],0)
