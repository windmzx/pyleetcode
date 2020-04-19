class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1=='0' or num2=='0':
            return '0'
        lnum1=len(num1)
        lnum2=len(num2)
        res=[0]*(lnum1+lnum2)
        for i in range(lnum1-1,-1,-1):
            for j in range(lnum2-1,-1,-1):
                temp=(ord(num1[i])-48)*(ord(num2[j])-48)
                temp+=res[i+j+1]
                res[i+j]+=temp//10
                res[i+j+1]=temp%10
        i=0
        result=''
        while res[i]==0:
            i+=1
        while i<lnum1+lnum2:
            result+=(str(res[i]))
            i+=1

        return result
if __name__ == "__main__":
    x=Solution()
    x.multiply("123","456")