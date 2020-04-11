from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        ll=len(nums)
        if ll<2:
            return nums[0] if ll==1 else 0
        dp=[0]*ll
        dp[0]=nums[0]
        dp[1]=max(nums[0],nums[1])
        for i in range(2,ll-1):
            dp[i]=max(nums[i]+dp[i-2],dp[i-1])

        temp=dp[-1]

        dp[0]=0
        dp[1]=nums[1]
        for i in range(2,ll):
                        dp[i]=max(nums[i]+dp[i-2],dp[i-1])


        return max(dp[-1],temp)
if __name__ == "__main__":
    x=Solution()
    print(x.rob([2,1,1,2]))