from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        dp = [[0 for _ in range(n)]for _ in range(m)]
        res=0
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = int(matrix[i][j])
                else:
                    if matrix[i][j] == '1':
                        dp[i][j]=1+min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
                    else:
                        dp[i][j]=0
                res=max(res,dp[i][j])
        return res*res


if __name__ == "__main__":
    x = Solution()
    print(x.maximalSquare([["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], [
          "1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]))
