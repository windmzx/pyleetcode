from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums is None:
            return[]
        n=len(nums)
        res=[1]*n
        temp,temp2=1,1
        for i in range(n):
            res[i]*=temp
            temp*=nums[i]
        
            res[n-1-i]*=temp2
            temp2*=nums[n-1-i]
        return res
if __name__ == "__main__":
    x=Solution()
    print(x.productExceptSelf([1,2,3,4]))