from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                return mid

            if nums[mid]<nums[right]:
                # 右边是有序的
                if nums[mid]<target and nums[right]>=target:
                    left=mid+1
                else:
                    right=mid-1
            else:
                # 左边是有序的
                if nums[mid]>target and nums[left]<=target:
                    right=mid-1
                else:
                    left=mid+1
        return -1
if __name__ == "__main__":
    x=Solution()
    print(x.search([4,5,6,1,2,3],1))