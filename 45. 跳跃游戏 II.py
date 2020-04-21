from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:
        ll=len(nums)
        dp=[ll]*ll
        dp[0]=0
        for i in range(ll):
            for j in range(1,nums[i]+1):
                if i+j<ll:
                    dp[i+j]=min(dp[i+j],dp[i]+1)
        return dp[-1]
if __name__ == "__main__":
    x=Solution()
    print(x.jump([2,3,1,1,4]))