from typing import  List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        res=0
        for j in range(1,len(height)):
            for i in range(j):
                weigth=j-i
                he=min(height[i],height[j])
                res=max(res,he*weigth)
        return res
if __name__ == "__main__":
    x=Solution()
    print(x.maxArea([1,8,6,2,5,4,8,3,7]))