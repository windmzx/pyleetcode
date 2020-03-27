from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp=[0]*len(nums)
        dp[0]=nums[0]
        for i in range(1,len(nums)):
            dp[i]=max(nums[i],nums[i]+dp[i-1])
        return max(dp)

if __name__ == "__main__":
    x=Solution()
    print(x.maxSubArray([1]))