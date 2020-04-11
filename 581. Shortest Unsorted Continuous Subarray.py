from typing import List
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        ll=len(nums)
        left=0 
        right=ll-1
        maxv=float("-inf")
        minv=float("inf")
        R=0
        L=0
        while left<ll:
            if nums[left]<maxv:
                R=left
            maxv=max(maxv,nums[left])
            left+=1
        while right>=0:
            if nums[right]>minv:
                L=right
            minv=min(minv,nums[right])
            right-=1

        return 0 if L==R else R-L+1
if __name__ == "__main__":
    x=Solution()
    print(x.findUnsortedSubarray([1,2,3,9,8,7,10,11,12]))
