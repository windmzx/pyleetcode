class Solution:
    def isAdditiveNumber(self, num: str) -> bool:

        length=len(num)


        def isactive(num1,num2,k):
            num3=num1+num2
            index=k+1
            while index<=length:
                if str(int(num[k:index]))==num[k:index] and int(num[k:index])==num3:
                    num1=num2
                    num2=num3
                    num3=num1+num2
                    return index==length or isactive(num1, num2, index)
                else:
                    index+=1
            return False

        for i in range(1,length//2+1):
            for j in range(1,length//2+1):                
                num1=int(num[:i]) 
                if str(int(num[i:i+j]))!=num[i:i+j]:
                    continue
                num2=int(num[i:i+j])
                if isactive(num1,num2, i+j):
                    return True
        return False
if __name__ == "__main__":
    x=Solution()
    print(x.isAdditiveNumber("1203"))