from typing import List
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        def swap(i,j):
            temp=nums[i]
            nums[i]=nums[j]
            nums[j]=temp
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums)==1:
            return
        i=len(nums)-1
        while(i-1>=0 and nums[i]<=nums[i-1]):
            i-=1
        # i就是要交换的位置
        if i!=0:
            j=len(nums)-1
            while j>=0 and nums[j]<=nums[i-1] :
                j-=1
            swap(i-1,j)
        k=len(nums)-1

        while i<k:
            swap(i,k)
            i+=1
            k-=1

        print(nums)
        
if __name__ == "__main__":
    x=Solution()
    x.nextPermutation([5,1,1])