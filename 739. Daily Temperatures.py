from typing import List
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        if T is None :
            return []
        if len(T)==1:
            return [0]
        le=len(T)

        res=[0]*le
        temp=0
        for i in range(le-2,-1,-1):
            if T[i]>=T[i+1]:
                temp+=1
                if res[i+temp]>0:
                    index=i+temp
                    while index <le:
                        if T[index]>T[i]:
                            res[i]=index-i
                            break
                        if res[index]>0:
                            index+=res[index]
                        else:
                            break                
                else:
                    temp=0
            else:
                res[i]=1
                temp=0
        return res
if __name__ == "__main__":
    x=Solution()
    print(x.dailyTemperatures([89,62,70,58,47,47,46,76,100,70]))
    print(x.dailyTemperatures([73,74,75,71,69,72,76,73]))

