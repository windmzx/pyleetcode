from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) < 2:
            return nums
        res = [0]*(len(nums)-k+1)
        curmax = float("-inf")
        for i in range(len(nums)):
            curmax = max(curmax, nums[i])
            # 只有当被出滑动窗口的数是最大值 且 入的数小于最大值的时候 才需要更新最大值
            if i > k-1 and nums[i] < curmax and nums[i-k] == curmax:
                curmax = float("-inf")
                for j in range(i-k+1, i+1):
                    curmax = max(curmax, nums[j])
            if i >= k-1:
                res[i-k+1] = curmax
        return res
if __name__ == "__main__":
    x=Solution()
    print(x.maxSlidingWindow([1,3,-1,-3,5,3,6,7],3))