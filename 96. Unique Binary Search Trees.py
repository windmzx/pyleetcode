class Solution:
    def numTrees(self, n: int) -> int:
        if n<2:
            return 1
        dp=[0]*(n+1)
        dp[0]=1
        dp[1]=1
        dp[2]=2
        for i in range(2,n):
            for j in range(0,i+1):
                print(j)
                print(i-j)
                dp[i+1]+=dp[j]*dp[i-j]
        return dp[-1]
if __name__ == "__main__":
    x=Solution()
    print(x.numTrees(3))