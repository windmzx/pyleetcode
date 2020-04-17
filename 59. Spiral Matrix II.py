from typing import List 
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        num=1
        left=0 
        right=n
        top=0
        under=n-1

        row=0
        col=0
        res=[[0 for _ in range(n)]for _ in range(n)]
        while True:
            for i in range(left,right):
                res[left][i]=num
                num+=1
                if num>n*n:return res
            top+=1
            for i in range(top,under):
                res[i][right-1]=num
                num+=1
                if num>n*n:return res

            right-=1

            for i in range(right,left-1,-1):
                res[under][i]=num
                num+=1
                if num>n*n:return res

            under-=1

            for i in range(under,top-1,-1):
                res[i][left]=num
                num+=1
                if num>n*n:return res
            left+=1
        return res
if __name__ == "__main__":
    x=Solution()
    res=x.generateMatrix(4)
    print(res)
