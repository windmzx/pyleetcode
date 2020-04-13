from typing import List
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def isvaild(s:str):
            count=0
            for i in s:
                if i=='(':
                    count+=1
                elif i==')':
                    count-=1
                if count<0:
                    return False
            if count==0:
                return True
            return False
        
        if isvaild(s):
            return [s]
        level={s}
        while 1:
            vaild=list(filter(isvaild,level))
            if vaild : return vaild
            nextlevel=set()
            for item in level:
                for i in range(len(item)):
                    if item[i] in "()":
                        nextlevel.add(item[:i]+item[i+1:])
            level= nextlevel
if __name__ == "__main__":
    x=Solution()
    s=x.removeInvalidParentheses("")
    print(s)