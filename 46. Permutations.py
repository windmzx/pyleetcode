from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        n=len(nums)
        def helper(temp,templist):
            if len(temp)==n:
                res.append(temp)
                return
            for i in range(len(templist)):
                helper(temp+[templist[i]],templist[:i]+templist[i+1:])
        helper([],nums)
        return res
if __name__ == "__main__":
    x=Solution()
    print(x.permute([1,2,3]))