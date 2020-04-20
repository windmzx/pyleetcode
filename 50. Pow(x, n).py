class Solution:
    def myPow(self, x: float, n: int) -> float:
        res=1
        i=n
        while i!=0:
            if i%2==1:
                res=res*x
            x=x*x
            i//=2
        return 1/res if n<0 else res
if __name__ == "__main__":
    x=Solution()
    # print(x.myPow(2,-2))
    print(-1//2)