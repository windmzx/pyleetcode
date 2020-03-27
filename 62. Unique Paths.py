class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[1]*n
        
        for j in range(1,m):
            for i in range(1,n):
               dp[i]=dp[i]+dp[i-1]
        return dp[n-1]
if __name__ == "__main__":
    x=Solution()
    print(x.uniquePaths(3,3))
# 此题约等于一个杨辉三角形