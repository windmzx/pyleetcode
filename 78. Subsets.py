from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        n=len(nums)

        def helper(index,templist):
            res.append(templist)

            for i in range(index,n):
                helper(i+1,templist+[nums[i]])
        helper(0,[])
        return res
if __name__ == "__main__":
    x=Solution()
    print(x.subsets([1,2,3,4]))