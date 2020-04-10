from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:

        if len(matrix) == 0:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        res = 0
        heights = [0]*n
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '0':
                    heights[j] = 0
                else:
                    heights[j] += 1
            res = max(res, self.largestRectangleArea(heights))
        return res

    def largestRectangleArea(self, heights: List[int]) -> int:
        maxarea = 0
        heights = [0]+heights+[0]
        stack = []
        for i in range(len(heights)):
            # 栈顶元素大于当前元素
            while stack and heights[stack[-1]] > heights[i]:
                temp = stack.pop()
                maxarea = max(maxarea, (i-stack[-1]-1)*heights[temp])
            stack.append(i)
        return maxarea


if __name__ == "__main__":
    x = Solution()
    print(x.maximalRectangle(
        [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], [
            "1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]
    ))
