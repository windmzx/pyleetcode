from typing import List
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        form=[1]*(n+1)
        source=[i for i in range(1,n+1)]
        res=""
        for i in range(1,n+1):
            form[i]=form[i-1]*i
        i=n
        k=k-1
        while n>0:
            index=k//form[n-1]
            res+=str(source[index])
            k=k%form[n-1]
            n-=1
            source.pop(index)
        return res





if __name__ == "__main__":
    x=Solution()
    res=x.getPermutation(4,5)
    print(res)