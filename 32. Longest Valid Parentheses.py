class Solution:
    def longestValidParentheses(self, s: str) -> int:
        dp=[0]*len(s)


        for i in range(1,len(s)):
            if s[i]==')':
                # 当遇到右括号的时候，去掉之前已经匹配好的括号的时候，并向前移动一位
                pre=i-dp[i-1]-1
                if pre>=0 and s[pre]=='(':
                    dp[i]=dp[i-1]+2
                    if pre>0:
                        dp[i]+=dp[pre-1]
        return max(dp)  
if __name__ == "__main__":
    x=Solution()
    print(x.longestValidParentheses("()()))))()()(()("))