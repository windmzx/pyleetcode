class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter

        if len(s)<len(t):
            return ""
        # 构建两个数组 来保存字符串中字符数量
        auxt=Counter(t)

        start,end=0, len(t) 

        auxs=Counter(s[start:end])

        minn=len(s)+1
        sstart=0
        while(end<=len(s)):
            while(self.check(auxs,auxt)):
                if minn > (end-start):
                    minn=  end-start 
                    sstart=start
                auxs[s[start]]-=1
                start+=1
            if end <len(s):
                auxs[s[end]]+=1
                end+=1
            else:
                # 到头之后结束算法
                break
        if minn<=len(s):
            return s[sstart:sstart+minn]
        else:
            return ""
    def check(self,auxs:[int],auxt:[int])-> bool:
        for i in auxt:
            if auxs[i]<auxt[i]:
                return False
        return True
if __name__ == "__main__":
    x=Solution()
    print(x.minWindow("a","b"))
