from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        ll=len(nums)
        if ll<2:
            return nums[0] if ll==1 else 0
        dp=[0]*ll
        dp[0]=nums[0]
        dp[1]=max(nums[0],nums[1])
        print(dp)
        for i in range(2,ll):
            dp[i]=max(nums[i]+dp[i-2],dp[i-1])
        
        return dp[-1]
if __name__ == "__main__":
    x=Solution()
    print(x.rob([]))