class Solution:
    def countSubstrings(self, s: str) -> int:
        n=len(s)    
        dp=[[False] * n for i in range(n) ]
        res=0
        for i in range(n,-1,-1):
            for j in range(i,n):
                if( s[i]==s[j] and (j-i<=2 or dp[i+1][j-1]==True    ) ):
                    dp[i][j]=True
                    res+=1
        return res






    # 使用暴力搜索会导致运行时间过长 应该用dp
    # def countSubstrings(self, s: str) -> int:
    #     strs=[]
    #     n=len(s)
    #     for i in range(n):
    #         for j in range(i,n):
    #             strs.append(s[i:j+1])
    #     res=[ self.palindromic(i) for i in strs]
    #     print(strs)
    #     return res


    # def palindromic(self,s:str)->bool:
    #     if len(s)==0 or len(s)==1:
    #         return True
    #     if s[0]==s[-1]:
    #         return self.palindromic(s[1:-1])
    #     return False

if __name__ == "__main__":
    x=Solution()
    print(x.countSubstrings("fdsklf"))