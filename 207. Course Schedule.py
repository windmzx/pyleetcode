from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        gradp=[[]for _ in range(numCourses)]
        du=[0]*numCourses
        for item in prerequisites:
            start=item[1]
            end=item[0]
            gradp[start].append(end)
            du[end]+=1
        
        queue=[]
        counter=0

        for i in range(numCourses):
            if du[i]==0:
                queue.append(i)
        while queue:
            te=queue.pop()
            counter+=1


            for i in gradp[te]:
                du[i]-=1
                if (du[i]==0):
                    queue.append(i)
        return counter==numCourses
        
