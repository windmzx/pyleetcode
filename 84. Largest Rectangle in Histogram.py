from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxarea=0
        heights=[0]+heights+[0]
        stack=[]
        for i in range(len(heights)):
            # 栈顶元素大于当前元素
            while stack  and heights[stack[-1]] > heights[i]:
                temp=stack.pop()
                maxarea=max(maxarea,(i-stack[-1]-1)*heights[temp])
            stack.append(i)
        return maxarea

if __name__ == "__main__":
    x=Solution()
    print(x.largestRectangleArea([1]))
