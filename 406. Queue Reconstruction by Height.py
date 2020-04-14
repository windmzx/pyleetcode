from typing import List
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        flag=True
        while  flag:
            flag=False
            for i in range(1,len(people)):
                a1=people[i-1]
                a2=people[i]
                if a1[0]<a2[0]:
                    flag=True
                    people[i]=a1
                    people[i-1]=a2
                elif  a1[0]==a2[0]:
                    if a1[1]>a2[1]:
                        flag=True
                        people[i]=a1
                        people[i-1]=a2
        res=[]
        for p in people:
            res.insert(p[1],p)
        return res
if __name__ == "__main__":
    x=Solution()
    in1=[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

    res=x.reconstructQueue(in1)
    print(res)