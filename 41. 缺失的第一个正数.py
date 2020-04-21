from typing import List
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while(nums[i]>0 and nums[i]<len(nums) and nums[i]!=nums[nums[i]-1]):
                temp=nums[nums[i]-1]
                nums[nums[i]-1]=nums[i]
                nums[i]=temp


        for i in range(0,len(nums)):
            if nums[i]!=i+1:
                return i+1
        return len(nums)+1
if __name__ == "__main__":
    x=Solution()
    print(x.firstMissingPositive([1,3,2]))