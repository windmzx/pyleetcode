from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        odd=[]
        for i in range(len(nums)):
            if nums[i]%2==1:
                odd.append(i)
        odd=[-1]+odd+[len(nums)]
        res=0
        for i in range(1,len(odd)-k):
            res+=(odd[i]-odd[i-1])*(odd[i+k]-odd[i+k-1])
        return res

if __name__ == "__main__":
    x = Solution()
    print(x.numberOfSubarrays([2, 2, 2, 1, 2, 2, 1, 2, 2, 2], 2))
