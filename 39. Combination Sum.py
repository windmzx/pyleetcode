from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n=len(candidates)
        res=[]

        def helper(i,temp_sum,temp):
            if i==n or temp_sum>target:
                return
            if temp_sum==target:
                res.append(temp)
                return
            
            helper(i,temp_sum+candidates[i],temp+[candidates[i]])
            # helper(i,temp_sum+candidates[i],temp.addpend(candidates[i])
            helper(i+1,temp_sum,temp)
        
        helper(0,0,[])

        return res
if __name__ == "__main__":
    x=Solution()
    print(x.combinationSum([1,2,3,4],7))