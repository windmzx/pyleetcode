from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = {}
        res=0
        dic[0]=1
        count=0
        for i in range(len(nums)):
            res+=nums[i]
            if res-k in dic.keys():
                count+=dic[res-k]
                print('find')
                print(dic[res-k])
            
            dic[res]=dic.get(res,0)+1
        return count

if __name__ == "__main__":
    x = Solution()
    print(x.subarraySum([1, 2, 1, 2,1], 3))
