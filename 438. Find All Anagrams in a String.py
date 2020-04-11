from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        if len(s)<len(p):
            return []
        pmap = {}
        for i in p:
            pmap[i] = pmap.get(i, 0)+1

        tempmap = {}
        res = []
        r = plen-1
        l=0
        for i in range(len(p)-1):
            cha=s[i]
            tempmap[cha] = tempmap.get(cha, 0)+1

        while r<len(s):
            tempmap[s[r]]=tempmap.get(s[r],0)+1
            if tempmap==pmap:
                res.append(l)
            tempmap[s[l]]-=1
            if tempmap[s[l]]==0:
                tempmap.pop(s[l])

            l+=1
            r+=1
        return res


if __name__ == "__main__":
    x = Solution()
    print(x.findAnagrams("abcababc", 'abc'))
