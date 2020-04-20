from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res=[]
        def dfs(i,tempsum,tempnum):
            if tempsum>target:
                return
            if tempsum==target:
                res.append(tempnum)
                return
            for j in range(i,len(candidates)):
                if tempsum+candidates[j]>target:
                    continue
                if j>i and candidates[j]==candidates[j-1]:
                    continue
                dfs(j+1,tempsum+candidates[j],tempnum+[candidates[j]])
        dfs(0,0,[])
        return res
if __name__ == "__main__":
    x=Solution()
    print(x.combinationSum2([10,1,2,7,6,1,5]
,8))