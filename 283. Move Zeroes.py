from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=0
        j=0
        while i<len(nums):
            if nums[i]!=0:
                nums[j]=nums[i]
                j+=1
            i+=1
        while j<len(nums):
            nums[j]=0
            j+=1

if __name__ == "__main__":
    x=Solution()
    r=[1,2,0,3,4]
    x.moveZeroes(r)
    print(r)
