
from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left=0
        right=len(nums)-1
        while(left<right):
            mid=(left+right)//2
            if nums[mid]>=target:
                # 等于的时候不加1
                right=mid
            else:
                left=mid+1
        # 这里有个点 就是right永远不会为target 又因为l<r 他们会逐渐逼近 left=mid+1 left应该就是左边界
        if nums[left]!=target: return [-1,-1]
        resl=left
# 现在开始寻找右边界
        right=len(nums)
        while(left<right):
            mid=(left+right)//2
            if nums[mid]<=target:
                left=mid+1
            else:
                right=mid
        return [resl,left-1]
if __name__ == "__main__":
    x=Solution()
    print(x.searchRange([1],1))
        