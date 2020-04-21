from typing import List
import copy
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res=[]
        s=s.replace(".","")
        ll=len(s)
        def dfs(i,nums):
            if  len(nums)==4:
                if i==ll:
                
                    res.append(copy.deepcopy(nums))
                else:
                    return
            for j in range(1,4):
                if i+j<=ll:
                    char=s[i:i+j]
                    if int(char)>=0 and int(char)<256:
                        if len(char)>1 and char[0]=='0':
                            continue
                        nums.append(char)
                        dfs(i+j,nums) 
                        nums.pop()
        dfs(0,[])
        for i in range(len(res)):
            res[i]="{}.{}.{}.{}".format(res[i][0],res[i][1],res[i][2],res[i][3])
        return res 

if __name__ == "__main__":
    x=Solution()
    print(x.restoreIpAddresses("010010"
))