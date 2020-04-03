from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height)<=2:
            return 0
        left,right=1,len(height)-2
        leftmax=height[left-1]
        rightmax=height[right+1]
        res=0
        while left<=right:
            if leftmax<rightmax:
                if height[left]>leftmax:
                    leftmax=height[left]
                else:
                    res+=leftmax-height[left]
                left+=1
            else:
                if height[right]>rightmax:
                    rightmax=height[right]
                else:
                    res+=rightmax-height[right]
                right-=1
        return res
if __name__ == "__main__":
    x=Solution()
    print(x.trap([1,0,2,0,3]))
                