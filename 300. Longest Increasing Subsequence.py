from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp=[1]*len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i]>nums[j]:
                    dp[i]=max(dp[j]+1,dp[i])
        return max(dp)
if __name__ == "__main__":
    x=Solution()
    res=x.lengthOfLIS([10,9,2,5,3,7,20,18])
    print(res)