class Solution:
    def reverseWords(self, s: str) -> str:
        def reverse(start,end):
            while start<end:
                t=s[start]
                s[start]=s[end]
                s[end]=t
                start+=1
                end-=1
        i=0
        j=0
        l=len(s)
        while j< l:
            while j<l and  s[j]!=' ':
                j+=1
            reverse(i,j-1)
            i=j+1
        return s
if __name__ == "__main__":
    x=Solution()
    res=x.reverseWords("Let's take LeetCode contest")
    print(res)
