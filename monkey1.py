def main():
    line1=input().strip().split(" ")
    m=int(line1[0])
    s=int(line1[1])
    line2=input().strip().split(" ")
    array=[int(i)for i in line2]
    print(solution(m,s,array))
    # print(solution(6,5,[5 ,1, 1 ,1 ,2 ,3]))
def solution(m,s,array):
    left=0
    right=1
    cursum=array[0]
    res=0
    while left<=right and right<m:
        if cursum<=s :
            if right-left+1 >res:
                res=max(res,right-left)
            cursum+=array[right]
            right+=1

        elif cursum>s:
            cursum-=array[left]
            left+=1
    return res        
main()