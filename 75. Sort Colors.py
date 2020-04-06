from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = len(nums)-1
        p = 0
        while left < right:
            if nums[left] == 2:
                nums[right], nums[left] = nums[left], nums[right]
                right -= 1
            elif nums[left] == 0:
                nums[p], nums[left] = nums[left], nums[p]
                p += 1
                left+=1
            else:
                left += 1


if __name__ == "__main__":
    x = Solution()
    l = [2, 0, 2, 1, 0]
    x.sortColors(l)
    print(l)
