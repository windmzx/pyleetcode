class Solution:
    def countAndSay(self, n: int) -> str:
        dic=['1','2','3']
        s='1'
        count=1
        for i in range(1,n):
            temp=""
            j=0
            while j<len(s):
                while j+1<len(s) and  s[j]==s[j+1]:
                    j+=1
                    count+=1
                temp+=str(count)
                temp+=str(s[j])
                count=1
                j+=1
            s=temp
            count=1
        return s
if __name__ == "__main__":
    x=Solution()
    print(x.countAndSay(12))
