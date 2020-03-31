class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m=len(word1)
        n=len(word2)
# TODO 这个地方可以尝试使用两个数组
        dp=[[0] * (n+1) for i in range(m+1) ]
        for i in range(1,m+1):
            dp[i][0]=i
        for i in range(1,n+1):
            dp[0][i]=i
        
        for i in range(m):
            for j in range(n):
                if word1[i]==word2[j]:
                    dp[i+1][j+1]=dp[i][j]
                else:    
                    dp[i+1][j+1]=1+min(dp[i][j+1],dp[i+1][j],dp[i][j])
        return dp[-1][-1]
