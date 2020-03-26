from typing import List
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if s > sum (nums):
            return 0
        res,sum_,i = 0,0,0

        for j in range(len(nums)):
            sum_+=nums[j]
            while sum_>=s:
                res=j-i+1 if res==0 else min(j-i+1,res)
                sum_-=nums[i]
                i+=1
        return res

if __name__ == "__main__":
    s=Solution()
    print(s.minSubArrayLen(2,[2,3,4,5]))
    