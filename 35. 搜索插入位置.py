from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if nums is None or len(nums)==0:
            return 0
        left=0
        right=len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                right=mid-1
            elif nums[mid]<target:
                left=mid+1
        return left
if __name__ == "__main__":
    x=Solution()
    print(x.searchInsert([1,3,5,6],2))