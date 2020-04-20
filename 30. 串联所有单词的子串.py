from typing import List
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if words==None or s==None:
            return []
        m=len(words)
        n=len(words[0])
        if len(s)<m*n:
            return []
        map1={}
        res=[]
        for word in words:
            map1[word]=map1.get(word,0)+1
        for i in range(0,len(s)-m*n+1):
            map2={}            
            for j in range(i,i+m*n,n):
                st=s[j:j+n]
                if st not in map1.keys():
                    break
                map2[st]=map2.get(st,0)+1
            
            if map1==map2:
                res.append(i)
                
        return res
if __name__ == "__main__":
    x=Solution()
    print(x.findSubstring("abcdef123abcdef",["abc","def"])                )