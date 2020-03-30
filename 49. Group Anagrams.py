from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic={}
        for s in strs:
            keys="".join(sorted(s))
            if keys in dic:
                dic[keys].append(s)
            else:
                dic[keys]=[s]  
        return list(dic.values())
if __name__ == "__main__":
    x=Solution()
    print(x.groupAnagrams(["a","aa","aab","aba"]))