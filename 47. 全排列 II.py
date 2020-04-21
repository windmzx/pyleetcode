from typing import List
import copy


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        temp = []
        dic={}
        for num in nums:
            dic[num]=dic.get(num,0)+1

        def backTrace(temp):
            if len(temp) == n:
                res.append(copy.deepcopy(temp))
            for key in dic.keys():
                if dic[key]==0:
                    continue
                temp.append(key)
                dic[key]-=1
                backTrace(temp)
                dic[key]+=1 
                temp.pop()
        backTrace([])
        return res
if __name__ == "__main__":
    x=Solution()
    print(x.permuteUnique([1,1,3]))

