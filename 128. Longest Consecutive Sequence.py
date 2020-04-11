from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        res = 0
        for num in nums:
            # num是左边界
            if num-1 not in numset:
                currnum = num
                curlen = 1
                while currnum+1 in numset:
                    currnum += 1
                    curlen += 1
                res = max(res, curlen)
        return res

if __name__ == "__main__":
    x=Solution()
    print(x.longestConsecutive([1,2,4,5,0,10,23]))
