from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in nums:
            x=abs(i)
            if nums[x-1]>0:
                nums[x-1]=-nums[x-1]
        res=[]
        for i in range(len(nums)):
            if nums[i]>0:
                res.append(i+1)
        return res
if __name__ == "__main__":
    x=Solution()
    print(x.findDisappearedNumbers([1,2,2,2,2,5]))