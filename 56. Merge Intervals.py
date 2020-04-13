from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def quicksort(nums,start,end):
            if  start>=end:
                return
            sentinel=nums[start]
            left=start
            right=end
            print(start,end)
            while left<right:
                while left<right and nums[right][0]>=sentinel[0]:
                    right-=1
                nums[left]=nums[right]
                while left<right and nums[left][0]<=sentinel[0]:
                    left+=1
                nums[right]=nums[left]
            nums[left]=sentinel

            quicksort(nums,start,left-1)
            quicksort(nums,left+1,end)

        quicksort(intervals,0,len(intervals)-1)
        res=[]
        for i in range(0, len(intervals)-1):
            if intervals[i][1]>=intervals[i+1][0]:
                intervals[i+1][0]=intervals[i][0]
                intervals[i+1][1]=max(intervals[i+1][1],intervals[i][1])
            else:
                res.append(intervals[i])
        res.append(intervals[-1])
        return res

if __name__ == "__main__":
    x=Solution()
    text=[[362,367],[314,315],[133,138],[434,443],[202,203],[144,145],[229,235],[205,212],[314,323],[128,129],[413,414],[342,345],[43,49],[333,342],[173,178],[386,391],[131,133],[157,163],[187,190],[186,186],[17,19],[63,69],[70,79],[386,391],[98,102],[236,239],[195,195],[338,338],[169,170],[151,153],[409,416],[377,377],[90,96],[156,165],[182,186],[371,372],[228,233],[297,306],[56,61],[184,190],[401,403],[221,228],[203,212],[39,43],[83,84],[66,68],[80,83],[32,32],[182,182],[300,306],[235,238],[267,272],[458,464],[114,120],[452,452],[372,375],[275,280],[302,302],[5,9],[54,62],[237,237],[432,439],[415,421],[340,347],[356,358],[165,168],[15,17],[259,265],[201,204],[192,197],[376,383],[210,211],[362,367],[481,488],[59,64],[307,315],[155,164],[465,467],[55,60],[20,24],[297,304],[207,210],[322,328],[139,142],[192,195],[28,36],[100,108],[71,76],[103,105],[34,38],[439,441],[162,168],[433,433],[368,369],[137,137],[105,112],[278,280],[452,452],[131,132],[475,480],[126,129],[95,104],[93,99],[394,403],[70,78]]
    x2=x.merge(text)
    print(x2)