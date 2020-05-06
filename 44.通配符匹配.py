#
# @lc app=leetcode.cn id=44 lang=python3
#
# [44] 通配符匹配
#

# @lc code=start


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        len1 = len(s)
        len2 = len(p)
        dp = [[False for _ in range(len1+1)]for _ in range(len2+1)]
        dp[0][0]=True
        for i in range(1,len2+1):
            if p[i-1]=='*':
                dp[i][0]=dp[i-1][0]
                for j  in range(1,len1+1):
                    dp[i][j]= dp[i-1][j-1] or dp[i][j-1] or dp[i-1][j]
            elif p[i-1]=='?':
                dp[i][0]=False 
                for j in range(1,len1+1):
                    dp[i][j]=dp[i-1][j-1]
            else:
                dp[i][0]=False
                for j in range(1,len1+1):
                    dp[i][j]= p[i-1]==s[j-1] and dp[i-1][j-1]
        return dp[len2][len1]

if __name__ == "__main__":
    x=Solution()
    print(x.isMatch("a","a*"))


# @lc code=end
# 这种方法会超时
# def isMatch(self, s: str, p: str) -> bool:
    #  len1=len(s)
    #  len2=len(p)

    #  def dfs(p1,p2):
#         if p1==len1:
#             if p2==len2:
#                 return True
#             if  p[p2]=="*":
#                 return dfs(p1,p2+1)
#             return False
#         if p2==len2 and p1!=len1:
#             return False

#         if p[p2]=='?':
#             return dfs(p1+1,p2+1)
#         elif p[p2]=='*':
#         # * 可以为0 或者为1以上
#             return dfs(p1,p2+1) or dfs(p1+1,p2+1) or dfs(p1+1,p2)
#         elif s[p1]==p[p2]:
#             return dfs(p1+1,p2+1)
#         return False

#     return dfs(0,0)
